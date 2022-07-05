class predicate:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def __and__(self, other):
        # return predicate(lambda *x, **y: self.func(*x, **y) and other.func(*x, **y))
    
        def func(*args, **kwargs):
            return self.func(*args, **kwargs) and other(*args, **kwargs)
        return predicate(func)

    def __or__(self, other):
        return predicate(lambda *x, **y: self.func(*x, **y) or other.func(*x, **y))
    
    def __invert__(self):
        return predicate(lambda *x, **y: not self.func(*x, **y))

    def test(self):
        print('additional test method')


@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

@predicate
def to_be():
    return True

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

@predicate
def return_false():
    return False

@predicate
def return_true():
    return True


print((is_even & is_positive)(4))
print((is_even & is_positive)(3))
print((is_even | is_positive)(3))
print((~is_even & is_positive)(3))

print((to_be | ~to_be)()) # True

print((is_less_than | is_equal)(1, 2)) #True
print((is_less_than | is_equal)(2, b=2)) #True
print((is_less_than | is_equal)(a=3, b=2)) #False


print((((return_false | return_false) & ~return_false) & ((return_false & return_true) | ~return_false))()) #

print('▬')
to_be.test()




# def print_argument(arg):
#     print(arg)
#     # return arg

# def print_is_string(arg):
#     print(isinstance(arg, str))
#     # return isinstance(arg, str)

# print_argument("Hello world")
# print_is_string('some string')
# print('▬▬▬▬')
# # (print_argument)('Hello world')
# (print_argument or print_is_string or True)('Hello world')


# def func1(arg):
#     print(arg)
#     return arg


# class func1:
#     def __str__(self):
#         return "func1".upper()

# print(func1("Hello world"))

