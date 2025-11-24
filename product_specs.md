# Product Specifications

## Products
- **Product A**
  - Price: $100
  - ID: add-a
  - Quantity field: qty-a

- **Product B**
  - Price: $150
  - ID: add-b
  - Quantity field: qty-b

## Discount Rule
- Supported discount code: **SAVE15**
- Discount Value: **15%**
- Discount is applied on the subtotal of:
  - (QtyA × $100) + (QtyB × $150)
- Discount code is case-insensitive.
- Discount code should accept leading/trailing spaces.
- Any discount code other than SAVE15 is invalid.

## Error Handling
- Invalid discount → display message in:
  - `<p id="discount-error">Invalid discount code</p>`
- Discount should not apply when:
  - Code is invalid
  - Code is empty

## Cart Total
- Total displayed in:
  - `<span id="total-price">...</span>`
- Total is recalculated after:
  - Quantity updates
  - Clicking “Apply Discount”
  - Adding items using Add to Cart buttons
