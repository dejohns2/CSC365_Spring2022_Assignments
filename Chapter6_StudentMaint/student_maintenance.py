#!/usr/bin/env python3

"""
Chapter 6 Assignment
This module contains the functions for adding, updating, and deleting student data
"""

import validation as v

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__date__ = '2022.03.24'
__status__ = 'Development'


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :param next_student_id: the next student id to be used for the add function
    :type next_student_id: int

    :return no value
    :rtype none
    """

    print('Add Student')
    print('-----------')
    first_name = v.get_string('Please enter the Student\'s First Name').title()
    last_name = v.get_string('Please enter the Student\'s Last Name').title()

    students.append([next_student_id, first_name, last_name])

    print()
    print(f'Student ID #{next_student_id} {first_name} {last_name} was added.')

    return


def update_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be updated from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to update the selected student, and then let the user know
    if the user was successfully updated.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """

    print('Update Student')
    print('--------------')

    if len(students) == 0:
        print('There are no students in the list.')
        return

    student_id = v.get_positive_num('Please enter the Student ID to be updated')

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} was not found.')
        return

    student_id, first_name, last_name = students[student_index]

    if not v.get_yes_no(f'Do you want to update Student ID #{student_id} {first_name} {last_name}'):
        print('Student update cancelled!')
        return

    new_first_name = input(f'Please enter the Student\'s First Name or press enter to keep {first_name}: ').title()
    if new_first_name > '':
        students[student_index][1] = new_first_name
    else:
        new_first_name = first_name

    new_last_name = input(f'Please enter the Student\'s Last Name or press enter to keep {last_name}: ').title()
    if new_last_name > '':
        students[student_index][2] = new_last_name
    else:
        new_last_name = last_name

    print()
    if first_name == new_first_name and last_name == new_last_name:
        print('Student\'s name was not changed. Update was cancelled.')
    else:
        print(f'Student ID #{student_id} {first_name} {last_name} was update to {new_first_name} {new_last_name}')

    return


def delete_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be deleted from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to delete the selected student, and then let the user know
    if the user was successfully deleted.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """

    print('Delete Student')
    print('--------------')

    if len(students) == 0:
        print('There are no students in the list.')
        return

    student_id = v.get_positive_num('Please enter the Student ID to be deleted')

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} was not found.')
        return

    student_id, first_name, last_name = students[student_index]

    if not v.get_yes_no(f'Please confirm deleting Student ID #{student_id} {first_name} {last_name}'):
        print('Student delete cancelled!')
    else:
        students.pop(student_index)
        print(f'Student ID #{student_id} {first_name} {last_name} was deleted.')

    return


def list_students(students):
    """
    Display the all student information stored in a 2D list (id, first name, last name)
    It will notify the student if there is no data found.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """

    if len(students) == 0:
        print('There are no students in the list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s}')
    print('=' * 4, '=' * 15, '=' * 15)

    for student in students:
        student_id, first_name, last_name = student
        print(f'{student_id:>4d} {first_name:<15s} {last_name:<15s}')

    return


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.

    CODE EXAMPLE:
    for student in students:
        if student_id in student:
            return students.index(student)
    return -1

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param student_id: student id that they user wants to find
    :type student_id: int

    :return the index of the student in the 2D list or -1 if not found
    :rtype int
    """

    for student in students:
        if student_id == student[0]:
            return students.index(student)

    return -1


if __name__ == '__main__':  # if this is the module where the program started from, then run the main function
    help('student_maintenance')
