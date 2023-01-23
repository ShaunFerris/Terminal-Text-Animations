'''Currently testing a function to animate a string to indicate loading with cycling elipses - completed
also added binary wipe
need to double check that I have finished adding functionality to all looping animations to allow them to be interrupted by 
the script they're called in'''


import time, sys, shutil, random,  os
from textanima import loading_dots, clear_line

test = 0
print('Loading', end='', flush=True)
while test < 2:
    loading_dots(1)
    test += 1
clear_line()
print('Done!')
