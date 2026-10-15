from functools import wraps

def decorate(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'calling : {func.__name__}')
        result = func(*args,**kwargs)
        print(f'Finished: {func.__name__}')
        return result
    return wrapper

@decorate
def brew_chai(type):
    print(f'Brewing {type} chai')
brew_chai('Masala')

        