#!/usr/bin/env python3
import csv

my_file_name = 'test.csv'

my_output_data = [
    [1, 'Johnson, Debbie', [10.1, 20.25, 30.0, 40.0]],
    [4, 'Book, Mac', [11.13, 30.5, 66.1, 43.1]],
    [33, 'Bear, Teddie', [10.14, 24.2, 32.3, 3.0]]
]

my_input_data = []


def print_report(my_data):
    """
    Display the 3D list
    :param my_data multi-dimensional list
    :return no value
    """

    if len(my_data) == 0:
        print('There are no data in the list.')
        return

    for record in my_data:
        student_id, student_name, student_grades = record
        print(f'Student ID # {student_id} {student_name} grades: ')
        print('    ', end='')
        for grade in student_grades:
            print(f'{grade:>3.2f}', end=' | ')
        print()

    print()


with open(my_file_name, 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    writer.writerows(my_output_data)

temp1 = []
with open(my_file_name, 'r', newline='') as file_object:
    reader = csv.reader(file_object)
    for row in reader:
        temp1.append(row)

for row in temp1:
    grades_str = row[2][1:-1]
    grades_list_str = grades_str.split(', ')
    temp2 = []
    for i in grades_list_str:
        temp2.append(float(i))
    my_input_data.append([int(row[0]), row[1], temp2])

print_report(my_output_data)
print_report(my_input_data)
