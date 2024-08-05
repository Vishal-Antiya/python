## THIS is the basic syntax for declaring a decorator.

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# @decorator
# ...


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result, 
    return wrapper

@timer      #this is a decorator 
def example_function(n):
    time.sleep(n)

example_function(2)
