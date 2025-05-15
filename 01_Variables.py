# 01_Variables.py - Simple Waiter's Order Entry

# Get order details
table_number = input("Enter table number: ")
customer_name = input("Enter customer name: ")
dish_ordered = input("Enter dish ordered: ")
quantity = int(input("Enter quantity: "))
price_per_dish = float(input("Enter price per dish: "))

# Calculate total
total_price = quantity * price_per_dish

# Print order summary
print("\n=== Order Summary ===")
print(f"Table #{table_number} - {customer_name}")
print(f"{dish_ordered} x {quantity} - ₱{total_price:.2f}")

