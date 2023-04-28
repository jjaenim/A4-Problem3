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

                # to write a new line on the file
                my_life.write(line + "\n")

                # ask the user if they want to enter another line
                choices = input("Do you want to enter another line? (y/n): ")

                # make a comment
                if choices == "n":
                    print("")
                    comments = ["You're doing great", "Great job!", "That was great!", "Impressive!"]
                    print(random.choice(comments))
                    print("")
                    print("Thank you for using")
                    break
                elif choices != "y":
                    print("Invalid input. Please enter 'y' or 'n'.")

                    # do a while loop to ask the user repeatedly
                while choices == "y":
                    print("")
                    line = input("Enter a line:")

                    # to write a new line on the file
                    my_life.write(line + "\n")

                     # ask again the user if they want to continue
                    choices = input("Do you want to enter another line? (y/n):")