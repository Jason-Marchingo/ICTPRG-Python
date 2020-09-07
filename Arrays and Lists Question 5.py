# Write a program that can accept many numbers from the user
# until the user enters a x
# Written by: Jason Marchingo
# Date: 07.09.2020

# Starting value for the number entered by user
number = None 
# List
Numbers = []

# If number is not 'x' 
while number != 'x':
# Ask the user to input a number
    number = input("Enter a number: ")

    if number != 'x':
# Converts number to an integer and then appends or adds number to the list
        Numbers.append(int(number)) 

# Outputs the list of numbers entered by user
print(Numbers)