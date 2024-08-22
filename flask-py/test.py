import numpy as np
import pandas as pd
def welcome(name: str) -> None: # the use of : and -> are for type hinting, leting others know what to expect from the function
    #age = 24
    name = input("Please enter your name: ").lower()
    print("Welcome to VS Code {}".format(name))


# welcome(name)


class MathOperation():
    all_time_favorite_number = 9

    def __init__(self, favorite_number):
        self.favorite_number = favorite_number

    def get_favorite_num(self):
        return self.favorite_number

    @classmethod
    def update_favorite_number(cls, new_num):
        cls.all_time_favorite_number = new_num

    @staticmethod
    def add(*args: int) -> int:
        sum = 0
        for arg in args:
            sum += arg
        return sum
    
    @staticmethod
    def subtract(*args: int) -> int:
        sum = args[0]
        for arg in args[1:]:
            sum -= arg
        return sum
    
    @staticmethod
    def multiply(*args: int) -> int:
        sum = 1
        for arg in args:
            sum *= arg
        return sum
    
    @staticmethod
    def divide(*args: int) -> int:
        pass

ops = MathOperation(11)

print(ops.add(1,2,3,4,5,6,8))
print(ops.subtract(4,7,6))
print(ops.multiply(4,7,6))

print(ops.get_favorite_num())
print(ops.all_time_favorite_number)