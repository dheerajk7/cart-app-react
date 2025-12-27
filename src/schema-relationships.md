# Database & CMS Schema Relationships Documentation

## Artificial Jewellery E-Commerce Platform

This document outlines the relationships between Prisma Database Schema and Sanity CMS Schema.

---

## 🔗 Core Linking Mechanism

### Primary Connection Point
- **Database Field**: `Product.sanityId` (String, Unique)
- **Sanity Field**: `product.sanityId` (String, Required)
- **Purpose**: Links transactional data (DB) with content data (CMS)

---

## 📊 Entity Relationship Diagram

### Database Schema Relationships

```
User
├── Address (1:N) - User can have multiple addresses
├── CartItem (1:N) - User can have multiple cart items
├── WishlistItem (1:N) - User can have multiple wishlist items
├── Order (1:N) - User can have multiple orders
├── Review (1:N) - User can write multiple reviews
└── AIRecommendation (1:N) - User can have multiple AI recommendations

Category
├── Category (Self-referential N:1) - Hierarchical categories
└── Product (1:N) - Category has many products

Product
├── Category (N:1) - Product belongs to one category
├── Variant (1:N) - Product has many variants
├── CartItem (1:N) - Product can be in multiple carts
├── OrderItem (1:N) - Product can be in multiple orders
├── WishlistItem (1:N) - Product can be in multiple wishlists
└── Review (1:N) - Product can have multiple reviews

Variant
├── Product (N:1) - Variant belongs to one product
├── CartItem (1:N) - Variant can be in multiple carts
└── OrderItem (1:N) - Variant can be in multiple orders

Order
├── User (N:1) - Order belongs to one user
├── Address (N:1) - Order uses one shipping address
├── OrderItem (1:N) - Order has many items
├── Payment (1:1) - Order has one payment
└── ShippingInfo (1:1) - Order has one shipping info

Payment
└── Order (1:1) - Payment belongs to one order

ShippingInfo
├── Order (1:1) - Shipping info belongs to one order
└── Address (N:1) - Shipping info can reference an address
```

### Sanity CMS Schema Relationships

```
Product (Sanity)
├── Category (Reference) - Product references a category
├── Related Products (Self-reference) - Product can reference other products
└── Images (Array) - Product has multiple images

Category (Sanity)
└── Parent Category (Self-reference) - Hierarchical categories

Collection
└── Products (Array of References) - Collection contains multiple products

Blog Post
├── Author (Reference) - Blog post has one author
├── Categories (Array of References) - Blog post can have multiple categories
└── Related Products (Array of References) - Blog post can reference products
```

---

## 🔄 Data Flow & Synchronization

### Product Creation Flow

1. **Content Creation (Sanity CMS)**
   - Content team creates product in Sanity
   - Fills in: title, description, images, category, attributes, etc.
   - Sanity auto-generates `sanityId` (document `_id`)

2. **Product Sync (Backend)**
   - Backend creates product record in PostgreSQL
   - Sets `Product.sanityId` = Sanity document `_id`
   - Sets transactional fields: `basePrice`, `stock`, `sku`, `status`

3. **Variant Creation (Backend)**
   - Backend creates variant records linked to product
   - Variants inherit product attributes from Sanity

### Product Retrieval Flow

1. **API Request**: `GET /api/products/:id`
2. **Backend Query**:
   - Fetches product from PostgreSQL by `id`
   - Uses `Product.sanityId` to fetch content from Sanity
   - Merges transactional data (DB) with content data (CMS)
3. **Response**: Combined product object with all fields

---

## 📋 Field Mapping Reference

### Product Fields

| Database (Prisma) | Sanity CMS | Notes |
|------------------|------------|-------|
| `id` | - | Database primary key |
| `sanityId` | `_id` | **Linking field** |
| `name` | `title` | Product name/title |
| `sku` | - | Stock keeping unit (DB only) |
| `slug` | `slug.current` | URL-friendly identifier |
| `basePrice` | - | Base price (DB only) |
| `stock` | - | Inventory count (DB only) |
| `status` | - | Product status (DB only) |
| `categoryId` | `category` | Category reference |
| `displayRank` | `displayRank` | Display priority |
| - | `description` | Full description (CMS only) |
| - | `images` | Product images array (CMS only) |
| - | `attributes` | Product attributes object (CMS only) |
| - | `badge` | Display badge (CMS only) |
| - | `tags` | Searchable tags (CMS only) |
| - | `seo` | SEO metadata (CMS only) |

### Variant Fields

| Database (Prisma) | Sanity CMS | Notes |
|------------------|------------|-------|
| `id` | - | Database primary key |
| `productId` | - | Links to product |
| `name` | `attributes.color` | Variant name (e.g., "Gold") |
| `sku` | - | Variant SKU (DB only) |
| `price` | - | Variant-specific price (DB only) |
| `stock` | - | Variant inventory (DB only) |
| `attributes` | `attributes` | Variant attributes (JSON) |

---

## 🎯 Key Relationships Explained

### 1. Product ↔ Category

**Database:**
- `Product.categoryId` → `Category.id` (Foreign Key)
- One category can have many products
- One product belongs to one category

**Sanity:**
- `product.category` → `category` (Reference)
- Same relationship structure

