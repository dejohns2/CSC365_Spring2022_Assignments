"""
Chapter 6 Assignment

Student Data System for managing student information (student id, first name, and last name)

This module contains the functions for displaying the main menu and running the menu options
"""

import student_maintenance as sm  # module with add, update, delete, etc logic
import validation as v

__author__ = "Debbie Johnson"
__version__ = "1.0"
__date__ = "2021.10.21"


def display_menu():
    """
    Displays a list of all the valid main menu options
    It also handles for nonnumerical data and invalid menu option selected.

    1 - List all students
    2 - Add a student
    3 - Update a student
    4 - Delete a student
    0 - Exit program

    :return no value
    :rtype none
    """

    print('Student Records Menu')
    print('======================')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')
    print()

    return


def main():
    """
    Main keeps the program looping until the user enters 0 to exit the program
    then based on the user's selected, will call the corresponding function option
    Local scoped students is a 2D list that is pass as an argument to each menu option function
    Local scoped max_student_id is the last student id used, and is passed to the add_student function,
    and this function will return the last added student id

    :return no value
    :rtype none
    """

    students = []  # 2D list of student data (student id, first name, last name)
    next_student_id = 1

    while True:
        display_menu()

        menu_num = v.get_range('Please enter a Menu #', 0, 4)
        print()
        if menu_num == 1:
            sm.list_students(students)
        elif menu_num == 2:
            sm.add_student(students, next_student_id)
            next_student_id += 1
        elif menu_num == 3:
            sm.update_student(students)
        elif menu_num == 4:
            sm.delete_student(students)
        elif menu_num == 0:
            break
        else:
            print('Not a valid menu option.')

        input("Press Enter to continue...")
        print()

    print('Bye!')

    return


if __name__ == "__main__":  # if this is the module where the program started from, then run the main function
    # help('main_menu')
    main()
