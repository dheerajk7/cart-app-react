#!/usr/bin/env python3
"""
Generate enhanced comprehensive PDF report with visual diagrams
for Artificial Jewellery E-Commerce Architecture
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.platypus.flowables import HRFlowable, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.graphics.shapes import Drawing, Rect, Line, String, Circle, Group
from reportlab.graphics import renderPDF
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib.utils import ImageReader
from datetime import datetime
import io

def create_cover_page(canvas_obj, doc):
    """Create a professional cover page"""
    canvas_obj.saveState()
    
    # Background color
    canvas_obj.setFillColor(HexColor('#2C3E50'))
    canvas_obj.rect(0, 0, letter[0], letter[1], fill=1)
    
    # Title
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont("Helvetica-Bold", 32)
    title = "Artificial Jewellery"
    title_width = canvas_obj.stringWidth(title, "Helvetica-Bold", 32)
    canvas_obj.drawString((letter[0] - title_width) / 2, letter[1] - 200, title)
    
    canvas_obj.setFont("Helvetica-Bold", 24)
    subtitle = "E-Commerce Platform"
    subtitle_width = canvas_obj.stringWidth(subtitle, "Helvetica-Bold", 24)
    canvas_obj.drawString((letter[0] - subtitle_width) / 2, letter[1] - 240, subtitle)
    
    # Architecture Document
    canvas_obj.setFont("Helvetica", 18)
    doc_text = "Detailed Architecture & Design Document"
    doc_width = canvas_obj.stringWidth(doc_text, "Helvetica", 18)
    canvas_obj.drawString((letter[0] - doc_width) / 2, letter[1] - 300, doc_text)
    
    # Enhanced version note
    canvas_obj.setFont("Helvetica", 14)
    enhanced_text = "Enhanced Edition with Visual Diagrams"
    enhanced_width = canvas_obj.stringWidth(enhanced_text, "Helvetica", 14)
    canvas_obj.drawString((letter[0] - enhanced_width) / 2, letter[1] - 330, enhanced_text)
    
    # Date
    canvas_obj.setFont("Helvetica", 12)
    date_text = f"Generated: {datetime.now().strftime('%B %d, %Y')}"
    date_width = canvas_obj.stringWidth(date_text, "Helvetica", 12)
    canvas_obj.drawString((letter[0] - date_width) / 2, letter[1] - 500, date_text)
    
    # Version
    canvas_obj.setFont("Helvetica", 10)
    version_text = "Version 2.0 - Enhanced"
    version_width = canvas_obj.stringWidth(version_text, "Helvetica", 10)
    canvas_obj.drawString((letter[0] - version_width) / 2, letter[1] - 520, version_text)
    
    canvas_obj.restoreState()

def draw_architecture_diagram():
    """Create high-level architecture diagram"""
    d = Drawing(500, 400)
    
    # Define positions
    frontend_x, frontend_y = 250, 350
    backend_x, backend_y = 250, 250
    sanity_x, sanity_y = 120, 150
    db_x, db_y = 250, 150
    razorpay_x, razorpay_y = 380, 150
    ai_x, ai_y = 250, 50
    
    box_width, box_height = 90, 50
    
    # Frontend box
    frontend_box = Rect(frontend_x - box_width/2, frontend_y - box_height/2, box_width, box_height,
                       fillColor=HexColor('#3498DB'), strokeColor=HexColor('#2980B9'), strokeWidth=2)
    d.add(frontend_box)
    d.add(String(frontend_x, frontend_y - 5, 'Frontend', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(frontend_x, frontend_y - 18, '(Next.js)', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # Backend box
    backend_box = Rect(backend_x - box_width/2, backend_y - box_height/2, box_width, box_height,
                      fillColor=HexColor('#E74C3C'), strokeColor=HexColor('#C0392B'), strokeWidth=2)
    d.add(backend_box)
    d.add(String(backend_x, backend_y - 5, 'Backend', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(backend_x, backend_y - 18, '(NestJS)', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # Sanity CMS box
    sanity_box = Rect(sanity_x - box_width/2, sanity_y - box_height/2, box_width, box_height,
                     fillColor=HexColor('#9B59B6'), strokeColor=HexColor('#8E44AD'), strokeWidth=2)
    d.add(sanity_box)
    d.add(String(sanity_x, sanity_y - 5, 'Sanity', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(sanity_x, sanity_y - 18, 'CMS', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # PostgreSQL box
    db_box = Rect(db_x - box_width/2, db_y - box_height/2, box_width, box_height,
                 fillColor=HexColor('#16A085'), strokeColor=HexColor('#138D75'), strokeWidth=2)
    d.add(db_box)
    d.add(String(db_x, db_y - 5, 'PostgreSQL', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(db_x, db_y - 18, '+ Prisma', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # Razorpay box
    razorpay_box = Rect(razorpay_x - box_width/2, razorpay_y - box_height/2, box_width, box_height,
                       fillColor=HexColor('#F39C12'), strokeColor=HexColor('#D68910'), strokeWidth=2)
    d.add(razorpay_box)
    d.add(String(razorpay_x, razorpay_y - 5, 'Razorpay', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(razorpay_x, razorpay_y - 18, 'Payment', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # AI Module box (dashed for future)
    ai_box = Rect(ai_x - box_width/2, ai_y - box_height/2, box_width, box_height,
                 fillColor=HexColor('#95A5A6'), strokeColor=HexColor('#7F8C8D'), strokeWidth=2,
                 strokeDashArray=[5, 3])
    d.add(ai_box)
    d.add(String(ai_x, ai_y - 5, 'AI Module', textAnchor='middle', fontSize=11, fillColor=colors.white, fontName='Helvetica-Bold'))
    d.add(String(ai_x, ai_y - 18, '(Future)', textAnchor='middle', fontSize=9, fillColor=colors.white))
    
    # Arrows
    arrow_color = HexColor('#34495E')
    arrow_width = 2
    
    # Frontend to Backend
    d.add(Line(frontend_x, frontend_y - box_height/2, backend_x, backend_y + box_height/2,
              strokeColor=arrow_color, strokeWidth=arrow_width))
    d.add(String(backend_x, (frontend_y + backend_y)/2, 'REST API', textAnchor='middle', fontSize=8, fillColor=arrow_color))
    
    # Backend to Sanity
    d.add(Line(backend_x - 30, backend_y - box_height/2, sanity_x, sanity_y + box_height/2,
              strokeColor=arrow_color, strokeWidth=arrow_width))
    d.add(String((backend_x + sanity_x)/2 - 20, (backend_y + sanity_y)/2, 'Content', textAnchor='middle', fontSize=8, fillColor=arrow_color))
    
    # Backend to PostgreSQL
    d.add(Line(backend_x, backend_y - box_height/2, db_x, db_y + box_height/2,
              strokeColor=arrow_color, strokeWidth=arrow_width))
    d.add(String(db_x, (backend_y + db_y)/2, 'Prisma ORM', textAnchor='middle', fontSize=8, fillColor=arrow_color))
    
    # Backend to Razorpay
    d.add(Line(backend_x + 30, backend_y - box_height/2, razorpay_x, razorpay_y + box_height/2,
              strokeColor=arrow_color, strokeWidth=arrow_width))
    d.add(String((backend_x + razorpay_x)/2 + 20, (backend_y + razorpay_y)/2, 'Payment', textAnchor='middle', fontSize=8, fillColor=arrow_color))
    
    # Backend to AI
    d.add(Line(backend_x, backend_y - box_height/2, ai_x, ai_y + box_height/2,
              strokeColor=arrow_color, strokeWidth=arrow_width, strokeDashArray=[5, 3]))
    d.add(String(ai_x, (backend_y + ai_y)/2, 'AI API', textAnchor='middle', fontSize=8, fillColor=arrow_color))
    
    return d

def draw_data_flow_diagram():
    """Create product data flow diagram"""
    d = Drawing(500, 300)
    
    # User request
    d.add(Rect(50, 230, 100, 40, fillColor=HexColor('#3498DB'), strokeColor=HexColor('#2980B9')))
    d.add(String(100, 250, 'User Request', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    # Backend
    d.add(Rect(200, 230, 100, 40, fillColor=HexColor('#E74C3C'), strokeColor=HexColor('#C0392B')))
    d.add(String(250, 250, 'Backend API', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    # Parallel queries
    d.add(Rect(50, 150, 100, 40, fillColor=HexColor('#9B59B6'), strokeColor=HexColor('#8E44AD')))
    d.add(String(100, 170, 'Sanity CMS', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    d.add(Rect(200, 150, 100, 40, fillColor=HexColor('#16A085'), strokeColor=HexColor('#138D75')))
    d.add(String(250, 170, 'PostgreSQL', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    # Merge
    d.add(Rect(350, 150, 100, 40, fillColor=HexColor('#F39C12'), strokeColor=HexColor('#D68910')))
    d.add(String(400, 170, 'Merge Data', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    # Response
    d.add(Rect(200, 70, 100, 40, fillColor=HexColor('#2ECC71'), strokeColor=HexColor('#27AE60')))
    d.add(String(250, 90, 'API Response', textAnchor='middle', fontSize=10, fillColor=colors.white))
    
    # Arrows
    arrow_color = HexColor('#34495E')
    d.add(Line(150, 250, 200, 250, strokeColor=arrow_color, strokeWidth=2))
    d.add(Line(250, 230, 250, 190, strokeColor=arrow_color, strokeWidth=2))
    d.add(Line(250, 230, 100, 170, strokeColor=arrow_color, strokeWidth=2))
    d.add(Line(300, 170, 350, 170, strokeColor=arrow_color, strokeWidth=2))
    d.add(Line(250, 150, 250, 110, strokeColor=arrow_color, strokeWidth=2))
    
    return d

def draw_db_relationship_diagram():
    """Create database relationship diagram"""
    d = Drawing(500, 400)
    
    # User table
    d.add(Rect(50, 320, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(110, 360, 'User', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(110, 345, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(110, 335, 'email, password', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # Product table
    d.add(Rect(250, 320, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(310, 360, 'Product', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(310, 345, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(310, 335, 'sanityId, sku, price', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # Variant table
    d.add(Rect(250, 220, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(310, 260, 'Variant', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(310, 245, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(310, 235, 'productId (FK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(310, 225, 'name, price, discount', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # Order table
    d.add(Rect(50, 220, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(110, 260, 'Order', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(110, 245, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(110, 235, 'userId (FK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(110, 225, 'totalAmount, status', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # OrderItem table
    d.add(Rect(150, 120, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(210, 160, 'OrderItem', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(210, 145, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(210, 135, 'orderId, productId (FK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(210, 125, 'quantity, price', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # Payment table
    d.add(Rect(50, 120, 80, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(90, 160, 'Payment', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(90, 145, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(90, 135, 'orderId (FK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(90, 125, 'razorpayId, status', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # CartItem table
    d.add(Rect(250, 120, 120, 60, fillColor=HexColor('#ECF0F1'), strokeColor=HexColor('#34495E'), strokeWidth=2))
    d.add(String(310, 160, 'CartItem', textAnchor='middle', fontSize=12, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    d.add(String(310, 145, 'id (PK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(310, 135, 'userId, productId (FK)', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    d.add(String(310, 125, 'quantity', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    # Relationships (arrows)
    rel_color = HexColor('#3498DB')
    # User -> Order
    d.add(Line(110, 320, 110, 280, strokeColor=rel_color, strokeWidth=2))
    d.add(String(120, 300, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # Product -> Variant
    d.add(Line(310, 320, 310, 280, strokeColor=rel_color, strokeWidth=2))
    d.add(String(320, 300, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # Order -> OrderItem
    d.add(Line(110, 220, 180, 180, strokeColor=rel_color, strokeWidth=2))
    d.add(String(145, 200, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # Order -> Payment
    d.add(Line(110, 220, 90, 180, strokeColor=rel_color, strokeWidth=2))
    d.add(String(100, 200, '1:1', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # Product -> OrderItem
    d.add(Line(310, 320, 240, 180, strokeColor=rel_color, strokeWidth=2))
    d.add(String(275, 250, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # User -> CartItem
    d.add(Line(170, 320, 310, 180, strokeColor=rel_color, strokeWidth=2))
    d.add(String(240, 250, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    # Product -> CartItem
    d.add(Line(310, 220, 310, 180, strokeColor=rel_color, strokeWidth=2))
    d.add(String(320, 200, '1:N', textAnchor='middle', fontSize=8, fillColor=rel_color))
    
    return d

def draw_payment_flow_diagram():
    """Create payment flow sequence diagram"""
    d = Drawing(500, 350)
    
    # Actors
    actors = ['User', 'Frontend', 'Backend', 'Razorpay']
    x_positions = [50, 150, 300, 450]
    
    # Draw vertical lines for actors
    for i, (actor, x) in enumerate(zip(actors, x_positions)):
        d.add(Line(x, 50, x, 320, strokeColor=HexColor('#BDC3C7'), strokeWidth=1))
        d.add(String(x, 330, actor, textAnchor='middle', fontSize=10, fillColor=HexColor('#2C3E50'), fontName='Helvetica-Bold'))
    
    # Flow steps
    y_pos = 300
    
    # Step 1: User clicks checkout
    d.add(Line(x_positions[0], y_pos, x_positions[1], y_pos, strokeColor=HexColor('#3498DB'), strokeWidth=2))
    d.add(String((x_positions[0] + x_positions[1])/2, y_pos + 10, 'Checkout', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 2: Frontend -> Backend: Create order
    d.add(Line(x_positions[1], y_pos, x_positions[2], y_pos, strokeColor=HexColor('#E74C3C'), strokeWidth=2))
    d.add(String((x_positions[1] + x_positions[2])/2, y_pos + 10, 'POST /orders', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 3: Backend -> Razorpay: Create payment
    d.add(Line(x_positions[2], y_pos, x_positions[3], y_pos, strokeColor=HexColor('#F39C12'), strokeWidth=2))
    d.add(String((x_positions[2] + x_positions[3])/2, y_pos + 10, 'Create Order', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 4: Razorpay -> Backend: Return order_id
    d.add(Line(x_positions[3], y_pos, x_positions[2], y_pos, strokeColor=HexColor('#16A085'), strokeWidth=2))
    d.add(String((x_positions[2] + x_positions[3])/2, y_pos + 10, 'order_id', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 5: Backend -> Frontend: Return payment details
    d.add(Line(x_positions[2], y_pos, x_positions[1], y_pos, strokeColor=HexColor('#9B59B6'), strokeWidth=2))
    d.add(String((x_positions[1] + x_positions[2])/2, y_pos + 10, 'Payment Data', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 6: Frontend -> Razorpay: Redirect
    d.add(Line(x_positions[1], y_pos, x_positions[3], y_pos, strokeColor=HexColor('#3498DB'), strokeWidth=2))
    d.add(String((x_positions[1] + x_positions[3])/2, y_pos + 10, 'Payment Page', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 7: User -> Razorpay: Complete payment
    d.add(Line(x_positions[0], y_pos, x_positions[3], y_pos, strokeColor=HexColor('#E74C3C'), strokeWidth=2))
    d.add(String((x_positions[0] + x_positions[3])/2, y_pos + 10, 'Pay', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 8: Razorpay -> Backend: Webhook
    d.add(Line(x_positions[3], y_pos, x_positions[2], y_pos, strokeColor=HexColor('#F39C12'), strokeWidth=2))
    d.add(String((x_positions[2] + x_positions[3])/2, y_pos + 10, 'Webhook', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    y_pos -= 30
    
    # Step 9: Backend -> Frontend: Success
    d.add(Line(x_positions[2], y_pos, x_positions[1], y_pos, strokeColor=HexColor('#2ECC71'), strokeWidth=2))
    d.add(String((x_positions[1] + x_positions[2])/2, y_pos + 10, 'Success', textAnchor='middle', fontSize=9, fillColor=HexColor('#2C3E50')))
    
    return d

def generate_pdf_report():
    """Generate the complete enhanced PDF report"""
    filename = "Artificial_Jewellery_ECommerce_Architecture_Enhanced.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_CENTER
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#34495E'),
        spaceAfter=12,
        spaceBefore=12
    ))
    
    styles.add(ParagraphStyle(
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
    ))
    
    # Cover page (handled separately)
    doc.build(story, onFirstPage=create_cover_page, onLaterPages=lambda c, d: None)
    
    # Rebuild with content
    story = []
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        ("1. Introduction", 3),
        ("2. Tech Stack", 4),
        ("3. High-Level Architecture", 5),
        ("4. NestJS Backend Modules", 6),
        ("5. Sanity CMS Content Schema", 7),
        ("6. Database Schema (Prisma)", 8),
        ("7. Database Relationships", 9),
        ("8. Product Flow & API Endpoints", 10),
        ("9. Ordering Logic", 11),
        ("10. Discount Logic", 12),
        ("11. Payment Integration (Razorpay)", 13),
        ("12. Payment Flow Diagram", 14),
        ("13. AI Recommendation Readiness", 15),
        ("14. Future Extensions", 16),
        ("15. Example Scenarios", 17),
        ("16. Conclusion", 18)
    ]
    
    for item, page_num in toc_items:
        story.append(Paragraph(f"{item} ........................... {page_num}", styles['Normal']))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # 1. Introduction
    story.append(Paragraph("1. Introduction", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    intro_text = """
    This document provides a comprehensive architecture and design specification for an Artificial 
    Jewellery E-Commerce Platform. The platform is designed to be highly scalable, maintainable, 
    and ready for future enhancements including AI-powered jewellery recommendations based on 
    dress images.
    
    The architecture leverages modern technologies including NestJS for the backend, Next.js for 
    the frontend, Sanity CMS for content management, PostgreSQL with Prisma ORM for data persistence, 
    and Razorpay for payment processing. The system is designed with modularity and scalability 
    as core principles, ensuring it can grow with business needs.
    
    <b>Key Design Principles:</b>
    <br/>• Modular architecture for independent scaling
    <br/>• Separation of content (CMS) and transactional data (Database)
    <br/>• Type-safe development with Prisma ORM
    <br/>• RESTful API design for frontend integration
    <br/>• Future-ready for AI/ML integration
    """
    story.append(Paragraph(intro_text, styles['Normal']))
    story.append(PageBreak())
    
    # 2. Tech Stack
    story.append(Paragraph("2. Tech Stack", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    tech_stack_data = [
        ['Component', 'Technology', 'Purpose'],
        ['Frontend Framework', 'Next.js 14+', 'Server-side rendering, React-based UI'],
        ['Backend Framework', 'NestJS', 'Modular, scalable Node.js backend'],
        ['Content Management', 'Sanity CMS', 'Headless CMS for product content'],
        ['Database', 'PostgreSQL', 'Relational database for transactional data'],
        ['ORM', 'Prisma', 'Type-safe database access'],
        ['Payment Gateway', 'Razorpay', 'Payment processing'],
        ['Future AI Module', 'Python/ML (TBD)', 'Image-based jewellery recommendations']
    ]
    
    tech_table = Table(tech_stack_data, colWidths=[2*inch, 2*inch, 3*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#ECF0F1')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HexColor('#F8F9FA')]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    story.append(tech_table)
    story.append(PageBreak())
    
    # 3. High-Level Architecture with Diagram
    story.append(Paragraph("3. High-Level Architecture", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("3.1 System Overview", styles['SectionHeading']))
    
    arch_text = """
    The system follows a layered architecture pattern with clear separation of concerns:
    
    <b>Presentation Layer (Next.js Frontend):</b> Handles user interactions, displays product 
    catalogs, manages shopping carts, and processes checkout flows. Implements server-side 
    rendering for SEO and performance.
    
    <b>Application Layer (NestJS Backend):</b> Contains business logic, API endpoints, authentication, 
    order processing, and integration with external services. Organized into feature modules for 
    maintainability.
    
    <b>Data Layer:</b> Consists of PostgreSQL database (transactional data) and Sanity CMS 
    (content data). Prisma ORM provides type-safe access to PostgreSQL.
    
    <b>External Services:</b> Razorpay for payments, Sanity CMS API for content, and future AI 
    service for recommendations.
    """
    story.append(Paragraph(arch_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Architecture diagram
    story.append(Paragraph("3.2 Architecture Diagram", styles['SectionHeading']))
    arch_diagram = draw_architecture_diagram()
    story.append(arch_diagram)
    story.append(Spacer(1, 0.2*inch))
    
    arch_diag_text = """
    <b>Key Interactions:</b>
    <br/>• Frontend communicates with Backend via REST API
    <br/>• Backend fetches product content from Sanity CMS
    <br/>• Backend stores transactional data in PostgreSQL via Prisma ORM
    <br/>• Backend processes payments through Razorpay
    <br/>• Backend will integrate with AI module for recommendations (future - shown in dashed lines)
    """
    story.append(Paragraph(arch_diag_text, styles['Normal']))
    story.append(PageBreak())
    
    # 4. NestJS Backend Modules
    story.append(Paragraph("4. NestJS Backend Modules", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    modules_text = """
    The NestJS backend is organized into feature modules following Domain-Driven Design principles. 
    Each module is self-contained with its own controllers, services, and DTOs.
    """
    story.append(Paragraph(modules_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Modules table
    modules_data = [
        ['Module', 'Responsibility', 'Key Endpoints'],
        ['Catalog', 'Product management, listings, search', 'GET /products, GET /products/:id, GET /categories'],
        ['Cart', 'Shopping cart management', 'POST /cart, GET /cart, PUT /cart/:id, DELETE /cart/:id'],
        ['Order', 'Order creation and management', 'POST /orders, GET /orders/:id, GET /orders'],
        ['Payment', 'Payment processing via Razorpay', 'POST /payments/create, POST /payments/verify'],
        ['User', 'User authentication and profiles', 'POST /auth/register, POST /auth/login, GET /user/profile'],
        ['Admin', 'Administrative operations', 'POST /admin/products, PUT /admin/products/:id']
    ]
    
    modules_table = Table(modules_data, colWidths=[1.5*inch, 3*inch, 2.5*inch])
    modules_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#ECF0F1')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HexColor('#F8F9FA')])
    ]))
    story.append(modules_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Catalog Module Details
    story.append(Paragraph("4.1 Catalog Module Structure", styles['SectionHeading']))
    catalog_structure = """
    <b>Folder Structure:</b>
    <br/>src/catalog/
    <br/>  ├── catalog.module.ts
    <br/>  ├── catalog.controller.ts
    <br/>  ├── catalog.service.ts
    <br/>  ├── catalog.repository.ts
    <br/>  ├── sanity-adapter.service.ts
    <br/>  ├── dto/
    <br/>  │   ├── product-response.dto.ts
    <br/>  │   ├── variant-response.dto.ts
    <br/>  │   └── product-query.dto.ts
    <br/>  └── entities/
    <br/>      └── product.entity.ts
    """
    story.append(Paragraph(catalog_structure, styles['CodeBlock']))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("4.2 Example Catalog Service Code", styles['SectionHeading']))
    catalog_service_code = """
    // catalog.service.ts
    import { Injectable } from '@nestjs/common';
    import { PrismaService } from '../prisma/prisma.service';
    import { SanityAdapterService } from './sanity-adapter.service';
    
    @Injectable()
    export class CatalogService {
      constructor(
        private prisma: PrismaService,
        private sanityAdapter: SanityAdapterService,
      ) {}
    
      async getProducts(query: ProductQueryDto) {
        // Query database
        const products = await this.prisma.product.findMany({
          where: { isActive: true, stock: { gt: 0 } },
          include: { variants: true },
          orderBy: [
            { stock: 'desc' },
            { displayRank: 'asc' },
            { createdAt: 'desc' }
          ],
          take: query.limit,
          skip: (query.page - 1) * query.limit,
        });
    
        // Fetch Sanity content for each product
        const productsWithContent = await Promise.all(
          products.map(async (product) => {
            const sanityData = await this.sanityAdapter
              .getProduct(product.sanityId);
            return this.mergeProductData(product, sanityData);
          })
        );
    
        return productsWithContent;
      }
    
      private mergeProductData(dbProduct, sanityData) {
        return {
          ...dbProduct,
          title: sanityData.title,
          description: sanityData.description,
          images: sanityData.images,
          badge: sanityData.badge,
          tags: sanityData.tags,
        };
      }
    }
    """
    story.append(Paragraph(catalog_service_code, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 5. Sanity CMS Content Schema
    story.append(Paragraph("5. Sanity CMS Content Schema", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    sanity_text = """
    Sanity CMS stores product content including descriptions, images, tags, and metadata. The 
    backend merges this content with database records that contain business logic data (stock, 
    prices, variants).
    """
    story.append(Paragraph(sanity_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Sanity Schema
    story.append(Paragraph("5.1 Product Schema", styles['SectionHeading']))
    sanity_schema = """
    // schemas/product.js
    export default {
      name: 'product',
      title: 'Product',
      type: 'document',
      fields: [
        {
          name: 'sanityId',
          title: 'Sanity ID',
          type: 'string',
          description: 'Unique identifier matching DB product.sanityId'
        },
        {
          name: 'title',
          title: 'Product Title',
          type: 'string',
          validation: Rule => Rule.required()
        },
        {
          name: 'description',
          title: 'Description',
          type: 'text',
          validation: Rule => Rule.required()
        },
        {
          name: 'images',
          title: 'Product Images',
          type: 'array',
          of: [{ 
            type: 'image',
            options: { hotspot: true }
          }]
        },
        {
          name: 'category',
          title: 'Category',
          type: 'reference',
          to: [{ type: 'category' }]
        },
        {
          name: 'tags',
          title: 'Tags',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            layout: 'tags'
          }
        },
        {
          name: 'badge',
          title: 'Badge (e.g., "New", "Sale")',
          type: 'string',
          options: {
            list: ['New', 'Sale', 'Trending', 'Featured']
          }
        },
        {
          name: 'displayRank',
          title: 'Display Rank (lower = higher priority)',
          type: 'number',
          description: 'Products with lower numbers appear first'
        }
      ],
      preview: {
        select: {
          title: 'title',
          media: 'images.0'
        }
      }
    }
    """
    story.append(Paragraph(sanity_schema, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 6. Database Schema (Prisma)
    story.append(Paragraph("6. Database Schema (Prisma)", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    prisma_intro = """
    The database schema is defined using Prisma ORM, providing type-safe database access. The 
    schema includes models for users, products, variants, orders, payments, and shopping carts.
    """
    story.append(Paragraph(prisma_intro, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    prisma_schema = """
    // prisma/schema.prisma
    
    generator client {
      provider = "prisma-client-js"
    }
    
    datasource db {
      provider = "postgresql"
      url      = env("DATABASE_URL")
    }
    
    model User {
      id        String   @id @default(cuid())
      email     String   @unique
      password  String
      name      String?
      phone     String?
      createdAt DateTime @default(now())
      updatedAt DateTime @updatedAt
      
      orders    Order[]
      cartItems CartItem[]
      
      @@map("users")
    }
    
    model Product {
      id          String   @id @default(cuid())
      sanityId    String   @unique
      sku         String   @unique
      basePrice   Decimal  @db.Decimal(10, 2)
      stock       Int      @default(0)
      isActive    Boolean  @default(true)
      createdAt   DateTime @default(now())
      updatedAt   DateTime @updatedAt
      
      variants    Variant[]
      orderItems  OrderItem[]
      cartItems   CartItem[]
      
      @@index([sanityId])
      @@index([isActive, stock])
      @@map("products")
    }
    
    model Variant {
      id          String   @id @default(cuid())
      productId   String
      name        String   // e.g., "Gold", "Silver"
      price       Decimal? @db.Decimal(10, 2)  // Overrides product.basePrice if set
      stock       Int      @default(0)
      sku         String   @unique
      discount    Decimal? @db.Decimal(5, 2)   // Percentage discount (variant-level)
      isActive    Boolean  @default(true)
      
      product     Product  @relation(fields: [productId], references: [id], onDelete: Cascade)
      
      @@index([productId])
      @@map("variants")
    }
    
    model Category {
      id          String   @id @default(cuid())
      name        String   @unique
      slug        String   @unique
      description String?
      parentId    String?
      parent      Category? @relation("CategoryHierarchy", fields: [parentId], references: [id])
      children    Category[] @relation("CategoryHierarchy")
      
      @@index([slug])
      @@map("categories")
    }
    
    model CartItem {
      id        String   @id @default(cuid())
      userId    String
      productId String
      variantId String?
      quantity  Int      @default(1)
      createdAt DateTime @default(now())
      
      user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
      product   Product  @relation(fields: [productId], references: [id], onDelete: Cascade)
      
      @@unique([userId, productId, variantId])
      @@map("cart_items")
    }
    
    model Order {
      id            String      @id @default(cuid())
      userId        String
      status        OrderStatus @default(PENDING)
      totalAmount   Decimal     @db.Decimal(10, 2)
      subtotal      Decimal     @db.Decimal(10, 2)
      discount      Decimal     @db.Decimal(10, 2) @default(0)
      shippingCost  Decimal     @db.Decimal(10, 2) @default(0)
      createdAt     DateTime    @default(now())
      updatedAt     DateTime    @updatedAt
      
      user          User        @relation(fields: [userId], references: [id])
      orderItems    OrderItem[]
      payment       Payment?
      shippingInfo  ShippingInfo?
      
      @@index([userId, status])
      @@map("orders")
    }
    
    model OrderItem {
      id            String   @id @default(cuid())
      orderId       String
      productId     String
      variantId     String?
      quantity      Int
      price         Decimal  @db.Decimal(10, 2)  // Price at time of order
      discount      Decimal  @db.Decimal(5, 2)   // Applied discount percentage
      
      order         Order    @relation(fields: [orderId], references: [id], onDelete: Cascade)
      product       Product  @relation(fields: [productId], references: [id])
      
      @@index([orderId])
      @@map("order_items")
    }
    
    model Payment {
      id            String       @id @default(cuid())
      orderId       String       @unique
      razorpayId    String?      @unique
      amount        Decimal      @db.Decimal(10, 2)
      status        PaymentStatus @default(PENDING)
      method        String?
      createdAt     DateTime     @default(now())
      updatedAt     DateTime     @updatedAt
      
      order         Order        @relation(fields: [orderId], references: [id])
      
      @@index([razorpayId])
      @@map("payments")
    }
    
    model ShippingInfo {
      id          String   @id @default(cuid())
      orderId     String   @unique
      name        String
      address     String
      city        String
      state       String
      pincode     String
      phone       String
      
      order       Order    @relation(fields: [orderId], references: [id])
      
      @@map("shipping_info")
    }
    
    enum OrderStatus {
      PENDING
      CONFIRMED
      PROCESSING
      SHIPPED
      DELIVERED
      CANCELLED
    }
    
    enum PaymentStatus {
      PENDING
      SUCCESS
      FAILED
      REFUNDED
    }
    """
    story.append(Paragraph(prisma_schema, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 7. Database Relationships Diagram
    story.append(Paragraph("7. Database Relationships", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    db_rel_text = """
    The database schema implements a relational model with clear foreign key relationships. The 
    diagram below illustrates the entity relationships.
    """
    story.append(Paragraph(db_rel_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    db_diagram = draw_db_relationship_diagram()
    story.append(db_diagram)
    story.append(Spacer(1, 0.2*inch))
    
    relationship_details = """
    <b>Key Relationships:</b>
    <br/>• User → Order (1:N): One user can have many orders
    <br/>• User → CartItem (1:N): One user can have many cart items
    <br/>• Product → Variant (1:N): One product can have many variants (colors, sizes)
    <br/>• Product → OrderItem (1:N): One product can appear in many order items
    <br/>• Product → CartItem (1:N): One product can be in many user carts
    <br/>• Order → OrderItem (1:N): One order contains many order items
    <br/>• Order → Payment (1:1): One order has one payment record
    <br/>• Order → ShippingInfo (1:1): One order has one shipping address
    """
    story.append(Paragraph(relationship_details, styles['Normal']))
    story.append(PageBreak())
    
    # 8. Product Flow & API
    story.append(Paragraph("8. Product Flow & API Endpoints", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    flow_text = """
    <b>Product Listing Flow:</b>
    <br/>1. Frontend requests product list: GET /api/catalog/products
    <br/>2. Backend queries PostgreSQL for active products with stock > 0
    <br/>3. For each product, fetch content from Sanity CMS using sanityId
    <br/>4. Merge database data (price, stock) with Sanity content (images, description)
    <br/>5. Apply ordering logic (in-stock first, then displayRank, then createdAt)
    <br/>6. Return paginated results
    """
    story.append(Paragraph(flow_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Data Flow Diagram
    story.append(Paragraph("8.1 Product Data Flow", styles['SectionHeading']))
    flow_diagram = draw_data_flow_diagram()
    story.append(flow_diagram)
    story.append(Spacer(1, 0.2*inch))
    
    # API Response Example
    story.append(Paragraph("8.2 API Response Example", styles['SectionHeading']))
    api_example = """
    // GET /api/catalog/products?page=1&limit=20&category=necklaces
    
    {
      "data": [
        {
          "id": "prod_123",
          "sanityId": "sanity_prod_123",
          "title": "Elegant Gold Necklace",
          "description": "Beautiful artificial gold necklace perfect for parties...",
          "images": [
            "https://cdn.sanity.io/images/abc123/image1.jpg",
            "https://cdn.sanity.io/images/abc123/image2.jpg"
          ],
          "basePrice": 1299.00,
          "stock": 45,
          "category": {
            "id": "cat_1",
            "name": "Necklaces",
            "slug": "necklaces"
          },
          "variants": [
            {
              "id": "var_1",
              "name": "Gold",
              "price": 1299.00,
              "stock": 30,
              "discount": null
            },
            {
              "id": "var_2",
              "name": "Rose Gold",
              "price": 1399.00,
              "stock": 15,
              "discount": 10.0
            }
          ],
          "badge": "New",
          "displayRank": 1,
          "tags": ["trending", "elegant", "party"]
        }
      ],
      "pagination": {
        "page": 1,
        "limit": 20,
        "total": 150,
        "totalPages": 8
      }
    }
    """
    story.append(Paragraph(api_example, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 9. Ordering Logic
    story.append(Paragraph("9. Ordering Logic", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    ordering_text = """
    Products are ordered using a multi-level sorting strategy to ensure the best user experience 
    and business goals:
    """
    story.append(Paragraph(ordering_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    ordering_logic = """
    <b>Sorting Priority (in order):</b>
    <br/>1. <b>Stock Availability:</b> Products with stock > 0 appear first
    <br/>2. <b>Display Rank:</b> Lower displayRank values appear first (1, 2, 3...)
    <br/>3. <b>Newness:</b> Most recently created products appear first
    
    <b>Implementation (TypeScript/JavaScript):</b>
    <br/>products.sort((a, b) => {
    <br/>  // Priority 1: Stock availability
    <br/>  if (a.stock > 0 && b.stock === 0) return -1;
    <br/>  if (a.stock === 0 && b.stock > 0) return 1;
    <br/>  
    <br/>  // Priority 2: Display rank (if set)
    <br/>  if (a.displayRank !== null && b.displayRank !== null) {
    <br/>    return a.displayRank - b.displayRank;
    <br/>  }
    <br/>  if (a.displayRank !== null) return -1;
    <br/>  if (b.displayRank !== null) return 1;
    <br/>  
    <br/>  // Priority 3: Newness
    <br/>  return new Date(b.createdAt) - new Date(a.createdAt);
    <br/>});
    
    <b>Database Query (Prisma):</b>
    <br/>const products = await prisma.product.findMany({
    <br/>  where: { 
    <br/>    isActive: true,
    <br/>    stock: { gt: 0 }  // Optional: filter out-of-stock
    <br/>  },
    <br/>  include: { variants: true },
    <br/>  orderBy: [
    <br/>    { stock: 'desc' },      // In-stock first
    <br/>    { displayRank: 'asc' }, // Lower rank first
    <br/>    { createdAt: 'desc' }   // Newest first
    <br/>  ],
    <br/>  take: limit,
    <br/>  skip: (page - 1) * limit
    <br/>});
    
    <b>Example Result:</b>
    <br/>1. Product A: stock=50, displayRank=1, createdAt=2024-01-15
    <br/>2. Product B: stock=30, displayRank=2, createdAt=2024-01-10
    <br/>3. Product C: stock=20, displayRank=null, createdAt=2024-01-20
    <br/>4. Product D: stock=0, displayRank=1, createdAt=2024-01-05 (out of stock, appears last)
    """
    story.append(Paragraph(ordering_logic, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 10. Discount Logic
    story.append(Paragraph("10. Discount Logic", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    discount_text = """
    Discounts are applied hierarchically with clear precedence rules to ensure predictable pricing:
    """
    story.append(Paragraph(discount_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    discount_logic = """
    <b>Discount Hierarchy:</b>
    <br/>1. <b>Variant-level discount</b> (highest priority) - Overrides product-level
    <br/>2. <b>Product-level discount</b> - Applied if no variant discount exists
    <br/>3. <b>No discount</b> - Full price if no discounts set
    
    <b>Rules:</b>
    <br/>• Only one discount can be active at a time
    <br/>• Discounts are stored as percentages (e.g., 10.0 = 10%)
    <br/>• Final price calculation: price * (1 - discount/100)
    <br/>• Discounts are applied at cart calculation time
    <br/>• Order items store the discounted price for historical accuracy
    
    <b>Price Calculation Implementation:</b>
    <br/>function calculatePrice(product, variant = null) {
    <br/>  let basePrice = product.basePrice;
    <br/>  let discount = null;
    <br/>  
    <br/>  if (variant) {
    <br/>    // Use variant price if set, otherwise use product base price
    <br/>    basePrice = variant.price || product.basePrice;
    <br/>    // Variant discount takes priority
    <br/>    discount = variant.discount || product.discount || null;
    <br/>  } else {
    <br/>    discount = product.discount || null;
    <br/>  }
    <br/>  
    <br/>  if (discount && discount > 0) {
    <br/>    return basePrice * (1 - discount / 100);
    <br/>  }
    <br/>  return basePrice;
    <br/>}
    
    <b>Example Scenarios:</b>
    <br/>Scenario 1: Product base price = ₹1,299, no discounts
    <br/>  → Final price: ₹1,299
    
    <br/>Scenario 2: Product base price = ₹1,299, product discount = 15%
    <br/>  → Final price: ₹1,299 * 0.85 = ₹1,104.15
    
    <br/>Scenario 3: Variant "Rose Gold" price = ₹1,399, variant discount = 10%
    <br/>  → Final price: ₹1,399 * 0.90 = ₹1,259.10
    
    <br/>Scenario 4: Product discount = 15%, Variant discount = 10% (variant wins)
    <br/>  → Final price: Uses variant discount (10%)
    """
    story.append(Paragraph(discount_logic, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 11. Payment Integration
    story.append(Paragraph("11. Payment Integration (Razorpay)", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_text = """
    Razorpay integration handles payment processing with webhook support for payment status updates. 
    The integration follows Razorpay's best practices for security and reliability.
    """
    story.append(Paragraph(payment_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_flow = """
    <b>Payment Flow Steps:</b>
    <br/>1. User initiates checkout: POST /api/orders
    <br/>2. Backend creates order with status PENDING
    <br/>3. Backend creates Razorpay order: POST /api/payments/create
    <br/>4. Razorpay returns order_id and key
    <br/>5. Frontend redirects to Razorpay payment page
    <br/>6. User completes payment on Razorpay
    <br/>7. Razorpay webhook: POST /api/payments/webhook
    <br/>8. Backend verifies payment signature
    <br/>9. Backend updates order status to CONFIRMED
    <br/>10. Backend updates payment record with razorpayId and status
    
    <b>Webhook Security:</b>
    <br/>• Verify Razorpay signature using secret key
    <br/>• Validate order amount matches
    <br/>• Idempotent processing (check if already processed)
    <br/>• Return 200 OK immediately, process asynchronously
    
    <b>Example Payment Service Code:</b>
    <br/>@Injectable()
    <br/>export class PaymentService {
    <br/>  async createRazorpayOrder(orderId: string, amount: number) {
    <br/>    const razorpayOrder = await this.razorpay.orders.create({
    <br/>      amount: amount * 100, // Convert to paise
    <br/>      currency: 'INR',
    <br/>      receipt: orderId,
    <br/>    });
    <br/>    
    <br/>    await this.prisma.payment.update({
    <br/>      where: { orderId },
    <br/>      data: { razorpayId: razorpayOrder.id }
    <br/>    });
    <br/>    
    <br/>    return {
    <br/>      orderId: razorpayOrder.id,
    <br/>      key: process.env.RAZORPAY_KEY_ID,
    <br/>      amount: razorpayOrder.amount
    <br/>    };
    <br/>  }
    <br/>  
    <br/>  async verifyWebhook(signature: string, orderId: string, paymentId: string) {
    <br/>    const payload = orderId + '|' + paymentId;
    <br/>    const expectedSignature = crypto
    <br/>      .createHmac('sha256', process.env.RAZORPAY_SECRET)
    <br/>      .update(payload)
    <br/>      .digest('hex');
    <br/>    
    <br/>    return signature === expectedSignature;
    <br/>  }
    <br/>}
    """
    story.append(Paragraph(payment_flow, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 12. Payment Flow Diagram
    story.append(Paragraph("12. Payment Flow Diagram", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_diag_text = """
    The following sequence diagram illustrates the complete payment flow from checkout initiation 
    to payment confirmation:
    """
    story.append(Paragraph(payment_diag_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_diagram = draw_payment_flow_diagram()
    story.append(payment_diagram)
    story.append(PageBreak())
    
    # 13. AI Recommendation Readiness
    story.append(Paragraph("13. AI Recommendation Readiness", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    ai_text = """
    The architecture is designed to accommodate future AI integration for image-based jewellery 
    recommendations. The system will accept dress images and suggest matching jewellery pieces 
    based on color, style, and occasion analysis.
    """
    story.append(Paragraph(ai_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    ai_design = """
    <b>Planned AI Module Architecture:</b>
    <br/>1. <b>Image Upload Endpoint:</b> POST /api/ai/recommend
    <br/>   • Accepts image file (dress photo)
    <br/>   • Validates image format (JPEG, PNG) and size (< 10MB)
    <br/>   • Stores temporarily or sends directly to AI service
    
    <b>AI Service Integration:</b>
    <br/>• Separate microservice (Python/ML framework like TensorFlow/PyTorch)
    <br/>• Receives image, analyzes:
    <br/>  - Color palette extraction
    <br/>  - Style classification (casual, formal, party, traditional)
    <br/>  - Occasion detection (wedding, office, party, etc.)
    <br/>• Returns recommended product IDs with confidence scores (0-1)
    <br/>• Backend queries catalog for recommended products
    <br/>• Returns enriched product data to frontend
    
    <b>Database Considerations:</b>
    <br/>• Add aiRecommendations table to track recommendations
    <br/>• Store image metadata, analysis results, user preferences
    <br/>• Track recommendation performance for ML model improvement
    <br/>• A/B testing support for different recommendation algorithms
    
    <b>Future Schema Addition:</b>
    <br/>model AIRecommendation {
    <br/>  id          String   @id @default(cuid())
    <br/>  userId      String?
    <br/>  sessionId   String   // For guest users
    <br/>  imageUrl    String
    <br/>  imageHash   String   // For duplicate detection
    <br/>  analysis    Json     // Store ML model output
    <br/>  productIds  String[] // Array of recommended product IDs
    <br/>  scores      Float[]  // Confidence scores for each product
    <br/>  createdAt   DateTime @default(now())
    <br/>  
    <br/>  @@index([userId])
    <br/>  @@index([sessionId])
    <br/>  @@map("ai_recommendations")
    <br/>}
    
    <b>Example API Response:</b>
    <br/>POST /api/ai/recommend
    <br/>Request: FormData with image file
    <br/>Response:
    <br/>{
    <br/>  "recommendations": [
    <br/>    {
    <br/>      "productId": "prod_123",
    <br/>      "confidence": 0.92,
    <br/>      "reason": "Color match: Gold matches dress accents"
    <br/>    },
    <br/>    {
    <br/>      "productId": "prod_456",
    <br/>      "confidence": 0.87,
    <br/>      "reason": "Style match: Elegant matches formal occasion"
    <br/>    }
    <br/>  ],
    <br/>  "analysis": {
    <br/>    "primaryColors": ["#FFD700", "#FFFFFF"],
    <br/>    "style": "formal",
    <br/>    "occasion": "wedding"
    <br/>  }
    <br/>}
    """
    story.append(Paragraph(ai_design, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 14. Future Extensions
    story.append(Paragraph("14. Future Extensions", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    extensions = """
    <b>Scalability Enhancements:</b>
    <br/>• <b>Redis Caching:</b> Cache product listings, user sessions, frequently accessed data
    <br/>• <b>Elasticsearch:</b> Advanced full-text search with filters (price range, category, tags)
    <br/>• <b>Microservices:</b> Split into independent services (catalog, order, payment, notification)
    <br/>• <b>CDN Integration:</b> CloudFront/Cloudflare for image delivery and static assets
    <br/>• <b>Queue System:</b> Bull/Redis for async order processing, email sending, inventory updates
    <br/>• <b>Database Replication:</b> Read replicas for scaling read operations
    <br/>• <b>Load Balancing:</b> Distribute traffic across multiple backend instances
    
    <b>Feature Extensions:</b>
    <br/>• <b>User Reviews & Ratings:</b> Product reviews, ratings, photos from customers
    <br/>• <b>Wishlist:</b> Save favorite products for later
    <br/>• <b>Order Tracking:</b> Real-time shipment tracking with carrier integration
    <br/>• <b>Notifications:</b> Email/SMS for order updates, promotions, stock alerts
    <br/>• <b>Admin Dashboard:</b> Comprehensive admin panel for inventory, orders, analytics
    <br/>• <b>Analytics & Reporting:</b> Sales reports, product performance, user behavior
    <br/>• <b>Multi-language:</b> Internationalization (i18n) support
    <br/>• <b>Multi-currency:</b> Support multiple currencies with automatic conversion
    <br/>• <b>Loyalty Program:</b> Points, rewards, referral system
    <br/>• <b>Subscription:</b> Recurring orders for regular customers
    
    <b>AI/ML Enhancements:</b>
    <br/>• <b>Personalized Recommendations:</b> User behavior-based product suggestions
    <br/>• <b>Image Search:</b> Upload image to find similar products
    <br/>• <b>Chatbot:</b> AI-powered customer support chatbot
    <br/>• <b>Price Optimization:</b> Dynamic pricing based on demand, inventory, competition
    <br/>• <b>Fraud Detection:</b> ML models to detect fraudulent transactions
    <br/>• <b>Inventory Forecasting:</b> Predict demand and optimize stock levels
    <br/>• <b>Search Ranking:</b> ML-powered search result ranking
    """
    story.append(Paragraph(extensions, styles['Normal']))
    story.append(PageBreak())
    
    # 15. Example Scenarios
    story.append(Paragraph("15. Example Scenarios", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario1 = """
    <b>Scenario 1: User Browsing Products</b>
    <br/>1. User visits homepage: GET /api/catalog/products?page=1&limit=20
    <br/>2. Backend queries database:
    <br/>   SELECT * FROM products 
    <br/>   WHERE isActive = true AND stock > 0
    <br/>   ORDER BY stock DESC, displayRank ASC, createdAt DESC
    <br/>   LIMIT 20 OFFSET 0
    <br/>3. For each product, fetch from Sanity CMS:
    <br/>   GET /v1/data/query?query=*[_id=="sanity_prod_123"]
    <br/>4. Merge database data (price, stock, variants) with Sanity content (images, description, badge)
    <br/>5. Return 20 products with pagination metadata
    <br/>6. Frontend displays product cards with images, prices, badges, "Add to Cart" buttons
    """
    story.append(Paragraph(scenario1, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario2 = """
    <b>Scenario 2: Adding to Cart with Discount</b>
    <br/>1. User selects product "Gold Necklace" with variant "Rose Gold"
    <br/>2. Backend calculates price:
    <br/>   • Base product price: ₹1,299
    <br/>   • Variant "Rose Gold" price: ₹1,399 (overrides base)
    <br/>   • Variant discount: 10%
    <br/>   • Final price: ₹1,399 * 0.90 = ₹1,259.10
    <br/>3. User adds to cart: POST /api/cart
    <br/>   { "productId": "prod_123", "variantId": "var_2", "quantity": 2 }
    <br/>4. Backend creates/updates cart item:
    <br/>   INSERT INTO cart_items (userId, productId, variantId, quantity)
    <br/>   VALUES ('user_123', 'prod_123', 'var_2', 2)
    <br/>5. Cart total: ₹2,518.20 (2 × ₹1,259.10)
    <br/>6. Frontend displays:
    <br/>   - Original price: ₹2,798 (2 × ₹1,399)
    <br/>   - Discount: 10% (-₹279.80)
    <br/>   - Final price: ₹2,518.20
    """
    story.append(Paragraph(scenario2, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario3 = """
    <b>Scenario 3: Complete Order Placement & Payment</b>
    <br/>1. User proceeds to checkout: POST /api/orders
    <br/>   {
    <br/>     "cartItems": [...],
    <br/>     "shippingInfo": { "name": "...", "address": "...", ... }
    <br/>   }
    <br/>2. Backend creates order:
    <br/>   - Calculates subtotal: ₹2,518.20
    <br/>   - Adds shipping: ₹50.00
    <br/>   - Total: ₹2,568.20
    <br/>   - Status: PENDING
    <br/>   - INSERT INTO orders (userId, totalAmount, status, ...)
    <br/>3. Backend creates Razorpay order:
    <br/>   POST https://api.razorpay.com/v1/orders
    <br/>   { "amount": 256820, "currency": "INR", "receipt": "order_xyz" }
    <br/>4. Razorpay returns: { "id": "order_rzp_123", "status": "created" }
    <br/>5. Backend stores razorpayId: UPDATE payments SET razorpayId = 'order_rzp_123'
    <br/>6. Frontend receives: { "razorpayOrderId": "order_rzp_123", "key": "rzp_test_..." }
    <br/>7. Frontend redirects to Razorpay payment page
    <br/>8. User pays ₹2,568.20 via UPI/Card/Net Banking
    <br/>9. Razorpay webhook: POST /api/payments/webhook
    <br/>   {
    <br/>     "razorpay_order_id": "order_rzp_123",
    <br/>     "razorpay_payment_id": "pay_xyz",
    <br/>     "razorpay_signature": "..."
    <br/>   }
    <br/>10. Backend verifies signature, updates:
    <br/>    - Order status: PENDING → CONFIRMED
    <br/>    - Payment status: PENDING → SUCCESS
    <br/>    - Payment razorpayId: 'pay_xyz'
    <br/>    - Reduce inventory for ordered items
    <br/>11. User receives order confirmation email
    <br/>12. Frontend shows success page with order details
    """
    story.append(Paragraph(scenario3, styles['Normal']))
    story.append(PageBreak())
    
    # 16. Conclusion
    story.append(Paragraph("16. Conclusion", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    conclusion = """
    This architecture provides a solid foundation for an artificial jewellery e-commerce platform 
    with the following key strengths:
    
    <b>Scalability:</b> Modular NestJS backend allows independent scaling of components. Database 
    indexing and caching strategies support high traffic. The architecture can easily scale horizontally.
    
    <b>Maintainability:</b> Clear separation of concerns, type-safe Prisma ORM, and well-organized 
    modules make the codebase maintainable. Sanity CMS enables non-technical staff to manage content.
    
    <b>Flexibility:</b> Sanity CMS enables content updates without code deployment. Discount and 
    ordering logic can be easily modified. The system supports various product variants and pricing strategies.
    
    <b>Future-Ready:</b> Architecture accommodates AI integration, additional payment gateways, 
    and feature extensions without major refactoring. The modular design allows incremental enhancements.
    
    <b>Security:</b> Payment webhook verification, user authentication, input validation, and secure 
    API design ensure the platform is secure and reliable.
    
    <b>Performance:</b> Database indexing, efficient queries, content CDN, and caching strategies 
    ensure fast response times and good user experience.
    
    <b>Next Steps for Implementation:</b>
    <br/>1. Set up development environment (NestJS, Next.js, PostgreSQL, Sanity)
    <br/>2. Implement core modules (Catalog, Cart, Order, Payment, User)
    <br/>3. Create Sanity CMS schemas and initial content
    <br/>4. Set up Razorpay integration with webhook handling
    <br/>5. Build frontend components (product listing, cart, checkout, order tracking)
    <br/>6. Implement authentication and authorization
    <br/>7. Add error handling, logging, and monitoring
    <br/>8. Write unit and integration tests
    <br/>9. Set up CI/CD pipeline
    <br/>10. Deploy to staging and production environments
    <br/>11. Future: Integrate AI recommendation module
    <br/>12. Future: Add analytics and reporting dashboard
    
    <b>Document Version:</b> 2.0 - Enhanced Edition
    <br/><b>Last Updated:</b> December 2024
    """
    story.append(Paragraph(conclusion, styles['Normal']))
    
    # Build PDF
    doc.build(story, onFirstPage=create_cover_page, onLaterPages=lambda c, d: None)
    
    print(f"Enhanced PDF report generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    try:
        generate_pdf_report()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()