**Sync Strategy:**
- Category must exist in both systems
- Category `slug` should match between DB and CMS

### 2. Product ↔ Variant

**Database:**
- `Variant.productId` → `Product.id` (Foreign Key)
- One product can have many variants
- Variant attributes stored in `Variant.attributes` (JSON)

**Sanity:**
- Variant data stored in `product.attributes.color` array
- Backend creates variant records based on Sanity attributes

**Example:**
```javascript
// Sanity product.attributes.color = ["Gold", "Silver", "Rose Gold"]
// Backend creates 3 Variant records:
// - Variant 1: name="Gold", productId=product.id
// - Variant 2: name="Silver", productId=product.id
// - Variant 3: name="Rose Gold", productId=product.id
```

### 3. Product ↔ User (Shopping)

**Cart:**
- `CartItem.userId` → `User.id`
- `CartItem.productId` → `Product.id`
- `CartItem.variantId` → `Variant.id` (optional)
- Unique constraint: `[userId, productId, variantId]`

**Wishlist:**
- `WishlistItem.userId` → `User.id`
- `WishlistItem.productId` → `Product.id`
- Unique constraint: `[userId, productId]`

**Orders:**
- `Order.userId` → `User.id`
- `OrderItem.orderId` → `Order.id`
- `OrderItem.productId` → `Product.id`
- `OrderItem.variantId` → `Variant.id` (optional)

### 4. Order ↔ Payment

**One-to-One Relationship:**
- `Payment.orderId` → `Order.id` (Unique)
- One order has exactly one payment
- Payment status tracks order payment state

### 5. Order ↔ Shipping

**One-to-One Relationship:**
- `ShippingInfo.orderId` → `Order.id` (Unique)
- One order has exactly one shipping info
- Can optionally reference `Address` for saved addresses

---

## 🔍 Query Patterns

### Get Complete Product with Content

```typescript
// 1. Fetch from database
const product = await prisma.product.findUnique({
  where: { id: productId },
  include: {
    category: true,
    variants: true
  }
})

// 2. Fetch from Sanity using sanityId
const sanityProduct = await sanityClient.fetch(
  `*[_id == $sanityId][0]`,
  { sanityId: product.sanityId }
)

// 3. Merge data
const completeProduct = {
  ...product,
  ...sanityProduct,
  // Combine images, descriptions, etc.
}
```

### Get Products by Category

```typescript
// Database query
const products = await prisma.product.findMany({
  where: {
    category: { slug: categorySlug },
    isActive: true,
    status: 'ACTIVE'
  },
  orderBy: [
    { stock: 'desc' },
    { displayRank: 'asc' },
    { createdAt: 'desc' }
  ]
})

// Fetch Sanity content for each
const productsWithContent = await Promise.all(
  products.map(async (product) => {
    const content = await sanityClient.fetch(
      `*[_id == $sanityId][0]`,
      { sanityId: product.sanityId }
    )
    return { ...product, ...content }
  })
)
```

---

## ⚠️ Important Constraints

### 1. Data Integrity
- `Product.sanityId` must always reference a valid Sanity document
- If Sanity document is deleted, handle gracefully (soft delete or archive)

### 2. Synchronization
- Product creation: Create in Sanity first, then sync to DB
- Product updates: Update both systems independently
- Product deletion: Soft delete in DB, hard delete in Sanity (or vice versa based on business logic)

### 3. Unique Constraints
- `Product.sku` must be unique across all products
- `Product.slug` must be unique (matches Sanity slug)
- `Variant.sku` must be unique across all variants
- `CartItem`: Unique `[userId, productId, variantId]`
- `WishlistItem`: Unique `[userId, productId]`

### 4. Referential Integrity
- Cannot delete `Category` if products reference it
- Cannot delete `Product` if orders reference it (use soft delete)
- Cannot delete `User` if orders exist (use soft delete)

---

## 🚀 Best Practices

1. **Always validate `sanityId` exists** before creating DB product
2. **Use transactions** when creating product + variants
3. **Cache Sanity content** to reduce API calls
4. **Index frequently queried fields**: `slug`, `sku`, `categoryId`, `status`
5. **Use soft deletes** for products with order history
6. **Maintain slug consistency** between DB and CMS
7. **Sync displayRank** from CMS to DB for consistent ordering

---

## 📝 Migration Checklist

When setting up the schemas:

- [ ] Create all Prisma models
- [ ] Run `prisma migrate dev` to create database tables
- [ ] Create all Sanity schemas
- [ ] Configure Sanity studio
- [ ] Set up sync mechanism (webhook or scheduled job)
- [ ] Create indexes on foreign keys and frequently queried fields
- [ ] Set up validation rules in both systems
- [ ] Test product creation flow (Sanity → DB)
- [ ] Test product retrieval flow (DB + Sanity merge)
- [ ] Test variant creation and linking
- [ ] Test category relationships

---

## 🔄 Future Enhancements

1. **Real-time Sync**: Webhook from Sanity to update DB on content changes
2. **Bulk Import**: Script to sync existing Sanity products to DB
3. **Audit Log**: Track all product changes in both systems
4. **Versioning**: Support product version history
5. **Multi-language**: Extend schemas for i18n support

