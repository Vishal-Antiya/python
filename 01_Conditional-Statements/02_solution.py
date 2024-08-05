day = input("Enter the day: ")
age = int(input("Enter the age: "))

# if day != "wed" and age < 18:
#     print("Ticket price is 8$")
# elif day == "wed" and age < 18:
#     print("Ticket price is 6$")
# elif day == "wed":
#     print("Ticket price is 10$")
# else:
#     print("Ticket price is 12$")


if day == "wednesday":
    price = 10 if age>=18 else 6
    print("Ticket Price:",price,"$")
else:
    price = 12 if age>=18 else 8
    print("Ticket Price:",price,"$")

