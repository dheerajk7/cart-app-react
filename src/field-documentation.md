# Complete Field Documentation
## Artificial Jewellery E-Commerce Platform

This document provides a comprehensive explanation of every field in both the Prisma Database Schema and Sanity CMS Schema, including what each field is used for and its purpose in the system.

---

## 📋 Table of Contents

1. [Database Schema (Prisma) Fields](#database-schema-prisma-fields)
   - [Enums](#enums)
   - [User Management](#user-management)
   - [Product Catalog](#product-catalog)
   - [Shopping Cart & Wishlist](#shopping-cart--wishlist)
   - [Orders & Payments](#orders--payments)
   - [Reviews & Ratings](#reviews--ratings)
   - [Discounts & Coupons](#discounts--coupons)
   - [AI Recommendations](#ai-recommendations)
   - [Analytics & Tracking](#analytics--tracking)

2. [Sanity CMS Schema Fields](#sanity-cms-schema-fields)
   - [Product Schema](#product-schema)
   - [Category Schema](#category-schema)
   - [Collection Schema](#collection-schema)
   - [Blog Post Schema](#blog-post-schema)
   - [Author Schema](#author-schema)
   - [Blog Category Schema](#blog-category-schema)
   - [Hero Section Schema](#hero-section-schema)

---

## Database Schema (Prisma) Fields

### Enums

#### OrderStatus
**Purpose**: Tracks the current state of an order in the fulfillment lifecycle.

- `PENDING`: Order created but not yet confirmed
- `CONFIRMED`: Payment received, order confirmed
- `PROCESSING`: Order being prepared for shipment
- `SHIPPED`: Order dispatched to customer
- `DELIVERED`: Order successfully delivered
- `CANCELLED`: Order cancelled before delivery
- `REFUNDED`: Order refunded to customer

**Usage**: Used in `Order.status` to track order progression and trigger appropriate actions (emails, notifications, etc.)

---

#### PaymentStatus
**Purpose**: Tracks payment transaction state.

- `PENDING`: Payment initiated but not completed
- `SUCCESS`: Payment successfully processed
- `FAILED`: Payment attempt failed
- `REFUNDED`: Payment refunded to customer

**Usage**: Used in `Payment.status` to determine if order can proceed to fulfillment.

---

#### PaymentMethod
**Purpose**: Identifies how the customer paid.

- `RAZORPAY`: Online payment via Razorpay gateway
- `CASH_ON_DELIVERY`: Payment on delivery
- `WALLET`: Payment from user's wallet/account balance

**Usage**: Used in `Payment.method` for payment processing and reporting.

---

#### ShippingStatus
**Purpose**: Tracks physical shipment progress.

- `PENDING`: Awaiting shipment preparation
- `PACKED`: Items packed, ready to ship
- `SHIPPED`: Dispatched to carrier
- `IN_TRANSIT`: On the way to customer
- `DELIVERED`: Successfully delivered
- `RETURNED`: Returned to sender

**Usage**: Used in `ShippingInfo.status` for order tracking and customer updates.

---

#### UserRole
**Purpose**: Defines user permissions and access levels.

- `CUSTOMER`: Regular customer with shopping access
- `ADMIN`: Full system access, can manage all data
- `MODERATOR`: Limited admin access, can moderate content/reviews

**Usage**: Used in `User.role` for authorization and access control.

---

#### ProductStatus
**Purpose**: Indicates product availability and state.

- `ACTIVE`: Product is live and available for purchase
- `INACTIVE`: Product temporarily hidden from catalog
- `OUT_OF_STOCK`: Product exists but no inventory available
- `COMING_SOON`: Product announced but not yet available

**Usage**: Used in `Product.status` to control product visibility and purchasing.

---

#### DiscountType
**Purpose**: Defines how discounts are calculated.

- `PERCENTAGE`: Discount as percentage (e.g., 10% off)
- `FIXED_AMOUNT`: Discount as fixed amount (e.g., ₹100 off)

**Usage**: Used in `Coupon.type` and `Order.discountType` for discount calculations.

---

### User Management

#### User Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key, used in all relationships |
| `email` | String (Unique) | User's email address | Login credential, account recovery, notifications |
| `password` | String | Hashed password | Authentication (must be hashed, never store plain text) |
| `name` | String? | User's full name | Display in UI, order confirmations, personalization |
| `phone` | String? (Unique) | User's phone number | SMS notifications, order updates, account verification |
| `role` | UserRole | User's permission level | Authorization, access control, feature visibility |
| `isEmailVerified` | Boolean | Email verification status | Prevent spam accounts, enable features after verification |
| `isPhoneVerified` | Boolean | Phone verification status | Two-factor auth, SMS notifications |
| `avatar` | String? | Profile picture URL | User profile display, personalization |
| `dateOfBirth` | DateTime? | User's birth date | Age verification, birthday promotions, analytics |
| `gender` | String? | User's gender | Personalization, product recommendations, analytics |
| `createdAt` | DateTime | Account creation timestamp | Analytics, account age, user segmentation |
| `updatedAt` | DateTime | Last update timestamp | Track profile changes |
| `lastLoginAt` | DateTime? | Last login timestamp | Security monitoring, inactive user detection |

**Relationships**:
- `addresses`: One user can have multiple saved addresses
- `cartItems`: User's shopping cart items
- `wishlistItems`: User's saved wishlist items
- `orders`: User's order history
- `reviews`: Reviews written by user
- `aiRecommendations`: AI-generated recommendations for user

---

#### Address Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `userId` | String | Owner of address | Links address to user |
| `type` | String | Address type | "HOME", "WORK", "OTHER" - for organization |
| `fullName` | String | Recipient name | Shipping label, order confirmation |
| `phone` | String | Contact phone | Delivery coordination, order updates |
| `addressLine1` | String | Primary address | Street address, building name |
| `addressLine2` | String? | Secondary address | Apartment, floor, landmark |
| `city` | String | City name | Shipping calculation, delivery routing |
| `state` | String | State/Province | Shipping calculation, tax calculation |
| `postalCode` | String | ZIP/Postal code | Shipping calculation, address validation |
| `country` | String | Country | Default "India", shipping rules |
| `isDefault` | Boolean | Default address flag | Auto-select in checkout, primary address |
| `landmark` | String? | Nearby landmark | Delivery instructions, easier location finding |
| `createdAt` | DateTime | Creation timestamp | Track when address was added |
| `updatedAt` | DateTime | Last update timestamp | Track address changes |

**Relationships**:
- `user`: Address belongs to one user
- `orders`: Address can be used in multiple orders

---

### Product Catalog

#### Category Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `name` | String (Unique) | Category name | Display in navigation, filters |
| `slug` | String (Unique) | URL-friendly identifier | SEO-friendly URLs: `/categories/necklaces` |
| `description` | String? | Category description | SEO, category pages, help users understand category |
| `image` | String? | Category image URL | Category banners, thumbnails |
| `icon` | String? | Category icon | Navigation icons, mobile UI |
| `parentId` | String? | Parent category ID | For hierarchical categories (e.g., "Necklaces" under "Jewellery") |
| `displayOrder` | Int | Display priority | Lower number = appears first in listings |
| `isActive` | Boolean | Active status | Hide inactive categories from frontend |
| `seoTitle` | String? | SEO meta title | Search engine optimization |
| `seoDescription` | String? | SEO meta description | Search engine optimization |
| `createdAt` | DateTime | Creation timestamp | Track when category was added |
| `updatedAt` | DateTime | Last update timestamp | Track category changes |

**Relationships**:
- `parent`: Self-referential - category can have parent category
- `children`: Self-referential - category can have child categories
- `products`: Category contains many products

---

#### Product Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key, used in all relationships |
| `sanityId` | String (Unique) | **CRITICAL LINKING FIELD** | Links to Sanity CMS document `_id`. This connects transactional data (DB) with content data (CMS) |
| `name` | String | Product name | Display in listings, cart, orders |
| `sku` | String (Unique) | Stock Keeping Unit | Inventory management, order tracking, warehouse operations |
| `slug` | String (Unique) | URL-friendly identifier | SEO URLs: `/products/gold-necklace-set` |
| `basePrice` | Decimal(10,2) | Base product price | Default price, used if variant doesn't override |
| `compareAtPrice` | Decimal(10,2)? | Original/List price | Shows "was ₹X, now ₹Y" for discount display |
| `discount` | Decimal(5,2)? | Product-level discount % | Applied if no variant discount exists |
| `stock` | Int | Available inventory | Stock management, out-of-stock detection |
| `lowStockThreshold` | Int | Low stock alert level | Trigger reorder alerts when stock falls below this |
| `trackInventory` | Boolean | Enable inventory tracking | For digital/virtual products, set to false |
| `status` | ProductStatus | Product availability state | Control visibility and purchasing |
| `isActive` | Boolean | Active flag | Quick enable/disable without changing status |
| `isFeatured` | Boolean | Featured product flag | Show on homepage, featured sections |
| `displayRank` | Int? | Display priority | Lower number = appears first in listings (1, 2, 3...) |
| `categoryId` | String | Category foreign key | Links product to category |
| `weight` | Decimal(8,2)? | Product weight in grams | Shipping calculation, product info |
| `dimensions` | Json? | Product dimensions | `{length, width, height}` in cm - shipping calculation |
| `material` | String? | Product material | "Brass", "Copper", "Alloy" - product specifications |
| `finish` | String? | Product finish | "Gold Plated", "Silver Plated", "Antique" - product specifications |
| `createdAt` | DateTime | Creation timestamp | Track when product was added |
| `updatedAt` | DateTime | Last update timestamp | Track product changes |

**Relationships**:
- `category`: Product belongs to one category
- `variants`: Product can have multiple variants (colors, sizes, etc.)
- `cartItems`: Product can be in multiple shopping carts
- `orderItems`: Product can be in multiple orders
- `wishlistItems`: Product can be in multiple wishlists
- `reviews`: Product can have multiple reviews

**Key Field: `sanityId`**
- **CRITICAL**: This field links the database product to its content in Sanity CMS
- When creating a product: Get `_id` from Sanity document and store here
- When fetching a product: Use this to fetch content (images, descriptions) from Sanity
- Must always reference a valid Sanity document

---

#### Variant Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `productId` | String | Parent product ID | Links variant to product |
| `name` | String | Variant name | "Gold", "Silver", "Rose Gold" - displayed to users |
| `sku` | String (Unique) | Variant SKU | Unique identifier for inventory tracking |
| `barcode` | String? (Unique) | Product barcode | Physical inventory scanning, warehouse operations |
| `price` | Decimal(10,2)? | Variant-specific price | Overrides `product.basePrice` if set |
| `compareAtPrice` | Decimal(10,2)? | Variant list price | For discount display on variants |
| `discount` | Decimal(5,2)? | Variant-level discount % | Highest priority discount (overrides product discount) |
| `stock` | Int | Variant inventory | Track stock per variant separately |
| `trackInventory` | Boolean | Enable inventory tracking | For variants that don't need stock tracking |
| `isActive` | Boolean | Active flag | Hide inactive variants from selection |
| `attributes` | Json? | Variant attributes | `{color: "Gold", size: "Medium", metalType: "Plated"}` - for filtering/searching |
| `createdAt` | DateTime | Creation timestamp | Track when variant was added |
| `updatedAt` | DateTime | Last update timestamp | Track variant changes |

**Relationships**:
- `product`: Variant belongs to one product
- `cartItems`: Variant can be in shopping carts
- `orderItems`: Variant can be in orders

**Discount Priority**:
1. Variant-level discount (highest priority)
2. Product-level discount
3. No discount (full price)

---

### Shopping Cart & Wishlist

#### CartItem Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `userId` | String | Cart owner | Links cart item to user |
| `productId` | String | Product in cart | Which product user wants |
| `variantId` | String? | Selected variant | Optional - if product has variants |
| `quantity` | Int | Quantity | How many items user wants |
| `priceAtAdd` | Decimal(10,2) | Price when added | **Price protection**: If price changes, show original price to user |
| `createdAt` | DateTime | Added timestamp | Track when item was added |
| `updatedAt` | DateTime | Last update timestamp | Track quantity changes |

**Unique Constraint**: `[userId, productId, variantId]`
- Prevents duplicate items in cart
- Same user can't add same product+variant twice (quantity increases instead)

**Relationships**:
- `user`: Cart item belongs to one user
- `product`: Cart item references one product
- `variant`: Cart item optionally references one variant

---

#### WishlistItem Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `userId` | String | Wishlist owner | Links wishlist item to user |
| `productId` | String | Saved product | Product user wants to save for later |
| `createdAt` | DateTime | Saved timestamp | Track when item was added to wishlist |

**Unique Constraint**: `[userId, productId]`
- User can only save a product once in wishlist
- No variant distinction (wishlist is product-level)

**Relationships**:
- `user`: Wishlist item belongs to one user
- `product`: Wishlist item references one product

---

### Orders & Payments

#### Order Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key (internal) |
| `orderNumber` | String (Unique) | Human-readable order ID | Display to customers: "ORD-2024-001234" |
| `userId` | String | Order owner | Links order to user |
| `status` | OrderStatus | Current order state | Track order lifecycle |
| `subtotal` | Decimal(10,2) | Items total before discounts | Sum of all order items |
| `discount` | Decimal(10,2) | Total discount amount | Sum of all discounts applied |
| `tax` | Decimal(10,2) | Tax amount | GST, VAT, etc. |
| `shippingCost` | Decimal(10,2) | Shipping charges | Delivery fees |
| `totalAmount` | Decimal(10,2) | Final amount | `subtotal - discount + tax + shipping` |
| `couponCode` | String? | Applied coupon code | Track which coupon was used |
| `discountType` | DiscountType? | Coupon discount type | PERCENTAGE or FIXED_AMOUNT |
| `discountValue` | Decimal(10,2)? | Coupon discount value | Actual discount amount/percentage |
| `createdAt` | DateTime | Order creation timestamp | When order was placed |
| `updatedAt` | DateTime | Last update timestamp | Track order changes |
| `confirmedAt` | DateTime? | Payment confirmation time | When payment was confirmed |
| `shippedAt` | DateTime? | Shipment dispatch time | When order was shipped |
| `deliveredAt` | DateTime? | Delivery completion time | When order was delivered |

**Relationships**:
- `user`: Order belongs to one user
- `orderItems`: Order contains multiple items
- `payment`: Order has one payment record
- `shippingInfo`: Order has one shipping information record

**Pricing Breakdown Example**:
```
Subtotal: ₹5,000
Discount: -₹500 (10% coupon)
Tax: ₹450 (9% GST)
Shipping: ₹100
Total: ₹5,050
```

---

#### OrderItem Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `orderId` | String | Parent order | Links item to order |
| `productId` | String | Product reference | Links to product (for future reference) |
| `variantId` | String? | Variant reference | Links to variant if applicable |
| `productName` | String | **Snapshot**: Product name at order time | Preserves product name even if product is renamed/deleted |
| `variantName` | String? | **Snapshot**: Variant name at order time | Preserves variant name |
| `sku` | String | **Snapshot**: SKU at order time | For order fulfillment, warehouse operations |
| `quantity` | Int | Quantity ordered | How many items |
| `price` | Decimal(10,2) | **Snapshot**: Price at order time | Preserves price even if product price changes |
| `discount` | Decimal(5,2) | Applied discount % | Discount applied to this item |
| `totalPrice` | Decimal(10,2) | Final item price | `price * quantity * (1 - discount/100)` |

**Why Snapshots?**
- Products can be renamed, prices can change, products can be deleted
- Order history must remain accurate
- Customer must see what they actually ordered

**Relationships**:
- `order`: Item belongs to one order
- `product`: Item references product (for current product data)
- `variant`: Item optionally references variant

---

#### Payment Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `orderId` | String (Unique) | Linked order | One payment per order |
| `amount` | Decimal(10,2) | Payment amount | Amount charged to customer |
| `currency` | String | Currency code | Default "INR" (Indian Rupees) |
| `method` | PaymentMethod | Payment method | RAZORPAY, CASH_ON_DELIVERY, WALLET |
| `status` | PaymentStatus | Payment state | PENDING, SUCCESS, FAILED, REFUNDED |
| `razorpayOrderId` | String? (Unique) | Razorpay order ID | Razorpay gateway order identifier |
| `razorpayPaymentId` | String? (Unique) | Razorpay payment ID | Razorpay transaction identifier |
| `razorpaySignature` | String? | Payment signature | For webhook verification (security) |
| `transactionId` | String? | Transaction reference | Bank/processor transaction ID |
| `failureReason` | String? | Failure description | Why payment failed (for debugging) |
| `createdAt` | DateTime | Payment initiation time | When payment was attempted |
| `updatedAt` | DateTime | Last update time | Track payment status changes |
| `paidAt` | DateTime? | Payment completion time | When payment was successfully processed |

**Razorpay Integration Flow**:
1. Create Razorpay order → Store `razorpayOrderId`
2. Customer pays → Razorpay returns `razorpayPaymentId`
3. Webhook verification → Verify `razorpaySignature`
4. Update status → Set `status = SUCCESS`, `paidAt = now()`

**Relationships**:
- `order`: Payment belongs to one order (1:1 relationship)

---

#### ShippingInfo Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `orderId` | String (Unique) | Linked order | One shipping info per order |
| `addressId` | String? | Saved address reference | Optional link to user's saved address |
| `fullName` | String | Recipient name | Shipping label |
| `phone` | String | Contact phone | Delivery coordination |
| `addressLine1` | String | Primary address | Shipping address |
| `addressLine2` | String? | Secondary address | Additional address details |
| `city` | String | City | Shipping destination |
| `state` | String | State/Province | Shipping destination |
| `postalCode` | String | ZIP code | Shipping destination |
| `country` | String | Country | Default "India" |
| `status` | ShippingStatus | Shipping state | PENDING, PACKED, SHIPPED, IN_TRANSIT, DELIVERED, RETURNED |
| `trackingNumber` | String? | Carrier tracking number | Customer can track shipment |
| `carrier` | String? | Shipping company | "FedEx", "BlueDart", "India Post" |
| `estimatedDelivery` | DateTime? | Expected delivery date | Show to customer |
| `actualDelivery` | DateTime? | Actual delivery date | Track when delivered |
| `createdAt` | DateTime | Creation timestamp | When shipping info was created |
| `updatedAt` | DateTime | Last update timestamp | Track shipping status changes |

**Why Duplicate Address Fields?**
- Address can be edited at checkout (different from saved address)
- Saved address might be deleted later
- Need to preserve exact shipping address used for order

**Relationships**:
- `order`: Shipping info belongs to one order (1:1)
- `address`: Optionally references saved address

---

### Reviews & Ratings

#### Review Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `userId` | String | Reviewer | Who wrote the review |
| `productId` | String | Reviewed product | Which product is reviewed |
| `orderId` | String? | Order reference | Link to order for verified purchase badge |
| `rating` | Int | Star rating | 1-5 stars (1=worst, 5=best) |
| `title` | String? | Review title | Short summary of review |
| `comment` | String? | Review text | Detailed review content |
| `isApproved` | Boolean | Moderation status | Admin must approve before showing publicly |
| `isVerifiedPurchase` | Boolean | Verified purchase flag | True if `orderId` exists and order is delivered |
| `createdAt` | DateTime | Review creation time | When review was written |
| `updatedAt` | DateTime | Last update time | Track review edits |

**Unique Constraint**: `[userId, productId, orderId]`
- One review per order (prevents duplicate reviews)
- User can review same product from different orders

**Moderation Workflow**:
1. User submits review → `isApproved = false`
2. Admin reviews → Set `isApproved = true`
3. Review appears on product page

**Relationships**:
- `user`: Review written by one user
- `product`: Review for one product

---

### Discounts & Coupons

#### Coupon Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `code` | String (Unique) | Coupon code | What customers enter: "SAVE10", "WELCOME50" |
| `type` | DiscountType | Discount calculation | PERCENTAGE or FIXED_AMOUNT |
| `value` | Decimal(10,2) | Discount value | 10 (for 10%) or 100 (for ₹100 off) |
| `minPurchaseAmount` | Decimal(10,2)? | Minimum order value | Coupon only works if order ≥ this amount |
| `maxDiscountAmount` | Decimal(10,2)? | Maximum discount cap | Limit discount even if percentage would be higher |
| `maxUses` | Int? | Total usage limit | Coupon can be used X times total (null = unlimited) |
| `maxUsesPerUser` | Int? | Per-user limit | Each user can use coupon X times (default: 1) |
| `usedCount` | Int | Usage counter | Track how many times coupon has been used |
| `validFrom` | DateTime | Start date | Coupon active from this date |
| `validUntil` | DateTime | End date | Coupon expires on this date |
| `isActive` | Boolean | Active flag | Quick enable/disable |
| `applicableCategories` | Json? | Category restrictions | Array of category IDs - coupon only works for these categories |
| `applicableProducts` | Json? | Product restrictions | Array of product IDs - coupon only works for these products |
| `excludeProducts` | Json? | Excluded products | Array of product IDs - coupon doesn't work for these |
| `createdAt` | DateTime | Creation timestamp | When coupon was created |
| `updatedAt` | DateTime | Last update timestamp | Track coupon changes |

**Example Coupon**:
```json
{
  "code": "SUMMER20",
  "type": "PERCENTAGE",
  "value": 20,
  "minPurchaseAmount": 1000,
  "maxDiscountAmount": 500,
  "maxUses": 1000,
  "maxUsesPerUser": 1,
  "validFrom": "2024-06-01",
  "validUntil": "2024-08-31"
}
```
- 20% off
- Minimum order ₹1,000
- Maximum discount ₹500 (even if 20% of order is more)
- Can be used 1000 times total
- Each user can use once
- Valid June-August 2024

**Relationships**: None (standalone model)

---

### AI Recommendations

#### AIRecommendation Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `userId` | String? | User reference | Optional - can be anonymous recommendations |
| `imageUrl` | String | Input image URL | Dress image uploaded by user |
| `imageHash` | String? | Image hash | For deduplication (same image = same recommendations) |
| `productIds` | String[] | Recommended products | Array of product IDs that match the image |
| `scores` | Float[] | Confidence scores | Array of scores (0-1) matching productIds order |
| `occasion` | String? | Detected occasion | "Wedding", "Party", "Casual" - extracted from image |
| `colorPalette` | Json? | Extracted colors | `{primary: "#FFD700", secondary: "#FF69B4"}` - colors from image |
| `style` | String? | Detected style | "Traditional", "Modern", "Vintage" - extracted from image |
| `createdAt` | DateTime | Creation timestamp | When recommendation was generated |

**Usage Flow**:
1. User uploads dress image → Store `imageUrl`
2. AI service analyzes image → Returns recommendations
3. Store `productIds` and `scores` → Show to user
4. Track `occasion`, `colorPalette`, `style` → For analytics and ML improvement

**Relationships**:
- `user`: Optional link to user (for personalized recommendations)

---

### Analytics & Tracking

#### ProductView Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `productId` | String | Viewed product | Which product was viewed |
| `userId` | String? | Viewer (if logged in) | Track logged-in user views |
| `sessionId` | String? | Anonymous session | Track anonymous user views |
| `ipAddress` | String? | Viewer IP | Analytics, fraud detection |
| `userAgent` | String? | Browser/device info | Analytics, device breakdown |
| `referrer` | String? | Source URL | Where user came from (Google, social media, etc.) |
| `createdAt` | DateTime | View timestamp | When product was viewed |

**Usage**: Track product popularity, user behavior, conversion rates

**Relationships**: None (analytics model)

---

#### SearchQuery Model

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `id` | String (CUID) | Unique identifier | Primary key |
| `query` | String | Search term | What user searched for |
| `userId` | String? | Searcher | Track logged-in searches |
| `sessionId` | String? | Anonymous session | Track anonymous searches |
| `resultsCount` | Int | Number of results | How many products matched |
| `createdAt` | DateTime | Search timestamp | When search was performed |

**Usage**: 
- Popular search terms
- Zero-result searches (improve catalog)
- Search-to-purchase conversion

**Relationships**: None (analytics model)

---

## Sanity CMS Schema Fields

### Product Schema

#### Basic Information

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `sanityId` | String | **CRITICAL LINKING FIELD** | Auto-generated Sanity document `_id`. Must match `Product.sanityId` in database. |
| `title` | String | Product title | Display name: "Elegant Gold Plated Necklace Set" |
| `slug` | Slug | URL-friendly identifier | Auto-generated from title, used in URLs |
| `description` | Text | Product description | Main product description (50-1000 chars) |
| `shortDescription` | Text | Brief description | For product cards, max 150 chars |
| `detailedDescription` | Array (Blocks) | Rich text description | Full product details with formatting, images |

#### Images

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `images` | Array (Images) | Product images | Multiple product photos |
| `images[].alt` | String | Image alt text | Accessibility, SEO |
| `images[].isPrimary` | Boolean | Primary image flag | Main product image for listings |

#### Category & Organization

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `category` | Reference | Product category | Links to category document |
| `tags` | Array (Strings) | Searchable tags | ["trending", "elegant", "traditional"] - for filtering |

#### Attributes

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `attributes.material` | String | Product material | "Brass", "Copper", "Alloy" |
| `attributes.finish` | String | Product finish | "Gold Plated", "Silver Plated", "Antique" |
| `attributes.occasion` | Array | Suitable occasions | ["wedding", "party", "casual"] |
| `attributes.style` | Array | Design style | ["traditional", "modern", "contemporary"] |
| `attributes.color` | Array | Available colors | ["Gold", "Silver", "Rose Gold"] - used to create variants |
| `attributes.size` | String | Product size | "Small", "Medium", "Large", "One Size" |
| `attributes.weight` | Number | Weight in grams | Product specifications |
| `attributes.dimensions` | Object | Dimensions | `{length, width, height}` in cm |

#### Display & Marketing

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `badge` | String | Display badge | "new", "sale", "bestseller", "limited", "trending" |
| `displayRank` | Number | Display priority | Lower number = appears first (1, 2, 3...) |
| `isFeatured` | Boolean | Featured flag | Show on homepage, featured sections |

#### SEO

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `seo.metaTitle` | String | SEO title | Max 60 chars, for search engines |
| `seo.metaDescription` | Text | SEO description | Max 160 chars, search result snippet |
| `seo.keywords` | Array | SEO keywords | Keywords for search optimization |

#### Additional Content

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `careInstructions` | Array | Care guide | How to maintain the jewellery |
| `relatedProducts` | Array (References) | Related products | Manually curated product recommendations |
| `video.url` | URL | Product video | YouTube/Vimeo URL for product showcase |
| `video.thumbnail` | Image | Video thumbnail | Preview image for video |

---

### Category Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `name` | String | Category name | "Necklaces", "Earrings", "Rings" |
| `slug` | Slug | URL-friendly identifier | Auto-generated, used in URLs |
| `description` | Text | Category description | Explain what this category contains |
| `image` | Image | Category image | Banner/thumbnail for category page |
| `image.alt` | String | Image alt text | Accessibility |
| `icon` | String | Category icon | Emoji or icon name (💍, 👑) |
| `parent` | Reference | Parent category | For hierarchical categories |
| `displayOrder` | Number | Display priority | Lower number = appears first |
| `isActive` | Boolean | Active flag | Show/hide category |
| `seo.metaTitle` | String | SEO title | Max 60 chars |
| `seo.metaDescription` | Text | SEO description | Max 160 chars |

---

### Collection Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `title` | String | Collection name | "Summer Collection 2024" |
| `slug` | Slug | URL-friendly identifier | Auto-generated |
| `description` | Text | Collection description | Marketing copy for collection |
| `image` | Image | Collection image | Banner/hero image |
| `products` | Array (References) | Products in collection | Curated product set |
| `isActive` | Boolean | Active flag | Show/hide collection |
| `displayOrder` | Number | Display priority | Lower number = appears first |

**Usage**: Create themed product collections (e.g., "Wedding Collection", "Festival Special")

---

### Blog Post Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `title` | String | Blog post title | Article headline |
| `slug` | Slug | URL-friendly identifier | Auto-generated |
| `author` | Reference | Post author | Links to author document |
| `mainImage` | Image | Featured image | Hero image for blog post |
| `categories` | Array (References) | Blog categories | Organize posts by topic |
| `publishedAt` | DateTime | Publication date | When post goes live |
| `excerpt` | Text | Post excerpt | Short summary for listings |
| `body` | Array (Blocks) | Post content | Full article with rich text, images |
| `relatedProducts` | Array (References) | Related products | Link products mentioned in article |

**Usage**: Content marketing, SEO, product education

---

### Author Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `name` | String | Author name | Display name |
| `slug` | Slug | URL-friendly identifier | Author profile URL |
| `image` | Image | Author photo | Profile picture |
| `bio` | Array (Blocks) | Author biography | Rich text bio |

**Usage**: Blog post authors, content creators

---

### Blog Category Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `title` | String | Category name | "Fashion Tips", "Jewellery Care" |
| `slug` | Slug | URL-friendly identifier | Auto-generated |
| `description` | Text | Category description | Explain category purpose |

**Usage**: Organize blog posts by topic

---

### Hero Section Schema

| Field | Type | Purpose | Usage |
|-------|------|---------|-------|
| `title` | String | Hero title | Main headline |
| `subtitle` | String | Hero subtitle | Supporting text |
| `image` | Image | Hero image | Background/banner image |
| `ctaButton.text` | String | Button text | "Shop Now", "Explore Collection" |
| `ctaButton.link` | String | Button link | Where button navigates |
| `isActive` | Boolean | Active flag | Show/hide hero section |
| `displayOrder` | Number | Display priority | Multiple hero sections, order them |

**Usage**: Homepage hero banners, promotional sections

---

## 🔗 Key Relationships Summary

### Database ↔ Sanity Linking

**Critical Connection**:
- `Product.sanityId` (Database) = `product._id` (Sanity)
- This single field connects all transactional data with content data

### Data Flow

1. **Product Creation**:
   - Create in Sanity → Get `_id`
   - Create in Database → Set `sanityId = _id`

2. **Product Retrieval**:
   - Fetch from Database → Get `sanityId`
   - Fetch from Sanity using `_id = sanityId`
   - Merge data → Complete product object

3. **Product Updates**:
   - Content updates → Sanity only
   - Price/stock updates → Database only
   - Both systems updated independently

---

## 📝 Field Usage Best Practices

### Database Fields
- **Never expose passwords**: Always hash before storing
- **Use snapshots in orders**: Preserve historical data
- **Track timestamps**: For analytics and auditing
- **Use enums**: For consistent status values
- **Index frequently queried fields**: `slug`, `sku`, `email`, `status`

### Sanity Fields
- **Rich content**: Use blocks for formatted text
- **SEO optimization**: Always fill meta fields
- **Image optimization**: Use appropriate image sizes
- **Accessibility**: Always provide alt text
- **Validation**: Use validation rules for data quality

---

## 🎯 Common Use Cases

### Finding Products
- By category: `Product.categoryId = category.id`
- By status: `Product.status = 'ACTIVE'`
- By stock: `Product.stock > 0`
- By featured: `Product.isFeatured = true`

### Calculating Prices
1. Check variant discount (highest priority)
2. Check product discount
3. Apply discount: `finalPrice = basePrice * (1 - discount/100)`

### Order Processing
1. Create order with `status = PENDING`
2. Create payment with `status = PENDING`
3. Process payment → Update `payment.status = SUCCESS`
4. Update `order.status = CONFIRMED`
5. Fulfill order → Update `order.status = SHIPPED`

---

This documentation covers every field in both schemas. Use this as a reference when implementing features, writing queries, or understanding the data model.

