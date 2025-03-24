# 02_DataTypes.py - Customer Order with Data Types

# Collect order details
table_number = int(input("Enter table number: "))  # Integer
customer_name = input("Enter customer name: ")  # String
dish_ordered = input("Enter dish ordered: ")  # String
quantity = int(input("Enter quantity: "))  # Integer
price_per_dish = float(input("Enter price per dish: "))  # Float
dine_in = input("Dine-in? (yes/no): ").lower() == "yes"  # Boolean

# Calculate total price
total_price = quantity * price_per_dish

# Print order summary
print("\n=== Order Summary ===")
print(f"Table #{table_number} - {customer_name}")
print(f"{dish_ordered} x {quantity} - ₱{total_price:.2f}")
print(f"Dine-in: {'Yes' if dine_in else 'No'}")
