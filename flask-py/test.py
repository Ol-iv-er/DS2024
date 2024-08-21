import numpy as np
import pandas as pd
def welcome(name: str) -> None: # the use of : and -> are for type hinting, leting others know what to expect from the function
    print("Welcome to VS Code {}".format(name))
age = 24
name = input("Please enter your name: ").lower()

welcome(name)