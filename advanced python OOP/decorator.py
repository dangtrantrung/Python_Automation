# def mydecorator(function):
#     def wrapper():
#         print('I am decorating function')
#         function()
#     return wrapper
# def hello_world():
#     print("Hello world")


# mydecorator(hello_world)()

def mydecorator(function):
    def wrapper():
        # function()
        print('I am decorating function')
        function()
    return wrapper

@mydecorator
def hello_world():
    print("Hello world")

hello_world()