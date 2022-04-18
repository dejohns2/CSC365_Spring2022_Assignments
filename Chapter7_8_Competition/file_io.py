#!/usr/bin/env python3

"""
Chapter 7 & 8 File I/O Competition Assignment
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__date__ = '2022.03.24'
__status__ = 'Development'

import csv
import re
import sys


def display_report(counters):
    valid_records, invalid_length, invalid_id, invalid_name, invalid_email, invalid_phone = counters

    total_records = valid_records + invalid_length + invalid_id + invalid_name + invalid_email + invalid_phone

    invalid_records = total_records - valid_records

    print(f'Total Records: {total_records}')
    print(f'Valid Records: {valid_records}')
    print(f'Invalid Records: {invalid_records}')
    print(f'        Length: {invalid_length}')
    print(f'        ID: {invalid_id}')
    print(f'        Name: {invalid_name}')
    print(f'        Email: {invalid_email}')
    print(f'        Phone: {invalid_phone}')


def process_file():
    valid_records = 0
    invalid_length = 0
    invalid_id = 0
    invalid_name = 0
    invalid_email = 0
    invalid_phone = 0

    # valid ids must only contain digits 0-9
    id_pattern = re.compile(r'[0-9]+')

    # valid emails must have an @ .edu domain suffix
    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.(edu)')

    # valid phone numbers must be 111-222-3333 pattern
    phone_pattern = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}')

    try:
        with open('input_file.csv', 'r', newline='') as input_file, \
                open('valid_file.csv', 'w', newline='') as valid_file, \
                open('invalid_file.csv', 'w', newline='') as invalid_file:

            reader = csv.reader(input_file, delimiter='|')
            valid_writer = csv.writer(valid_file, delimiter=',')
            invalid_writer = csv.writer(invalid_file, delimiter=',')

            for row in reader:

                invalid_data = ''

                try:
                    id, name, email, phone = row
                except:
                    invalid_length += 1
                    invalid_writer(['L', *row])

                try:
                    last_name, first_name = name.split(',')
                except:
                    invalid_data += 'N'

                if not re.search(id_pattern, id):
                    invalid_data += 'I'

                if not re.search(email_pattern, email):
                    invalid_data += 'E'

                if not re.search(phone_pattern, phone):
                    invalid_data += 'P'

                if invalid_data > '':
                    invalid_writer.writerow([invalid_data, *row])
                else:
                    valid_records += 1
                    phone = phone.replace('-', '.')
                    valid_writer.writerow([id, first_name, last_name, email, phone])

    except Exception as e:
        traceback.print_exception(*sys.exc_info())
        raise
    finally:
        return valid_records, invalid_length, invalid_id, invalid_name, invalid_email, invalid_phone


def main():
    print('Chapter 7 & 8 File I/O Competition')
    print('==================================')
    counters = process_file()
    display_report(counters)


# if this is the module where the program started from, then run the main function
if __name__ == '__main__':
    main()