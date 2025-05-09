# Let's Get Real! 🛒
# In this project, you’ll create a simple inventory management program using lists, dictionaries, and tuples.

inventory = {
    "battery":   (30, 5.99),
    "Windex":    (15, 6.77),
    "Freshener": (11, 2.99)
}


inventory["Tire patch"] = (12, 22.55)
inventory.pop("Windex")
inventory["battery"] = (28, 5.99)

for item, (qty, price) in inventory.items():
    print(f"Item: {item}, Quantity: {qty}, Price: ${price}")
