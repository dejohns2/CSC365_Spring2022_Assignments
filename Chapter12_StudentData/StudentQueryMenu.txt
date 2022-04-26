#!/usr/bin/env python3
"""
This module contains the functions for displaying the main menu and running the menu options
"""

import queries

__author__ = "Debbie Johnson"
__version__ = "1.0"
_date__ = "2020.11.05"


def display_menu():
    """
    Displays a list of all the valid main menu options
    It also handles for nonnumerical data and invalid menu option selected.
    :return: no value
    :rtype: none
    """
    print('Student Data Queries')
    print('===========================')
    print('1 - Students Information')
    print('2 - All Sports List')
    print('3 - Each Class Genders')
    print('4 - Sue Smith Class List')
    print('5 - Student in Science not Math')
    print('6 - NonSports Groups')
    print('7 - All Season Sports Students')
    print('8 - Students Classes same as Sue Smith')
    print('9 - Student with Low Grades')
    print('0 - Exit program')
    print()

    return


def main():
    """
    Main keeps the program looping until the user enters 0 to exit the program
    then based on the user's selected, will call the corresponding function option

    :return: no value
    :rtype: none
    """

    while True:
        display_menu()

        try:  # the try is used to catch non numeric data
            menu_num = int(input('Please enter a Menu # '))
            if menu_num == 1:
                queries.student_information()
            elif menu_num == 2:
                queries.all_sports_list()
            elif menu_num == 3:
                queries.each_class_genders()
            elif menu_num == 4:
                queries.sue_smith_class_list()
            elif menu_num == 5:
                queries.students_in_science_not_math()
            elif menu_num == 6:
                queries.non_sports_groups()
            elif menu_num == 7:
                queries.all_seasons_sports_students()
            elif menu_num == 8:
                queries.student_classes_same_as_sue_smith()
            elif menu_num == 9:
                queries.students_with_low_grades()
            elif menu_num == 0:
                break
            else:
                print('Not a valid menu option.')

            print()
            input("Press Enter to continue...")
            print()

        except ValueError:  # catch the error if the user entered nonnumeric data
            print('Please enter a number between 0 and 6.')
            input("Press Enter to continue...")
            print()

    print('Bye!')

    return


if __name__ == "__main__":  # if this is the module where the program started from, then run the main function
    main()
