// ============================================
// Artificial Jewellery E-Commerce Platform
// Complete Sanity CMS Schema
// ============================================
// 
// Usage in sanity.config.js:
// import schemas from './schemas'
// export default { ...config, schema: { types: schemas } }

// ============================================
// PRODUCT SCHEMA
// ============================================

const product = {
  name: 'product',
  title: 'Product',
  type: 'document',
  fields: [
    // Linking Field - Critical for connecting to database
    {
      name: 'sanityId',
      title: 'Sanity ID',
      type: 'string',
      description: 'Unique identifier matching DB product.sanityId. Auto-generated on publish.',
      readOnly: true,
      validation: Rule => Rule.required()
    },
    
    // Basic Information
    {
      name: 'title',
      title: 'Product Title',
      type: 'string',
      validation: Rule => Rule.required().max(100)
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96,
        slugify: input => input
          .toLowerCase()
          .replace(/\s+/g, '-')
          .slice(0, 96)
      },
      validation: Rule => Rule.required()
    },
    
    // Description
    {
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 4,
      validation: Rule => Rule.required().min(50).max(1000)
    },
    {
      name: 'shortDescription',
      title: 'Short Description',
      type: 'text',
      rows: 2,
      description: 'Brief description for product cards (max 150 chars)',
      validation: Rule => Rule.max(150)
    },
    {
      name: 'detailedDescription',
      title: 'Detailed Description',
      type: 'array',
      of: [
        {
          type: 'block'
        },
        {
          type: 'image',
          fields: [
            {
              name: 'alt',
              type: 'string',
              title: 'Alternative Text'
            }
          ]
        }
      ]
    },
    
    // Images
    {
      name: 'images',
      title: 'Product Images',
      type: 'array',
      of: [
        {
          type: 'image',
          fields: [
            {
              name: 'alt',
              type: 'string',
              title: 'Alternative Text',
              validation: Rule => Rule.required()
            },
            {
              name: 'isPrimary',
              type: 'boolean',
              title: 'Primary Image',
              description: 'Main product image'
            }
          ],
          options: {
            hotspot: true
          }
        }
      ],
      validation: Rule => Rule.min(1).error('At least one product image is required')
    },
    
    // Category
    {
      name: 'category',
      title: 'Category',
      type: 'reference',
      to: [{ type: 'category' }],
      validation: Rule => Rule.required()
    },
    
    // Tags & Attributes
    {
      name: 'tags',
      title: 'Tags',
      type: 'array',
      of: [{ type: 'string' }],
      options: {
        layout: 'tags'
      },
      description: 'Tags for filtering and search (e.g., trending, elegant, traditional)'
    },
    {
      name: 'attributes',
      title: 'Product Attributes',
      type: 'object',
      fields: [
        {
          name: 'material',
          title: 'Material',
          type: 'string',
          description: 'e.g., Brass, Copper, Alloy'
        },
        {
          name: 'finish',
          title: 'Finish',
          type: 'string',
          description: 'e.g., Gold Plated, Silver Plated, Antique'
        },
        {
          name: 'occasion',
          title: 'Occasion',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            list: [
              { title: 'Wedding', value: 'wedding' },
              { title: 'Party', value: 'party' },
              { title: 'Casual', value: 'casual' },
              { title: 'Festival', value: 'festival' },
              { title: 'Formal', value: 'formal' },
              { title: 'Traditional', value: 'traditional' }
            ]
          }
        },
        {
          name: 'style',
          title: 'Style',
          type: 'array',
          of: [{ type: 'string' }],
          options: {
            list: [
              { title: 'Traditional', value: 'traditional' },
              { title: 'Modern', value: 'modern' },
              { title: 'Contemporary', value: 'contemporary' },
              { title: 'Vintage', value: 'vintage' },
              { title: 'Minimalist', value: 'minimalist' }
            ]
          }
        },
        {
          name: 'color',
          title: 'Color',
          type: 'array',
          of: [{ type: 'string' }],
          description: 'Available colors (e.g., Gold, Silver, Rose Gold)'
        },
        {
          name: 'size',
          title: 'Size',
          type: 'string',
          description: 'e.g., Small, Medium, Large, One Size'
        },
        {
          name: 'weight',
          title: 'Weight (grams)',
          type: 'number'
        },
        {
          name: 'dimensions',
          title: 'Dimensions',
          type: 'object',
          fields: [
            { name: 'length', type: 'number', title: 'Length (cm)' },
            { name: 'width', type: 'number', title: 'Width (cm)' },
            { name: 'height', type: 'number', title: 'Height (cm)' }
          ]
        }
      ]
    },
    
    // Badge & Display
    {
      name: 'badge',
      title: 'Badge',
      type: 'string',
      options: {
        list: [
          { title: 'New', value: 'new' },
          { title: 'Sale', value: 'sale' },
          { title: 'Best Seller', value: 'bestseller' },
          { title: 'Limited Edition', value: 'limited' },
          { title: 'Trending', value: 'trending' }
        ]
      }
    },
    {
      name: 'displayRank',
      title: 'Display Rank',
      type: 'number',
      description: 'Lower number = higher priority in listings (1, 2, 3...)',
      validation: Rule => Rule.integer().min(1)
    },
    {
      name: 'isFeatured',
      title: 'Featured Product',
      type: 'boolean',
      description: 'Show on homepage/featured section'
    },
    
    // SEO
    {
      name: 'seo',
      title: 'SEO Settings',
      type: 'object',
      fields: [
        {
          name: 'metaTitle',
          title: 'Meta Title',
          type: 'string',
          validation: Rule => Rule.max(60)
        },
        {
          name: 'metaDescription',
          title: 'Meta Description',
          type: 'text',
          rows: 3,
          validation: Rule => Rule.max(160)
        },
        {
          name: 'keywords',
          title: 'Keywords',
          type: 'array',
          of: [{ type: 'string' }]
        }
      ]
    },
    
    // Care Instructions
    {
      name: 'careInstructions',
      title: 'Care Instructions',
      type: 'array',
      of: [{ type: 'string' }],
      description: 'How to care for this jewellery piece'
    },
    
    // Related Products
    {
      name: 'relatedProducts',
      title: 'Related Products',
      type: 'array',
      of: [
        {
          type: 'reference',
          to: [{ type: 'product' }]
        }
      ],
      description: 'Manually curated related products'
    },
    
    // Video
    {
      name: 'video',
      title: 'Product Video',
      type: 'object',
      fields: [
        {
          name: 'url',
          title: 'Video URL',
          type: 'url',
          description: 'YouTube, Vimeo, or direct video URL'
        },
        {
          name: 'thumbnail',
          title: 'Video Thumbnail',
          type: 'image'
        }
      ]
    }
  ],
  
  preview: {
    select: {
      title: 'title',
      media: 'images.0',
      badge: 'badge'
    },
    prepare({ title, media, badge }) {
      return {
        title: title,
        subtitle: badge ? `Badge: ${badge}` : '',
        media: media
      }
    }
  },
  
  orderings: [
    {
      title: 'Display Rank',
      name: 'displayRankAsc',
      by: [{ field: 'displayRank', direction: 'asc' }]
    },
    {
      title: 'Title',
      name: 'titleAsc',
      by: [{ field: 'title', direction: 'asc' }]
    }
  ]
}

