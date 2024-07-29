pet =  input("Enter the species of pet you have: ")
age = int(input("Age of the pet? "))

if pet == "dog":
    food = "dog food" if age >=2 else "puppy food"
    print(food)
elif pet == "cat":
    food = "senior cat food" if age >5 else "kitten food"
    print(food)
