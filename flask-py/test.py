import numpy as np
import pandas as pd
def welcome(name):
    print("Welcome to VS Code {}".format(name))

name = input("Please enter your name: ").lower()

welcome(name)