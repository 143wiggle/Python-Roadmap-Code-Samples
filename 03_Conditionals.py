# 03_Conditionals.py - Order with Discounts and Service Type

# Collect order details
table_number = int(input("Enter table number: "))  # Integer
customer_name = input("Enter customer name: ")  # String
dish_ordered = input("Enter dish ordered: ")  # String
quantity = int(input("Enter quantity: "))  # Integer
price_per_dish = float(input("Enter price per dish: "))  # Float
dine_in_input = input("Dine-in? (yes/no): ").lower()  # String for user input

# Convert to Boolean
if dine_in_input == "yes":
    dine_in = True
else:
    dine_in = False

# Calculate total price
total_price = quantity * price_per_dish
discount = 0  

# Apply discount if total price is 500 or more
if total_price >= 500:
    discount = total_price * 0.05  # 5% discount
    final_price = total_price - discount
else:
    final_price = total_price  # No discount applied

# Print order summary
print("\n=== Order Summary ===")
print(f"Table #{table_number} - {customer_name}")
print(f"{dish_ordered} x {quantity} - ₱{total_price:.2f}")

# Print discount details
if discount > 0:
    print(f"Discount Applied: ₱{discount:.2f}")

print(f"Final Price: ₱{final_price:.2f}")

# Print dine-in status
if dine_in:
    print("Service Type: Dine-in")
else:
    print("Service Type: Takeout")
