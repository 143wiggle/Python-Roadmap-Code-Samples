# 08_Sets.py - Tracking Unique Ordered Dishes

# Set to store unique dishes ordered
unique_dishes = set()

# Function to take an order
def take_order():
    customer_name = input("Enter customer name: ")
    dish_ordered = input("Enter dish ordered: ")

    # Add dish to the set (automatically prevents duplicates)
    unique_dishes.add(dish_ordered)

    print(f"Order recorded for {customer_name}: {dish_ordered}")

# Function to display unique dishes
def display_unique_dishes():
    if len(unique_dishes) == 0:
        print("\nNo dishes ordered yet.")
        return
    
    print("\n=== Unique Dishes Ordered ===")
    for dish in unique_dishes:
        print(f"- {dish}")

# Main function to manage orders
def main():
    while True:
        print("\n1. Take Order")
        print("2. View Unique Dishes Ordered")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            take_order()
        elif choice == "2":
            display_unique_dishes()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
main()
____________________________________________________________________________
Sample output:


1. Take Order
2. View Unique Dishes Ordered
3. Exit
Enter choice: 1
Enter customer name: Wigor
Enter dish ordered: 2
Order recorded for Wigor: 2

1. Take Order
2. View Unique Dishes Ordered
3. Exit
Enter choice: 3
Exiting...
