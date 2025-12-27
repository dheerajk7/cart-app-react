#!/usr/bin/env python3
"""
Generate comprehensive PDF report for Artificial Jewellery E-Commerce Architecture
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.graphics.shapes import Drawing, Rect, Line, String
from reportlab.graphics import renderPDF
from datetime import datetime
import os

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
    
    # Date
    canvas_obj.setFont("Helvetica", 12)
    date_text = f"Generated: {datetime.now().strftime('%B %d, %Y')}"
    date_width = canvas_obj.stringWidth(date_text, "Helvetica", 12)
    canvas_obj.drawString((letter[0] - date_width) / 2, letter[1] - 500, date_text)
    
    # Version
    canvas_obj.setFont("Helvetica", 10)
    version_text = "Version 1.0"
    version_width = canvas_obj.stringWidth(version_text, "Helvetica", 10)
    canvas_obj.drawString((letter[0] - version_width) / 2, letter[1] - 520, version_text)
    
    canvas_obj.restoreState()

def draw_architecture_diagram(canvas_obj, x, y, width, height):
    """Draw high-level architecture diagram"""
    # Define component positions
    components = {
        'Frontend (Next.js)': (width/2, height - 50),
        'Backend (NestJS)': (width/2, height - 150),
        'Sanity CMS': (width/4, height - 250),
        'PostgreSQL': (width/2, height - 250),
        'Razorpay': (3*width/4, height - 250),
        'AI Module (Future)': (width/2, height - 350)
    }
    
    # Draw boxes for components
    box_width, box_height = 100, 40
    for comp_name, (cx, cy) in components.items():
        canvas_obj.setStrokeColor(colors.HexColor('#34495E'))
        canvas_obj.setFillColor(colors.HexColor('#ECF0F1'))
        canvas_obj.rect(cx - box_width/2, cy - box_height/2, box_width, box_height, fill=1, stroke=1)
        
        # Component label
        canvas_obj.setFillColor(colors.black)
        canvas_obj.setFont("Helvetica", 8)
        words = comp_name.split()
        if len(words) > 1:
            canvas_obj.drawCentredString(cx, cy - 5, words[0])
            canvas_obj.drawCentredString(cx, cy - 15, ' '.join(words[1:]))
        else:
            canvas_obj.drawCentredString(cx, cy - 10, comp_name)
    
    # Draw arrows (connections)
    canvas_obj.setStrokeColor(colors.HexColor('#3498DB'))
    canvas_obj.setLineWidth(2)
    # Frontend to Backend
    canvas_obj.line(components['Frontend (Next.js)'][0], 
                   components['Frontend (Next.js)'][1] - 20,
                   components['Backend (NestJS)'][0],
                   components['Backend (NestJS)'][1] + 20)
    # Backend to Sanity
    canvas_obj.line(components['Backend (NestJS)'][0] - 30,
                   components['Backend (NestJS)'][1] - 20,
                   components['Sanity CMS'][0],
                   components['Sanity CMS'][1] + 20)
    # Backend to PostgreSQL
    canvas_obj.line(components['Backend (NestJS)'][0],
                   components['Backend (NestJS)'][1] - 20,
                   components['PostgreSQL'][0],
                   components['PostgreSQL'][1] + 20)
    # Backend to Razorpay
    canvas_obj.line(components['Backend (NestJS)'][0] + 30,
                   components['Backend (NestJS)'][1] - 20,
                   components['Razorpay'][0],
                   components['Razorpay'][1] + 20)
    # Backend to AI Module
    canvas_obj.line(components['Backend (NestJS)'][0],
                   components['Backend (NestJS)'][1] - 20,
                   components['AI Module (Future)'][0],
                   components['AI Module (Future)'][1] + 20)

def create_table_of_contents(story, styles):
    """Create table of contents"""
    story.append(Paragraph("Table of Contents", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        ("1. Introduction", 3),
        ("2. Tech Stack", 4),
        ("3. High-Level Architecture", 5),
        ("4. NestJS Backend Modules", 6),
        ("5. Sanity CMS Content Schema", 7),
        ("6. Database Schema (Prisma)", 8),
        ("7. Product Flow & API Endpoints", 9),
        ("8. Ordering Logic", 10),
        ("9. Discount Logic", 11),
        ("10. Payment Integration (Razorpay)", 12),
        ("11. AI Recommendation Readiness", 13),
        ("12. Future Extensions", 14),
        ("13. Example Scenarios", 15),
        ("14. Conclusion", 16)
    ]
    
    for item, page_num in toc_items:
        story.append(Paragraph(f"{item} ........................... {page_num}", styles['Normal']))
        story.append(Spacer(1, 0.1*inch))

def generate_pdf_report():
    """Generate the complete PDF report"""
    filename = "Artificial_Jewellery_ECommerce_Architecture.pdf"
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
        backColor=HexColor('#F5F5F5')
    ))
    
    # Cover page (handled separately)
    doc.build(story, onFirstPage=create_cover_page, onLaterPages=lambda c, d: None)
    
    # Rebuild with content
    story = []
    story.append(PageBreak())
    
    # Table of Contents
    create_table_of_contents(story, styles)
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
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HexColor('#F8F9FA')])
    ]))
    story.append(tech_table)
    story.append(PageBreak())
    
    # 3. High-Level Architecture
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
    
    # Architecture diagram description
    story.append(Paragraph("3.2 Architecture Diagram", styles['SectionHeading']))
    arch_diag_text = """
    The following diagram illustrates the high-level system architecture:
    
    [Frontend (Next.js)] 
         ↓ HTTP/REST
    [Backend (NestJS)]
         ↓       ↓        ↓
    [Sanity CMS] [PostgreSQL] [Razorpay]
         ↓
    [AI Module (Future)]
    
    <b>Key Interactions:</b>
    • Frontend communicates with Backend via REST API
    • Backend fetches product content from Sanity CMS
    • Backend stores transactional data in PostgreSQL
    • Backend processes payments through Razorpay
    • Backend will integrate with AI module for recommendations (future)
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
          required: true
        },
        {
          name: 'description',
          title: 'Description',
          type: 'text',
          required: true
        },
        {
          name: 'images',
          title: 'Product Images',
          type: 'array',
          of: [{ type: 'image' }]
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
          of: [{ type: 'string' }]
        },
        {
          name: 'badge',
          title: 'Badge (e.g., "New", "Sale")',
          type: 'string'
        },
        {
          name: 'displayRank',
          title: 'Display Rank (lower = higher priority)',
          type: 'number'
        }
      ]
    }
    """
    story.append(Paragraph("5.1 Product Schema", styles['SectionHeading']))
    story.append(Paragraph(sanity_schema, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 6. Database Schema (Prisma)
    story.append(Paragraph("6. Database Schema (Prisma)", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    prisma_schema = """
    // prisma/schema.prisma
    
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
    }
    
    model Variant {
      id          String   @id @default(cuid())
      productId   String
      name        String   // e.g., "Gold", "Silver"
      price       Decimal  @db.Decimal(10, 2)  // Overrides product.basePrice if set
      stock       Int      @default(0)
      sku         String   @unique
      discount    Decimal? @db.Decimal(5, 2)   // Percentage discount (variant-level)
      isActive    Boolean  @default(true)
      
      product     Product  @relation(fields: [productId], references: [id])
      
      @@index([productId])
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
    }
    
    model CartItem {
      id        String   @id @default(cuid())
      userId    String
      productId String
      variantId String?
      quantity  Int      @default(1)
      createdAt DateTime @default(now())
      
      user      User     @relation(fields: [userId], references: [id])
      product   Product  @relation(fields: [productId], references: [id])
      
      @@unique([userId, productId, variantId])
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
    }
    
    model OrderItem {
      id            String   @id @default(cuid())
      orderId       String
      productId     String
      variantId     String?
      quantity      Int
      price         Decimal  @db.Decimal(10, 2)  // Price at time of order
      discount      Decimal  @db.Decimal(5, 2)   // Applied discount percentage
      
      order         Order    @relation(fields: [orderId], references: [id])
      product       Product  @relation(fields: [productId], references: [id])
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
    
    # 7. Product Flow & API
    story.append(Paragraph("7. Product Flow & API Endpoints", styles['Heading1']))
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
    
    # API Response Example
    story.append(Paragraph("7.1 API Response Example", styles['SectionHeading']))
    api_example = """
    // GET /api/catalog/products?page=1&limit=20&category=necklaces
    
    {
      "data": [
        {
          "id": "prod_123",
          "sanityId": "sanity_prod_123",
          "title": "Elegant Gold Necklace",
          "description": "Beautiful artificial gold necklace...",
          "images": [
            "https://cdn.sanity.io/images/...",
            "https://cdn.sanity.io/images/..."
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
          "tags": ["trending", "elegant"]
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
    
    # 8. Ordering Logic
    story.append(Paragraph("8. Ordering Logic", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    ordering_text = """
    Products are ordered using a multi-level sorting strategy to ensure the best user experience:
    """
    story.append(Paragraph(ordering_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    ordering_logic = """
    <b>Sorting Priority (in order):</b>
    <br/>1. <b>Stock Availability:</b> Products with stock > 0 appear first
    <br/>2. <b>Display Rank:</b> Lower displayRank values appear first (1, 2, 3...)
    <br/>3. <b>Newness:</b> Most recently created products appear first
    
    <b>Pseudocode:</b>
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
    <br/>  return b.createdAt - a.createdAt;
    <br/>});
    
    <b>Database Query (Prisma):</b>
    <br/>const products = await prisma.product.findMany({
    <br/>  where: { isActive: true },
    <br/>  orderBy: [
    <br/>    { stock: 'desc' },  // In-stock first
    <br/>    { displayRank: 'asc' },  // Lower rank first
    <br/>    { createdAt: 'desc' }  // Newest first
    <br/>  ],
    <br/>  take: limit,
    <br/>  skip: (page - 1) * limit
    <br/>});
    """
    story.append(Paragraph(ordering_logic, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 9. Discount Logic
    story.append(Paragraph("9. Discount Logic", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    discount_text = """
    Discounts are applied hierarchically with clear precedence rules:
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
    
    <b>Price Calculation Pseudocode:</b>
    <br/>function calculatePrice(product, variant = null) {
    <br/>  let basePrice = product.basePrice;
    <br/>  let discount = null;
    <br/>  
    <br/>  if (variant) {
    <br/>    basePrice = variant.price || product.basePrice;
    <br/>    discount = variant.discount || product.discount || null;
    <br/>  } else {
    <br/>    discount = product.discount || null;
    <br/>  }
    <br/>  
    <br/>  if (discount) {
    <br/>    return basePrice * (1 - discount / 100);
    <br/>  }
    <br/>  return basePrice;
    <br/>}
    
    <b>Example:</b>
    <br/>Product base price: ₹1,299
    <br/>Variant "Rose Gold" price: ₹1,399 (overrides base)
    <br/>Variant discount: 10%
    <br/>Final price: ₹1,399 * 0.9 = ₹1,259.10
    """
    story.append(Paragraph(discount_logic, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 10. Payment Integration
    story.append(Paragraph("10. Payment Integration (Razorpay)", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_text = """
    Razorpay integration handles payment processing with webhook support for payment status updates.
    """
    story.append(Paragraph(payment_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    payment_flow = """
    <b>Payment Flow:</b>
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
    """
    story.append(Paragraph(payment_flow, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 11. AI Recommendation Readiness
    story.append(Paragraph("11. AI Recommendation Readiness", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    ai_text = """
    The architecture is designed to accommodate future AI integration for image-based jewellery 
    recommendations. The system will accept dress images and suggest matching jewellery pieces.
    """
    story.append(Paragraph(ai_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    ai_design = """
    <b>Planned AI Module Architecture:</b>
    <br/>1. <b>Image Upload Endpoint:</b> POST /api/ai/recommend
    <br/>   • Accepts image file (dress photo)
    <br/>   • Validates image format and size
    <br/>   • Stores temporarily or sends to AI service
    
    <b>AI Service Integration:</b>
    <br/>• Separate microservice (Python/ML framework)
    <br/>• Receives image, analyzes color, style, occasion
    <br/>• Returns recommended product IDs with confidence scores
    <br/>• Backend queries catalog for recommended products
    <br/>• Returns enriched product data to frontend
    
    <b>Database Considerations:</b>
    <br/>• Add aiRecommendations table to track recommendations
    <br/>• Store image metadata, user preferences
    <br/>• Track recommendation performance for ML improvement
    
    <b>Future Schema Addition:</b>
    <br/>model AIRecommendation {
    <br/>  id          String   @id @default(cuid())
    <br/>  userId      String?
    <br/>  imageUrl    String
    <br/>  productIds  String[]  // Array of recommended product IDs
    <br/>  scores      Float[]   // Confidence scores
    <br/>  createdAt   DateTime  @default(now())
    <br/>}
    """
    story.append(Paragraph(ai_design, styles['CodeBlock']))
    story.append(PageBreak())
    
    # 12. Future Extensions
    story.append(Paragraph("12. Future Extensions", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    extensions = """
    <b>Scalability Enhancements:</b>
    <br/>• Implement Redis caching for product listings
    <br/>• Add Elasticsearch for advanced search capabilities
    <br/>• Microservices architecture for independent scaling
    <br/>• CDN integration for image delivery
    <br/>• Queue system (Bull/Redis) for async order processing
    
    <b>Feature Extensions:</b>
    <br/>• User reviews and ratings
    <br/>• Wishlist functionality
    <br/>• Order tracking with shipment updates
    <br/>• Email/SMS notifications
    <br/>• Admin dashboard for inventory management
    <br/>• Analytics and reporting
    <br/>• Multi-language support
    <br/>• Multi-currency support
    
    <b>AI/ML Enhancements:</b>
    <br/>• Personalized product recommendations
    <br/>• Image-based search (find similar products)
    <br/>• Chatbot for customer support
    <br/>• Price optimization using ML
    <br/>• Fraud detection
    """
    story.append(Paragraph(extensions, styles['Normal']))
    story.append(PageBreak())
    
    # 13. Example Scenarios
    story.append(Paragraph("13. Example Scenarios", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario1 = """
    <b>Scenario 1: User Browsing Products</b>
    <br/>1. User visits homepage: GET /api/catalog/products?page=1
    <br/>2. Backend queries: SELECT * FROM products WHERE isActive = true AND stock > 0
    <br/>3. For each product, fetch from Sanity: GET /v1/data/query?query=*[_id=="sanity_prod_123"]
    <br/>4. Merge data and sort: in-stock → displayRank → createdAt
    <br/>5. Return 20 products per page
    <br/>6. Frontend displays product cards with images, prices, badges
    """
    story.append(Paragraph(scenario1, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario2 = """
    <b>Scenario 2: Adding to Cart with Discount</b>
    <br/>1. User selects product "Gold Necklace" with variant "Rose Gold"
    <br/>2. Backend calculates price:
    <br/>   • Base price: ₹1,399 (variant override)
    <br/>   • Discount: 10% (variant-level)
    <br/>   • Final price: ₹1,259.10
    <br/>3. User adds to cart: POST /api/cart { productId, variantId, quantity: 2 }
    <br/>4. Cart total: ₹2,518.20
    <br/>5. Cart displays original price (₹2,798), discount (10%), final price (₹2,518.20)
    """
    story.append(Paragraph(scenario2, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    scenario3 = """
    <b>Scenario 3: Order Placement & Payment</b>
    <br/>1. User proceeds to checkout: POST /api/orders { cartItems, shippingInfo }
    <br/>2. Backend creates order: status = PENDING, totalAmount = ₹2,518.20
    <br/>3. Backend creates Razorpay order: amount = ₹2,518.20
    <br/>4. Razorpay returns: { order_id: "order_xyz", key: "rzp_test_..." }
    <br/>5. Frontend redirects to Razorpay payment page
    <br/>6. User pays ₹2,518.20
    <br/>7. Razorpay webhook: { razorpay_order_id, razorpay_payment_id, signature }
    <br/>8. Backend verifies signature, updates order: status = CONFIRMED
    <br/>9. Backend updates payment: status = SUCCESS, razorpayId = "pay_xyz"
    <br/>10. User receives order confirmation
    """
    story.append(Paragraph(scenario3, styles['Normal']))
    story.append(PageBreak())
    
    # 14. Conclusion
    story.append(Paragraph("14. Conclusion", styles['Heading1']))
    story.append(Spacer(1, 0.2*inch))
    
    conclusion = """
    This architecture provides a solid foundation for an artificial jewellery e-commerce platform 
    with the following key strengths:
    
    <b>Scalability:</b> Modular NestJS backend allows independent scaling of components. Database 
    indexing and caching strategies support high traffic.
    
    <b>Maintainability:</b> Clear separation of concerns, type-safe Prisma ORM, and well-organized 
    modules make the codebase maintainable.
    
    <b>Flexibility:</b> Sanity CMS enables content updates without code deployment. Discount and 
    ordering logic can be easily modified.
    
    <b>Future-Ready:</b> Architecture accommodates AI integration, additional payment gateways, 
    and feature extensions without major refactoring.
    
    <b>Next Steps:</b>
    <br/>1. Set up development environment (NestJS, Next.js, PostgreSQL, Sanity)
    <br/>2. Implement core modules (Catalog, Cart, Order, Payment)
    <br/>3. Create Sanity CMS schemas and content
    <br/>4. Set up Razorpay integration
    <br/>5. Build frontend components
    <br/>6. Testing and deployment
    <br/>7. Future: Integrate AI recommendation module
    """
    story.append(Paragraph(conclusion, styles['Normal']))
    
    # Build PDF
    doc.build(story, onFirstPage=create_cover_page, onLaterPages=lambda c, d: None)
    
    print(f"PDF report generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    try:
        generate_pdf_report()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()


