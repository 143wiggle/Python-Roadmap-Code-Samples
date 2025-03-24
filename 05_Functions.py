# 05_Functions.py - Order Calculation using Functions

# Function to calculate total price
def calculate_total_price(quantity, price_per_dish):
    return quantity * price_per_dish

# Function to apply discount
def apply_discount(total_price):
    discount = 0
    if total_price >= 500:
        discount = total_price * 0.05  # 5% discount
    return discount, total_price - discount  # Return both discount and final price

# Function to determine service type
def get_service_type(dine_in_input):
    return dine_in_input.lower() == "yes"

# Function to display order summary
def print_order_summary(table_number, customer_name, dish_ordered, quantity, total_price, discount, final_price, dine_in):
    print("\n=== Order Summary ===")
    print(f"Table #{table_number} - {customer_name}")
    print(f"{dish_ordered} x {quantity} - ₱{total_price:.2f}")

    if discount > 0:
        print(f"Discount Applied: ₱{discount:.2f}")

    print(f"Final Price: ₱{final_price:.2f}")
    print("Service Type: Dine-in" if dine_in else "Service Type: Takeout")

# Main function to handle order processing
def main():
    # Collect order details
    table_number = int(input("Enter table number: "))
    customer_name = input("Enter customer name: ")
    dish_ordered = input("Enter dish ordered: ")
    quantity = int(input("Enter quantity: "))
    price_per_dish = float(input("Enter price per dish: "))
    dine_in_input = input("Dine-in? (yes/no): ")

    # Process order details
    total_price = calculate_total_price(quantity, price_per_dish)
    discount, final_price = apply_discount(total_price)
    dine_in = get_service_type(dine_in_input)

    # Display order summary
    print_order_summary(table_number, customer_name, dish_ordered, quantity, total_price, discount, final_price, dine_in)

# Run the program
main()
________________________________________________________________________________

Sample output:

Enter table number: 8
Enter customer name: Wigor
Enter dish ordered: 2
Enter quantity: 1
Enter price per dish: 888
Dine-in? (yes/no): yes

=== Order Summary ===
Table #8 - Wigor
2 x 1 - ₱888.00
Discount Applied: ₱44.40
Final Price: ₱843.60
Service Type: Dine-in
