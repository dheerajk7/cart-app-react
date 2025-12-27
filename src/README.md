# Artificial Jewellery E-Commerce Platform
## Complete Database & CMS Schema Documentation

This repository contains the complete database schema (Prisma) and Sanity CMS schema for an Artificial Jewellery E-Commerce Platform, along with comprehensive documentation.

---

## 📁 Files in This Repository

### 1. **prisma-schema.prisma**
Complete Prisma database schema with all models, relationships, and constraints.

**Contains**:
- User management (User, Address)
- Product catalog (Product, Variant, Category)
- Shopping (CartItem, WishlistItem)
- Orders & Payments (Order, OrderItem, Payment, ShippingInfo)
- Reviews & Ratings
- Discounts & Coupons
- AI Recommendations
- Analytics & Tracking

**Usage**:
```bash
# Generate Prisma Client
npx prisma generate

# Run migrations
npx prisma migrate dev --name init

# Open Prisma Studio
npx prisma studio
```

---

### 2. **sanity-schemas.js**
Complete Sanity CMS schema with all content types.

**Contains**:
- Product schema (with images, attributes, SEO)
- Category schema (hierarchical)
- Collection schema
- Blog Post schema
- Author schema
- Blog Category schema
- Hero Section schema

**Usage**:
```javascript
// In sanity.config.js
import schemas from './schemas/sanity-schemas'

export default {
  // ... other config
  schema: {
    types: schemas
  }
}
```

---

### 3. **schema-relationships.md**
Comprehensive documentation of relationships between database and CMS schemas.

**Contains**:
- Entity relationship diagrams
- Field mapping reference
- Data flow and synchronization patterns
- Query examples
- Best practices and constraints
- Migration checklist

**Use this for**: Understanding how database and CMS connect, data synchronization strategies.

---

### 4. **field-documentation.md** ⭐ **NEW**
Complete field-by-field documentation explaining every field in both schemas.

**Contains**:
- Detailed explanation of every database field
- Detailed explanation of every Sanity CMS field
- Purpose and usage of each field
- Relationships and constraints
- Common use cases
- Best practices

**Use this for**: Understanding what each field does, when to use it, and how it fits into the system.

---

## 🚀 Quick Start Guide

### 1. Database Setup (Prisma)

```bash
# Install Prisma
npm install prisma @prisma/client

# Initialize Prisma (if not already done)
npx prisma init

# Copy prisma-schema.prisma to your prisma/ directory
cp prisma-schema.prisma prisma/schema.prisma

# Set DATABASE_URL in .env
DATABASE_URL="postgresql://user:password@localhost:5432/jewellery_db"

# Generate Prisma Client
npx prisma generate

# Run migrations
npx prisma migrate dev --name init

# Seed database (optional)
npx prisma db seed
```

### 2. Sanity CMS Setup

```bash
# Install Sanity CLI
npm install -g @sanity/cli

# Initialize Sanity project
sanity init

# Copy sanity-schemas.js to your schemas/ directory
cp sanity-schemas.js schemas/index.js

# Start Sanity Studio
sanity start
```

### 3. Linking Database & CMS

**Critical**: The `sanityId` field links database products to Sanity content.

**Product Creation Flow**:
1. Create product in Sanity CMS
2. Get Sanity document `_id`
3. Create product in database with `sanityId = _id`
4. Create variants in database based on Sanity attributes

**Product Retrieval Flow**:
1. Fetch product from database
2. Use `product.sanityId` to fetch content from Sanity
3. Merge transactional data (DB) with content data (CMS)
4. Return complete product object

---

## 📊 Schema Overview

### Database Models (15 total)

| Model | Purpose | Key Fields |
|-------|---------|------------|
| **User** | User accounts | email, password, role, addresses |
| **Address** | Shipping addresses | fullName, phone, addressLine1, city, state |
| **Category** | Product categories | name, slug, parentId (hierarchical) |
| **Product** | Products | name, sku, basePrice, stock, **sanityId** (links to CMS) |
| **Variant** | Product variants | name, price, stock, attributes |
| **CartItem** | Shopping cart | userId, productId, variantId, quantity |
| **WishlistItem** | Wishlist | userId, productId |
| **Order** | Orders | orderNumber, status, totalAmount |
| **OrderItem** | Order items | productName (snapshot), price (snapshot) |
| **Payment** | Payments | status, razorpayOrderId, razorpayPaymentId |
| **ShippingInfo** | Shipping details | trackingNumber, status, carrier |
| **Review** | Product reviews | rating, comment, isApproved |
| **Coupon** | Discount coupons | code, type, value, validFrom, validUntil |
| **AIRecommendation** | AI recommendations | imageUrl, productIds, scores |
| **ProductView** | Analytics | productId, userId, sessionId |
| **SearchQuery** | Search analytics | query, resultsCount |

### Sanity Content Types (7 total)

| Type | Purpose | Key Fields |
|------|---------|------------|
| **product** | Product content | title, images, description, attributes, **sanityId** |
| **category** | Category content | name, image, icon, parent |
| **collection** | Product collections | title, products (references) |
| **blogPost** | Blog posts | title, body, author, relatedProducts |
| **author** | Blog authors | name, image, bio |
| **blogCategory** | Blog categories | title, description |
| **heroSection** | Homepage banners | title, image, ctaButton |

---

## 🔗 Key Relationships

### Critical Linking Field
- **Database**: `Product.sanityId`
- **Sanity**: `product._id` (auto-generated)
- **Purpose**: Connects transactional data with content data

