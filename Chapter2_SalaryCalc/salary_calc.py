#!/usr/bin/env python3

# Description: This program calculates annual salary based on hours
# GitHub URL:
# Programmer: Debbie Johnson
# Date: 2022.01.26

DASH_LINE_LENGTH = 35  # used to have a standard dash line length

# display a welcome message
print('The Salary Calculator program')
print('=' * DASH_LINE_LENGTH)

# get input from the user
salary_per_hour = float(input('Salary per hour:\t\t'))
hours_per_week = float(input('Hours per Week:\t\t\t'))
days_per_week = float(input('Days per Week:\t\t\t'))
holiday_per_year = float(input('Holidays per Year:\t\t'))
vacation_per_year = float(input('Vacation Days per Year:\t'))

# calculate annual salary and adjusted annual salary
workday_per_year = 52 * days_per_week
adj_workday_per_year = workday_per_year - (holiday_per_year + vacation_per_year)
hours_per_day = (hours_per_week / days_per_week)
annual_salary = round(workday_per_year * hours_per_day * salary_per_hour, 2)
adj_annual_salary = round(adj_workday_per_year * hours_per_day * salary_per_hour, 2)

# display the result
print('=' * DASH_LINE_LENGTH)
print('Unadjusted Salary:      $', annual_salary)
print('Adjusted Annual Salary: $', adj_annual_salary)
print('=' * DASH_LINE_LENGTH)
print('Goodbye!')
