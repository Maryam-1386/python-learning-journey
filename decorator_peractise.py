def logger(func):

    def wrapper(*args, **kwargs):

        print(f"Executing {func.__name__} ...")

        result = func(*args, **kwargs)

        print("Function finished.")

        return result

    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def multiply(a, b):
    return a * b

print(add(5, 3))

print(multiply(4, 6))

def repeat(times):
    def decorator(func):
        def wrapper(*args ,**kwargs):
            for i in range(times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def hello():
    print("Hello")

hello()

@repeat(3)
def add(a, b):
    return a + b

x = add(2, 3)

print(x)