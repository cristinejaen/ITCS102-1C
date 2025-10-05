try:
    item_price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))

    if item_price <= 0 or quantity <= 0:
        print("Error: Price and quantity must be positive numbers.")
    else:
        total_cost = item_price * quantity

        if total_cost > 100:
            final_cost = total_cost * 0.9   # Apply 10% discount
            discount_msg = "(with 10% discount)"
        else:
            final_cost = total_cost
            discount_msg = "(no discount applied)"

        print(f"\nItem Price: ${item_price}")
        print(f"Quantity: {quantity}")
        print(f"Total Cost: ${total_cost}")
        print(f"Final Cost {discount_msg}: ${final_cost}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")