# Joshua Adrian O. Daet
# BSCpE 1-4
# Assignment 4 - Problem 3

import random

def write():
    # open mylife.txt and put the write function to it
    try:
        with open("C:/assignments_oop/A4-Problem3/mylife.txt", "w") as my_life:
            while True:
                 # put a variable to where the user will input their lines
                line = input("Enter a line (press Enter to exit): ")

                # exit the loop if the user presses Enter
                if not line:
                    break