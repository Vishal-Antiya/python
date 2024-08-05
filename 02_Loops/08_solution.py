number = 9
isPrime = True

if number < 1:
    print(number, "is not a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime == True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

