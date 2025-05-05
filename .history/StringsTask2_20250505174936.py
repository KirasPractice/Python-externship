
#Task 1



pw = input("Enter password: ")

if (
    len(pw) >= 8
    and any(c.isupper() for c in pw)
    and any(c.islower() for c in pw)
    and any(c.isdigit() for c in pw)
    and any(not c.isalnum() for c in pw)
):
    print("Strong password!")
else:
    print("Password must be ≥8 chars, with uppercase, lowercase, digit, and special char.")