// ============================================
// CATEGORY SCHEMA
// ============================================

const category = {
  name: 'category',
  title: 'Category',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Category Name',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'name',
        maxLength: 96
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 3
    },
    {
      name: 'image',
      title: 'Category Image',
      type: 'image',
      options: {
        hotspot: true
      },
      fields: [
        {
          name: 'alt',
          type: 'string',
          title: 'Alternative Text'
        }
      ]
    },
    {
      name: 'icon',
      title: 'Icon',
      type: 'string',
      description: 'Icon name or emoji (e.g., 💍, 👑)'
    },
    {
      name: 'parent',
      title: 'Parent Category',
      type: 'reference',
      to: [{ type: 'category' }],
      description: 'For hierarchical categories'
    },
    {
      name: 'displayOrder',
      title: 'Display Order',
      type: 'number',
      description: 'Lower number = appears first',
      validation: Rule => Rule.integer().min(0)
    },
    {
      name: 'isActive',
      title: 'Active',
      type: 'boolean',
      description: 'Show this category on the website',
      initialValue: true
    },
    {
      name: 'seo',
      title: 'SEO Settings',
      type: 'object',
      fields: [
        {
          name: 'metaTitle',
          title: 'Meta Title',
          type: 'string',
          validation: Rule => Rule.max(60)
        },
        {
          name: 'metaDescription',
          title: 'Meta Description',
          type: 'text',
          rows: 3,
          validation: Rule => Rule.max(160)
        }
      ]
    }
  ],
  
  preview: {
    select: {
      title: 'name',
      media: 'image',
      parent: 'parent.name'
    },
    prepare({ title, media, parent }) {
      return {
        title: title,
        subtitle: parent ? `Parent: ${parent}` : 'Top Level',
        media: media
      }
    }
  }
}

