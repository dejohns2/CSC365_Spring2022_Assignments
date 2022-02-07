#!/usr/bin/env python3

import tkinter as tk

'''''
  Name: Salary Calculator
  Programmer: Alex Ocegueda -> Git: https://github.com/AlexOcegueda/Salary_Calculator
  Version: 1.0
  Description: Takes in your Salary per hour, total hours worked per week, how many days you work, and 
                your holidays and vacations. It will display your salary before and after holidays are 
                deducted.
'''''


def calculate_unadjusted_salary(salary, total_hours_per_week, days_per_week):
    # hours worked on an average day
    daily_hours = int(total_hours_per_week) / int(days_per_week)

    # This assumes 5 working day schedule for the year
    working_days_per_year = 52 * int(days_per_week)

    unadjusted_salary = int(salary) * int(daily_hours) * int(working_days_per_year)

    return unadjusted_salary


def calculate_adjusted_salary(salary, total_hours_per_week, days_per_week, holidays, vacations):
    # hours worked on an average day
    daily_hours = int(total_hours_per_week) / int(days_per_week)

    # This assumes 5 working day schedule for the year
    working_days_per_year = 52 * int(days_per_week)

    adjusted_days_off = int(working_days_per_year) - (int(holidays) + int(vacations))

    adjusted_salary = int(salary) * int(daily_hours) * int(adjusted_days_off)

    return adjusted_salary


# Calculates their unadjusted salary and adjusted salary and displays it on screen
def calculate(salary, total_hours_per_week, days_per_week, holidays, vacations, root):
    adjusted_salary_label = tk.Label(root, text="Your adjusted salary is")
    adjusted_salary = tk.Label(root,
                               text=calculate_adjusted_salary(salary, total_hours_per_week, days_per_week, holidays,
                                                              vacations))
    unadjusted_salary_label = tk.Label(root, text="Your unadjusted salary is")
    unadjusted_salary = tk.Label(root, text=calculate_unadjusted_salary(salary, total_hours_per_week, days_per_week))

    adjusted_salary_label.pack()
    adjusted_salary.pack()
    unadjusted_salary_label.pack()
    unadjusted_salary.pack()


root = tk.Tk()
root.title("Salary Calculator")
root.geometry("300x300")

# Takes in amount of Salary
salary_label = tk.Label(root, text="Salary per Hour")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

# Takes in amount of hours per week
total_hours_per_week_label = tk.Label(root, text="Hours per Week")
total_hours_per_week_label.pack()
total_hours_per_week_entry = tk.Entry(root)
total_hours_per_week_entry.pack()

# Takes in amount of days per week
days_per_week_label = tk.Label(root, text="Days per Week")
days_per_week_label.pack()
days_per_week_entry = tk.Entry(root)
days_per_week_entry.pack()

# Takes in amount of holiday days off
holiday_label = tk.Label(root, text="Holiday per year")
holiday_label.pack()
holiday_entry = tk.Entry(root)
holiday_entry.pack()

# Takes in amount of vacation days off
vacations_days_label = tk.Label(root, text="Vacation days per year")
vacations_days_label.pack()
vacation_days_entry = tk.Entry(root)
vacation_days_entry.pack()

calculate_button = tk.Button(root, text='Calculate',
                             command=lambda: calculate(salary_entry.get(), total_hours_per_week_entry.get(),
                                                       days_per_week_entry.get(), holiday_entry.get(),
                                                       vacation_days_entry.get(), root))
calculate_button.pack()

root.mainloop()




