#!/usr/bin/env python

class A:
    interest: float = 0.05
    number: int
    def __init__(self) -> None:
        self.number = 0
        self.interest = 0.1
    
    @classmethod
    def get_interest(cls) -> float:
        #print(cls.number)
        return cls.interest
    
a=A()
print(a.get_interest()) # output is 0.05, __init__() is not called for class method

# write a decorator to call __init__() for class method
def call_init(func):
    def wrapper(*args, **kwargs):
        args[0].__init__()
        return func(*args, **kwargs)
    return wrapper