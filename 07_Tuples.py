# 07_Tuples.py - Storing Immutable Order Details Using Tuples

# List to store multiple orders (each order as a tuple)
orders = []

# Function to take an order
def take_order():
    table_number = int(input("Enter table number: "))
    customer_name = input("Enter customer name: ")
    dish_ordered = input("Enter dish ordered: ")
    quantity = int(input("Enter quantity: "))
    price_per_dish = float(input("Enter price per dish: "))
    dine_in_input = input("Dine-in? (yes/no): ").lower()
    
    # Determine service type
    dine_in = dine_in_input == "yes"

    # Calculate total price
    total_price = quantity * price_per_dish

    # Store order as a tuple (immutable data)
    order = (table_number, customer_name, dish_ordered, quantity, total_price, dine_in)
    
    orders.append(order)  # Add order to the list

# Function to display all orders
def display_orders():
    if len(orders) == 0:
        print("\nNo orders yet.")
        return
    
    print("\n=== All Orders ===")
    for order in orders:
        table_number, customer_name, dish_ordered, quantity, total_price, dine_in = order
        print(f"\nTable #{table_number} - {customer_name}")
        print(f"{dish_ordered} x {quantity} - ₱{total_price:.2f}")
        print(f"Service Type: {'Dine-in' if dine_in else 'Takeout'}")

# Main function to manage multiple orders
def main():
    while True:
        print("\n1. Take Order")
        print("2. View Orders")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            take_order()
        elif choice == "2":
            display_orders()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
main()
___________________________________________________________________________
Sample output:

1. Take Order
2. View Orders
3. Exit
Enter choice: 1
Enter table number: 2
Enter customer name: wigor
Enter dish ordered: 2
Enter quantity: 2
Enter price per dish: 777
Dine-in? (yes/no): yes

1. Take Order
2. View Orders
3. Exit
Enter choice: 3
Exiting...
