"""
Nested loops — a loop inside a loop. Outer runs once; inner runs fully each time.

"""


# 1) The mental model: rows x columns
# =====================================================================
# For each ROW (outer), sweep every COLUMN (inner).
for row in range(3):                 # 0, 1, 2
    for col in range(4):             # 0, 1, 2, 3  -> runs 4 times PER row
        print(f"({row},{col})", end=" ")
    print()                          # newline AFTER each row (inside outer, after inner)
print()
# That printed 3 x 4 = 12 cells, in 3 lines.

# =====================================================================
# 2) REAL USE: a clean multiplication grid (tables 1..5)
# =====================================================================
print("   |" + "".join(f"{c:>4}" for c in range(1, 6)))
print("---+" + "----" * 5)
for r in range(1, 6):                # each row = one multiplicand
    cells = ""
    for c in range(1, 6):            # each column = the other multiplicand
        cells += f"{r * c:>4}"
    print(f"{r:>2} |{cells}")
print()

# =====================================================================
# 3) REAL USE: every combination (product variants)
# =====================================================================
# An e-commerce SKU for every (colour x size) pair — classic nested-loop job.
colours = ["Red", "Blue"]
sizes = ["S", "M", "L"]
print("Generating product variants:")
for colour in colours:               # 2 colours
    for size in sizes:               # x 3 sizes = 6 variants
        sku = f"TSHIRT-{colour[:3].upper()}-{size}"
        print(f"  {colour} / {size}  ->  {sku}")
print()

# =====================================================================
# 4) REAL USE: scan a 2-D seating grid for free seats
# =====================================================================
# 'O' = free, 'X' = booked. Outer = rows (A, B, C), inner = seat number.
seating = [
    ['O', 'X', 'O', 'O'],
    ['X', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'O'],
]
row_labels = "ABC"
free_seats = []
for r_index, seat_row in enumerate(seating):
    for seat_no, seat in enumerate(seat_row, start=1):
        if seat == 'O':
            free_seats.append(f"{row_labels[r_index]}{seat_no}")
print("Available seats:", ", ".join(free_seats))
print()

# =====================================================================
# 5) break only escapes the INNER loop
# =====================================================================
# Find the first booked seat in each row (then move to the next row).
print("First booked seat per row:")
for r_index, seat_row in enumerate(seating):
    for seat_no, seat in enumerate(seat_row, start=1):
        if seat == 'X':
            print(f"  Row {row_labels[r_index]}: seat {seat_no}")
            break                    # exits THIS row's inner loop only
    # ...outer loop continues to the next row here