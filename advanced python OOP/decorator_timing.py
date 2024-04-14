import time


def timed(function):
    def wrapper(*args,**kargs):
        before=time.time()
        value=function(*args,**kargs)
        after=time.time()
        fname=function.__name__
        print(f'{fname} took {after-before} seconds to execute, result = {value}')
        return value
    return wrapper


@timed
def myfunction(x):
    result=1
    for i in range(1,x):
        result*=i
    return result

@timed
def myfunction1(x):
    result=1
    for i in range(1,x):
        result+=i
    return result
myfunction(100)
myfunction1(2000)
