data = {}
print("Welcome to the Personal Finance Tracker!")
while True:
    print("1.Add Expense  2.View Expenses  3.View Summary  4.Exit")
    choice = input("> ")
    if choice == "1":
        desc = input("Description: ")
        cat = input("Category: ")
        amt = input("Amount: ")
        try:
            amt = float(amt)
            data.setdefault(cat, []).append((desc, amt))
            print("Expense added")
        except:
            print("Invalid amount")
    elif choice == "2":
        for cat, exps in data.items():
            print(cat)
            for d, a in exps:
                print(f"  - {d}: ${a:.2f}")
    elif choice == "3":
        for cat, exps in data.items():
            print(f"{cat}: ${sum(a for _, a in exps):.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
