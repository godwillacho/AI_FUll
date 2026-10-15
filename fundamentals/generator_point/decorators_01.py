from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print('before function runs')
        func()
        print('After  function runs')
    return wrapper

@my_decorator
def greet():
    print('Hello to decorating shit ')

greet()
