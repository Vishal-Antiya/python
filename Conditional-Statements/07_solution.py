size = input("enter the size of your coffee")
shot = input("do you want an extra espresso shot?Y/N:")

if size == "small":
    coffee = "small coffee" if shot == 'N' else "small coffee w xtra shot"
    print(coffee)
elif size == "medium":
    coffee = "Medium coffee" if shot == 'N' else "Medium coffee w xtra shot"
    print(coffee)
elif size == "large":
    coffee = "Large coffee" if shot == 'N' else "Large coffee w xtra shot"
    print(coffee)
else:
    print("choose sizes bw small, medium, large")