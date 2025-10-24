# write a function that measure the time of a function to execute

# import time

# def timer(func):
#     def wrraper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start}")
#         return result
#     return wrraper
# @timer
# def exp(n):
#     time.sleep(n)

# exp(4)

# create a decorator to print the function name and the values of its
# arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwarhs_value = ', '.join(f"{k}={v}"for k, v in kwargs)
        print(f"{func.__name__} and {args_values} and {kwarhs_value}")
        return func(*args, **kwargs)
        
    return wrapper
     


@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name} ")

greet("aniket", "welcome")