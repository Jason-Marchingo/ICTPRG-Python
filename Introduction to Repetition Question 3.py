# Write a program that keeps asking a user for a number
# Tell the user if their number is within a range 50 and 70
# Written By: Jason Marchingo
# Date: 06.09.2020

# Asks the user to enter a number, and then stores that number
number = int(input("Enter a number: "))

# Will check if the entry by the user is between 50 and 70
while number not in range(50,70):
# If it is not within the range, it will tell the user.
    print("Your entry is not within the range.")
    number= int(input("Enter a number: "))
# If it is within the range, it will tell the user, and stop the program.
print("Your entry is within the range.")