# 09_Dictionaries.py - Storing and Retrieving Customer Orders

# Dictionary to store orders (key: table number, value: order details)
orders = {}

# Function to take an order
def take_order():
    table_number = input("Enter table number: ")
    customer_name = input("Enter customer name: ")
    dish_ordered = input("Enter dish ordered: ")
    quantity = int(input("Enter quantity: "))

    # Store order in dictionary
    orders[table_number] = {
        "Customer": customer_name,
        "Dish": dish_ordered,
        "Quantity": quantity
    }

    print(f"Order recorded for Table {table_number}")

# Function to view all orders
def view_orders():
    if not orders:
        print("\nNo orders placed yet.")
        return

    print("\n=== All Orders ===")
    for table, details in orders.items():
        print(f"Table {table}: {details['Customer']} ordered {details['Quantity']}x {details['Dish']}")

# Function to retrieve order by table number
def get_order():
    table_number = input("Enter table number to retrieve order: ")

    if table_number in orders:
        details = orders[table_number]
        print(f"\nOrder for Table {table_number}:")
        print(f"{details['Customer']} ordered {details['Quantity']}x {details['Dish']}")
    else:
        print("No order found for this table.")

# Main function to manage orders
def main():
    while True:
        print("\n1. Take Order")
        print("2. View All Orders")
        print("3. Retrieve Order by Table Number")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            take_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            get_order()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
main()
________________________________________________________________________________________________

Sample output:


1. Take Order
2. View All Orders
3. Retrieve Order by Table Number
4. Exit
Enter choice: 1
Enter table number: 2
Enter customer name: Wigor
Enter dish ordered: 1
Enter quantity: 1
Order recorded for Table 2

1. Take Order
2. View All Orders
3. Retrieve Order by Table Number
4. Exit
Enter choice: 2

=== All Orders ===
Table 2: Wigor ordered 1x 1

1. Take Order
2. View All Orders
3. Retrieve Order by Table Number
4. Exit
Enter choice: 
