# def mydecorator(function):
#     def wrapper():
#         print('I am decorating function')
#         function()
#     return wrapper
# def hello_world():
#     print("Hello world")


# mydecorator(hello_world)()

# def mydecorator(function):
#     def wrapper():
#         # function()
#         print('I am decorating function')
#         function()
#     return wrapper

# @mydecorator
# def hello_world():
#     print("Hello world")

# hello_world()

# def mydecorator(function):
#     def wrapper(*arg,**kargs):
#         # function()
#         print('I am decorating function')
#         function(*arg,**kargs)
#     return wrapper

# @mydecorator
# def hello(person):
#     print(f"Hello {person}")

# hello('Mike')

# decorator with arg, kargs and return function
# def mydecorator(function):
#     def wrapper(*arg,**kargs):
#         # function()
#         print('I am decorating function')
#         return function(*arg,**kargs)
#     return wrapper

# @mydecorator
# def hello(person):
#     return f"Hello {person}"

# print(hello('Mike'))

# decorator with arg, kargs and return value
def mydecorator(function):
    def wrapper(*arg,**kargs):
        # function()
        return_value= function(*arg,**kargs)
        print('I am decorating function')
        return return_value

    return wrapper

@mydecorator
def hello(person):
    print (f"Hello {person}")
    return f"Hello {person}!!! -->return value"

print(hello('Mike'))