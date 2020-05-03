# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:49:17 2020

@author: Lenovo
"""

import time

start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0
while True:

    ##################
    # your code here #
    ##################

    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()