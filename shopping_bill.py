
from datetime import datetime

print("=" * 40)
print("             MY SHOP")
print("          SHOPPING RECEIPT")
print("=" * 40)

print("Date:", datetime.now().strftime("%d-%m-%Y"))
print("-" * 40)

items = []
subtotal = 0

while True:
    name = input("Enter item name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    try:
        price = float(input("Enter price per item (₹): "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity. Try again.")
            continue

        amount = price * quantity
        subtotal += amount

        items.append((name, quantity, price, amount))

    except ValueError:
        print("Please enter a valid price and quantity.")

print("\n" + "=" * 55)
print("                    MY SHOP")
print("                 SHOPPING RECEIPT")
print("=" * 55)
print(f"{'Item':<18}{'Qty':>5}{'Price':>12}{'Amount':>12}")
print("-" * 55)

for name, quantity, price, amount in items:
    print(f"{name[:18]:<18}{quantity:>5}{price:>12.2f}{amount:>12.2f}")

print("-" * 55)
print(f"{'Subtotal:':>35} ₹{subtotal:>10.2f}")
print(f"{'Total:':>35} ₹{subtotal:>10.2f}")
print("=" * 55)
print("       Thank you for shopping with us!")
print("=" * 55)