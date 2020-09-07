# Write a program that counts from 0 to 25
# outputting each number on the same line, separated by commas.
# Written By: Jason Marchingo
# Date: 06.09.2020

# Empty Variable
value = ""

# Here we are checking and counting numbers between 0 and 25
# 0 and 26 are used because 0 counts as a number and we want all numbers between 0 and 25
for number in range(0, 26):
# Number is an integer which cannot be appended to a variable other than through a string
# We are appending number to the empty variable
    value += str(number)
# Checking if the last number is 25
# If it is not the last number it is adding a comma to ensure that there is no comma after the last number 
    if number != 25:
        value += ', '

# Outputting the string
print(value)