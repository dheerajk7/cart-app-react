#!/usr/bin/env python3
"""
Convert field-documentation.md to PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from datetime import datetime
import re

def create_cover_page(canvas_obj, doc):
    """Create a professional cover page"""
    canvas_obj.saveState()
    
    # Background color
    canvas_obj.setFillColor(HexColor('#2C3E50'))
    canvas_obj.rect(0, 0, letter[0], letter[1], fill=1)
    
    # Title
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont("Helvetica-Bold", 32)
    title = "Complete Field Documentation"
    title_width = canvas_obj.stringWidth(title, "Helvetica-Bold", 32)
    canvas_obj.drawString((letter[0] - title_width) / 2, letter[1] - 200, title)
    
    canvas_obj.setFont("Helvetica-Bold", 24)
    subtitle = "Artificial Jewellery E-Commerce Platform"
    subtitle_width = canvas_obj.stringWidth(subtitle, "Helvetica-Bold", 24)
    canvas_obj.drawString((letter[0] - subtitle_width) / 2, letter[1] - 240, subtitle)
    
    # Description
    canvas_obj.setFont("Helvetica", 16)
    desc_text = "Prisma Database Schema & Sanity CMS Schema"
    desc_width = canvas_obj.stringWidth(desc_text, "Helvetica", 16)
    canvas_obj.drawString((letter[0] - desc_width) / 2, letter[1] - 300, desc_text)
    
    # Date
    canvas_obj.setFont("Helvetica", 12)
    date_text = f"Generated: {datetime.now().strftime('%B %d, %Y')}"
    date_width = canvas_obj.stringWidth(date_text, "Helvetica", 12)
    canvas_obj.drawString((letter[0] - date_width) / 2, letter[1] - 500, date_text)
    
    canvas_obj.restoreState()

def parse_markdown(content):
    """Parse markdown content and return structured elements"""
    lines = content.split('\n')
    elements = []
    current_table = []
    in_table = False
    in_code_block = False
    code_block_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Skip empty lines (but preserve some spacing)
        if not line:
            if not in_table and not in_code_block:
                elements.append(('spacer', 0.1))
            i += 1
            continue
        
        # Code blocks
        if line.startswith('```'):
            if in_code_block:
                # End code block
                if code_block_lines:
                    elements.append(('code', '\n'.join(code_block_lines)))
                    code_block_lines = []
                in_code_block = False
            else:
                # Start code block
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue
        
        # Headers
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            elements.append(('header', level, text))
            i += 1
            continue
        
        # Horizontal rules
        if line.strip() == '---':
            elements.append(('hr',))
            i += 1
            continue
        
        # Tables
        if '|' in line and line.count('|') >= 2:
            if not in_table:
                in_table = True
                current_table = []
            
            # Skip separator rows (|---|---|)
            if re.match(r'^\|[\s\-\|:]+\|$', line):
                i += 1
                continue
            
            # Parse table row
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            current_table.append(cells)
            i += 1
            continue
        else:
            if in_table:
                if current_table:
                    elements.append(('table', current_table))
                    current_table = []
                in_table = False
        
        # Lists
        if line.strip().startswith('- '):
            text = line.strip()[2:]
            elements.append(('list_item', text))
            i += 1
            continue
        
        # Bold text (simple)
        # Regular paragraph
        elements.append(('paragraph', line))
        i += 1
    
    # Handle remaining table
    if in_table and current_table:
        elements.append(('table', current_table))
    
    return elements

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Parse markdown
    elements = parse_markdown(md_content)
    
    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles (check if they exist first)
    custom_styles = {
        'CustomTitle': ParagraphStyle(
            name='CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=HexColor('#2C3E50'),
            spaceAfter=30,
            alignment=TA_CENTER
        ),
        'CustomH1': ParagraphStyle(
            name='CustomH1',
            parent=styles['Heading1'],
            fontSize=20,
            textColor=HexColor('#2C3E50'),
            spaceAfter=12,
            spaceBefore=12
        ),
        'CustomH2': ParagraphStyle(
            name='CustomH2',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=HexColor('#34495E'),
            spaceAfter=10,
            spaceBefore=10
        ),
        'CustomH3': ParagraphStyle(
            name='CustomH3',
            parent=styles['Heading3'],
            fontSize=14,
            textColor=HexColor('#34495E'),
            spaceAfter=8,
            spaceBefore=8
        ),
        'CustomH4': ParagraphStyle(
            name='CustomH4',
            parent=styles['Heading4'],
            fontSize=12,
            textColor=HexColor('#34495E'),
            spaceAfter=6,
            spaceBefore=6
        ),
        'CodeBlock': ParagraphStyle(
            name='CodeBlock',
            parent=styles['Code'],
            fontSize=9,
            fontName='Courier',
            leftIndent=20,
            rightIndent=20,
            spaceAfter=12,
            backColor=HexColor('#F5F5F5'),
            borderColor=HexColor('#BDC3C7'),
            borderWidth=1,
            borderPadding=5
        ),
        'ListItem': ParagraphStyle(
            name='ListItem',
            parent=styles['Normal'],
            fontSize=10,
            leftIndent=20,
            bulletIndent=10,
            spaceAfter=4
        )
    }
    
    for name, style in custom_styles.items():
        if name not in styles.byName:
            styles.add(style)
    
    # Process elements
    for elem_type, *args in elements:
        if elem_type == 'header':
            level, text = args
            if level == 1:
                story.append(Paragraph(text, styles['CustomH1']))
            elif level == 2:
                story.append(Paragraph(text, styles['CustomH2']))
            elif level == 3:
                story.append(Paragraph(text, styles['CustomH3']))
            elif level == 4:
                story.append(Paragraph(text, styles['CustomH4']))
            else:
                story.append(Paragraph(text, styles['Normal']))
        
        elif elem_type == 'paragraph':
            text = args[0]
            # Convert markdown formatting to HTML-like tags for reportlab
            # Bold: **text** or **text**
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            # Inline code: `code`
            text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9">\1</font>', text)
            # Links: [text](url) - just show text
            text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
            
            story.append(Paragraph(text, styles['Normal']))
        
        elif elem_type == 'list_item':
            text = args[0]
            # Convert markdown formatting
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9">\1</font>', text)
            
            story.append(Paragraph(f"• {text}", styles['ListItem']))
        
        elif elem_type == 'code':
            code_text = args[0]
            story.append(Paragraph(code_text.replace('<', '&lt;').replace('>', '&gt;'), styles['CodeBlock']))
        
        elif elem_type == 'table':
            table_data = args[0]
            if not table_data:
                continue
            
            # Determine column widths
            num_cols = len(table_data[0]) if table_data else 1
            col_widths = [4.5 * inch / num_cols] * num_cols
            
            # Create table
            table = Table(table_data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495E')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), HexColor('#ECF0F1')),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HexColor('#F8F9FA')])
            ]))
            story.append(table)
            story.append(Spacer(1, 0.2*inch))
        
        elif elem_type == 'hr':
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=HexColor('#BDC3C7')))
            story.append(Spacer(1, 0.2*inch))
        
        elif elem_type == 'spacer':
            story.append(Spacer(1, args[0] * inch))
    
    # Build PDF
    doc.build(story, onFirstPage=create_cover_page, onLaterPages=lambda c, d: None)
    
    print(f"PDF generated successfully: {pdf_file}")

if __name__ == "__main__":
    md_file = "field-documentation.md"
    pdf_file = "field-documentation.pdf"
    
    try:
        convert_md_to_pdf(md_file, pdf_file)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()

