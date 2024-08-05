password = input("Enter a password:")

if len(password) < 6:
    print("WEAKKK")
elif len(password) < 11:
    print("Medium")
if len(password) > 10:
    print("Strong")