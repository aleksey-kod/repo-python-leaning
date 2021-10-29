from functools import wraps
import numbers
def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'\tcall {func.__name__}')
        for arg in *args,*kwargs.values():
            result=None
            if isinstance(arg, numbers.Number):
                result = func(arg)
            print(f'{type(arg)} {arg}: result ->{result} type{type(result)}')
    return wrapper

@type_logger
def calc_cube(x):
    return x**3


print(calc_cube(3,6,{4,3,},"cool",ur=30))
print(calc_cube(7.6,9.3,1,2))
print(calc_cube(67,7.5))

