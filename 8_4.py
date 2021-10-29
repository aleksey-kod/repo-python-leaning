from functools import wraps
def val_checker(check):
    def _check(func):

        @wraps(func)
        def wrapper(*args):
            if check(*args):
                return func(*args)
            else:
                msg = f'wrong val {", ".join(map(str, args))}'
                raise ValueError(msg)
        return wrapper
    return _check
        
        


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

try:
    print(calc_cube(3))
    print(calc_cube(-5))
except ValueError as err:
    print(err)
print(calc_cube.__name__)



