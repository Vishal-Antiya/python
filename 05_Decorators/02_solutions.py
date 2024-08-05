def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ", ".join(str(i) for i in args)
        kwarg_value  = ", ".join(f"{k} : {v}" for k,v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"{func.__name__} is running with args {arg_value} and kwargs {kwarg_value}")
        return result
    return wrapper

@debug
def greet(name = "John Doe", greeting = "Hello"):
    return f"{greeting}, {name}"

print(greet("Vishal", greeting = "Kaise ho"))