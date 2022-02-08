#!/usr/bin/env python3

# Description: This program calculates Fahrenheit to Celsius or visa versa
# GitHub URL: https://github.com/dejohns2/CSC365_Spring2022_Assignments.git
# Programmer: Debbie Johnson
# Date: 2022.02.08

DASH_LINE_LENGTH = 60  # used to have a standard dash line length

# display a welcome message
print('Welcome to the Temperature Calculator')

# keep looping until the user enter's "n" for no
while True:

    # display the conversion options
    print('=' * DASH_LINE_LENGTH)
    print('Enter F to convert from Fahrenheit to Celsius.')
    print('Enter C to convert from Celsius to Fahrenheit.')

    # loop until the user enters f or c
    while True:
        user_input = input('Enter the conversion type (F,C): ')
        temp_type = user_input[0].lower()
        if temp_type in ['f', 'c']:
            break
        else:
            print("Invalid input!")

    # separate the conversion type prompt from the remanding prompts
    print('=' * DASH_LINE_LENGTH)
    print()

    # loop until the user enters a valid starting temperature
    while True:
        temp_start = int(input(f'{"Enter the starting temperature (-50 to 150)":.<45s}: '))
        if -50 <= temp_start <= 150:
            break
        else:
            print("Invalid input!")

    # loop until the user enters a valid stopping temperature
    while True:
        temp_stop = int(input(f'{"Enter the stopping temperature (-50 to 150)":.<45s}: '))
        if -50 <= temp_stop <= 150:
            break
        else:
            print("Invalid input!")

    # loop until the user enters a valid stepping temperature
    while True:
        temp_step = int(input(f'{"Enter the stepping temperature (-50 to 50)":.<45s}: '))
        if -50 <= temp_step <= 50:
            break
        else:
            print("Invalid input!")

    # display the table column headings
    print()
    print("|=====|=====|")
    if temp_type == 'f':
        print("|  F  |  C  |")
    else:
        print("|  C  |  F  |")
    print("|=====|=====|")

    # display the temperature conversion chart
    for temp in range(temp_start, temp_stop + 1, temp_step):
        if temp_type == 'f':
            temp_conv = (temp - 32) * 5 / 9  # convert F to C
        else:
            temp_conv = temp * 9 / 5 + 32    # convert C to F

        # display the temps in a column width of 3 with no decimal places
        print(f'| {temp:3.0f} | {temp_conv:3.0f} |')

    # display the closing lines of the conversion chart
    print("|=====|=====|")
    print()

    # keep looping until the user enters y or n
    while True:
        user_input = input("Do you want to display another temperature chart (y/n)? ")
        if user_input[0].lower() in ['y', 'n']:
            break
        else:
            print("Invalid input!")

    # if the user enters n, break out of the loop and end the program
    if user_input[0].lower() == 'n':
        break
    else:
        print()

# display the program closing
print()
print('=' * DASH_LINE_LENGTH)
print()
print("Bye!")
