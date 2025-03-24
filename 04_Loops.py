# 04_Loops.py - Multiple Orders System

orders = []  # List to store all orders
total_sales = 0  # Track total sales

while True:  
    # Collect order details
    table_number = int(input("Enter table number: "))  
    customer_name = input("Enter customer name: ")  
    dish_ordered = input("Enter dish ordered: ")  
    quantity = int(input("Enter quantity: "))  
    price_per_dish = float(input("Enter price per dish: "))  

    # Calculate total price for this order
    total_price = quantity * price_per_dish
    total_sales += total_price  

    # Store order details in a dictionary
    order = {
        "table": table_number,
        "name": customer_name,
        "dish": dish_ordered,
        "quantity": quantity,
        "total_price": total_price
    }
    orders.append(order)  

    # Ask if they want to add another order
    more_orders = input("\nAdd another order? (yes/no): ").lower()
    if more_orders != "yes":
        break  

# Print all orders
print("\n=== Order Summary ===")
for order in orders:
    print(f"Table #{order['table']} - {order['name']} | {order['dish']} x {order['quantity']} | ₱{order['total_price']:.2f}")

print(f"\nTotal Sales: ₱{total_sales:.2f}")

_______________________________________________________________________________________
Output Sample:

Enter table number: 8
Enter customer name: Wigor
Enter dish ordered: Pancit
Enter quantity: 2
Enter price per dish: 88

Add another order? (yes/no): no

=== Order Summary ===
Table #8 - Wigor | Pancit x 2 | ₱176.00

Total Sales: ₱176.00