// ============================================
// COLLECTION SCHEMA (for curated product sets)
// ============================================

const collection = {
  name: 'collection',
  title: 'Collection',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Collection Title',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 4
    },
    {
      name: 'image',
      title: 'Collection Image',
      type: 'image',
      options: {
        hotspot: true
      }
    },
    {
      name: 'products',
      title: 'Products',
      type: 'array',
      of: [
        {
          type: 'reference',
          to: [{ type: 'product' }]
        }
      ]
    },
    {
      name: 'isActive',
      title: 'Active',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'displayOrder',
      title: 'Display Order',
      type: 'number'
    }
  ]
}

// ============================================
// BLOG POST SCHEMA (for content marketing)
// ============================================

const blogPost = {
  name: 'blogPost',
  title: 'Blog Post',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'author',
      title: 'Author',
      type: 'reference',
      to: [{ type: 'author' }]
    },
    {
      name: 'mainImage',
      title: 'Main Image',
      type: 'image',
      options: {
        hotspot: true
      }
    },
    {
      name: 'categories',
      title: 'Categories',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'blogCategory' }] }]
    },
    {
      name: 'publishedAt',
      title: 'Published At',
      type: 'datetime',
      validation: Rule => Rule.required()
    },
    {
      name: 'excerpt',
      title: 'Excerpt',
      type: 'text',
      rows: 3
    },
    {
      name: 'body',
      title: 'Body',
      type: 'array',
      of: [
        {
          type: 'block'
        },
        {
          type: 'image',
          fields: [
            {
              name: 'alt',
              type: 'string',
              title: 'Alternative Text'
            }
          ]
        }
      ]
    },
    {
      name: 'relatedProducts',
      title: 'Related Products',
      type: 'array',
      of: [
        {
          type: 'reference',
          to: [{ type: 'product' }]
        }
      ]
    }
  ],
  
  preview: {
    select: {
      title: 'title',
      author: 'author.name',
      media: 'mainImage'
    },
    prepare({ title, author, media }) {
      return {
        title: title,
        subtitle: author ? `by ${author}` : '',
        media: media
      }
    }
  }
}

// ============================================
// AUTHOR SCHEMA
// ============================================

const author = {
  name: 'author',
  title: 'Author',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Name',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'name',
        maxLength: 96
      }
    },
    {
      name: 'image',
      title: 'Image',
      type: 'image',
      options: {
        hotspot: true
      }
    },
    {
      name: 'bio',
      title: 'Bio',
      type: 'array',
      of: [
        {
          type: 'block'
        }
      ]
    }
  ],
  
  preview: {
    select: {
      title: 'name',
      media: 'image'
    }
  }
}

// ============================================
// BLOG CATEGORY SCHEMA
// ============================================

const blogCategory = {
  name: 'blogCategory',
  title: 'Blog Category',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96
      }
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text'
    }
  ]
}

// ============================================
// HOMEPAGE HERO SCHEMA
// ============================================

const heroSection = {
  name: 'heroSection',
  title: 'Hero Section',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'subtitle',
      title: 'Subtitle',
      type: 'string'
    },
    {
      name: 'image',
      title: 'Hero Image',
      type: 'image',
      options: {
        hotspot: true
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'ctaButton',
      title: 'CTA Button',
      type: 'object',
      fields: [
        {
          name: 'text',
          title: 'Button Text',
          type: 'string'
        },
        {
          name: 'link',
          title: 'Link',
          type: 'string'
        }
      ]
    },
    {
      name: 'isActive',
      title: 'Active',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'displayOrder',
      title: 'Display Order',
      type: 'number'
    }
  ]
}

// ============================================
// EXPORT ALL SCHEMAS
// ============================================

export default [
  product,
  category,
  collection,
  blogPost,
  author,
  blogCategory,
  heroSection
]