### Main Relationships

```
User
├── Address (1:N)
├── CartItem (1:N)
├── WishlistItem (1:N)
├── Order (1:N)
└── Review (1:N)

Category
├── Category (Self-referential, hierarchical)
└── Product (1:N)

Product
├── Category (N:1)
├── Variant (1:N)
├── CartItem (1:N)
├── OrderItem (1:N)
└── Review (1:N)

Order
├── User (N:1)
├── OrderItem (1:N)
├── Payment (1:1)
└── ShippingInfo (1:1)
```

---

## 📖 Documentation Guide

### For Developers
1. **Start with**: `schema-relationships.md` - Understand the overall architecture
2. **Then read**: `field-documentation.md` - Learn what each field does
3. **Reference**: `prisma-schema.prisma` and `sanity-schemas.js` - Implementation details

### For Content Managers
1. **Read**: `field-documentation.md` - Sanity CMS section
2. **Focus on**: Product schema fields, Category schema, Collection schema
3. **Understand**: How content in Sanity connects to products in database

### For Database Administrators
1. **Read**: `prisma-schema.prisma` - Complete database structure
2. **Review**: `field-documentation.md` - Database section
3. **Check**: `schema-relationships.md` - Constraints and relationships

---

## 🎯 Common Tasks

### Adding a New Product

1. **In Sanity CMS**:
   - Create new product document
   - Fill in: title, description, images, category, attributes
   - Note the document `_id` (this is the `sanityId`)

2. **In Database**:
   ```typescript
   const product = await prisma.product.create({
     data: {
       sanityId: sanityDocumentId, // From step 1
       name: "Product Name",
       sku: "SKU-001",
       slug: "product-name",
       basePrice: 1299.00,
       stock: 50,
       categoryId: categoryId,
       status: "ACTIVE"
     }
   })
   
   // Create variants based on Sanity attributes.color
   const variants = await Promise.all(
     colors.map(color => prisma.variant.create({
       data: {
         productId: product.id,
         name: color,
         sku: `SKU-001-${color}`,
         stock: 10
       }
     }))
   )
   ```

### Fetching Complete Product

```typescript
// 1. Fetch from database
const product = await prisma.product.findUnique({
  where: { id: productId },
  include: {
    category: true,
    variants: true
  }
})

// 2. Fetch from Sanity
const sanityProduct = await sanityClient.fetch(
  `*[_id == $sanityId][0]`,
  { sanityId: product.sanityId }
)

// 3. Merge data
const completeProduct = {
  ...product,
  ...sanityProduct,
  images: sanityProduct.images,
  description: sanityProduct.description
}
```

### Calculating Product Price

```typescript
function calculatePrice(product: Product, variant?: Variant): number {
  let basePrice = product.basePrice
  let discount = product.discount
  
  // Variant overrides product price
  if (variant) {
    basePrice = variant.price || product.basePrice
    discount = variant.discount || product.discount || null
  }
  
  // Apply discount
  if (discount) {
    return basePrice * (1 - discount / 100)
  }
  
  return basePrice
}
```

---

## ⚠️ Important Notes

### Data Synchronization
- **Product content** (images, descriptions) → Sanity CMS only
- **Transactional data** (prices, stock, orders) → Database only
- **Linking field**: `Product.sanityId` connects both systems

### Field Naming
- Database uses `camelCase`: `basePrice`, `displayRank`
- Sanity uses `camelCase`: `displayRank`, `isFeatured`
- Keep field names consistent between systems where applicable

### Required Fields
- **Database Product**: `sanityId`, `name`, `sku`, `slug`, `basePrice`, `categoryId`
- **Sanity Product**: `sanityId`, `title`, `slug`, `description`, `images`, `category`

### Unique Constraints
- `Product.sku` - Must be unique
- `Product.slug` - Must be unique (matches Sanity slug)
- `Product.sanityId` - Must be unique (links to Sanity)
- `Variant.sku` - Must be unique
- `User.email` - Must be unique
- `User.phone` - Must be unique (if provided)

---

## 🔄 Next Steps

1. **Set up development environment**
   - Install Prisma and Sanity
   - Configure database connection
   - Set up Sanity project

2. **Run migrations**
   - Create database tables
   - Generate Prisma Client

3. **Configure Sanity Studio**
   - Import schemas
   - Set up content structure

4. **Implement sync mechanism**
   - Webhook from Sanity to update database
   - Or scheduled job to sync products

5. **Test the system**
   - Create test product in Sanity
   - Sync to database
   - Fetch complete product
   - Test ordering flow

---

## 📚 Additional Resources

- [Prisma Documentation](https://www.prisma.io/docs)
- [Sanity CMS Documentation](https://www.sanity.io/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 📝 File Summary

| File | Lines | Purpose |
|------|-------|---------|
| `prisma-schema.prisma` | ~580 | Complete database schema |
| `sanity-schemas.js` | ~785 | Complete CMS schema |
| `schema-relationships.md` | ~345 | Relationship documentation |
| `field-documentation.md` | ~1,200+ | Field-by-field documentation |
| `README.md` | This file | Quick start guide |

---

## 🎉 You're All Set!

You now have:
- ✅ Complete database schema (Prisma)
- ✅ Complete CMS schema (Sanity)
- ✅ Comprehensive documentation
- ✅ Field-by-field explanations
- ✅ Relationship diagrams
- ✅ Usage examples

Start building your Artificial Jewellery E-Commerce Platform! 💍✨

