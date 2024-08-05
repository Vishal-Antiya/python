# def factorial(n):
#     m = 1
#     for i in range(n, 1, -1):
#         m = m * i
#     print(m)
            
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
