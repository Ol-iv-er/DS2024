#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:50:37 2024

@author: oliver
"""

## Vulture find unused code and dead code

import os
import time
import numpy as np

class Greeter():
    def greet(self):
        print('Hi')

def hello_world():
    message = "Hello World"
    greeter = Greeter()
    greet_func = getattr(greeter, "greet")
    greet_func()
    
    
if __name__ == "__main__":
    hello_world()