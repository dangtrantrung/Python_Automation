#[sequence 1 to 900000]
import sys


def mygenerator(n):
    for x in range(n):
        yield x**3
values=mygenerator(10000)
print(type(values))
print(sys.getsizeof(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

#infinite sequence
def infinite_sequence():
    result=1
    while True:
        yield result
        result*=5
values=infinite_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))