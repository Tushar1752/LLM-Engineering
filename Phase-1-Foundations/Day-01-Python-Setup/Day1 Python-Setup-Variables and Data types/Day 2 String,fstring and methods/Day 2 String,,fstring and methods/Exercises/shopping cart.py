"""
Shopping Cart receipt.
"""


item = "Wireless Mouse"
price = 799.0
quantity = 3
gst_rate = 0.18

subtotal = price * quantity
gst = subtotal * gst_rate
total = subtotal + gst

print(f"{item} x {quantity}")
print(f"Subtotal: Rs {subtotal:,.2f}")
print(f"GST ({gst_rate:.0%}): Rs {gst:,.2f}")
print(f"TOTAL: Rs {total:,.2f}")