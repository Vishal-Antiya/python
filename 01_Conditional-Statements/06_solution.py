dist = int(input("enter the distance to be travelled: "))

if dist < 3:
    print("I think you should walk")
elif dist < 16:
    print("You can use the bike.")
else:
    print("CARRR")