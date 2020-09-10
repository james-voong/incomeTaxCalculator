#!/usr/bin/env python3
import sys

'''
These rates are correct at 10/09/2020

Income tax
0-14000         10.5%
14001-48000     17.5%
48001-70000     30%
70000+          33%

ACC Levy
0-130911        1.39%
130912+         0%
'''

def print_acc_levy(income):
    levy_limit = 130911
    levy_rate = 0.0139
    if income < levy_limit:
        print('{}{:.2f}'.format(
            "Acc Levy: ",
            round(income * levy_rate)
        ))
    else:
        print('{}{:.2f}'.format(
            "Acc Levy: ",
            round(levy_limit * levy_rate)
        ))

def print_cumulative_tax(cumulative_tax):
    print('{}{:.2f}'.format(
        "Income Tax Paid: ",
        round(cumulative_tax, 2)
    ))

def print_income(income):
    print('{}{:.2f}'.format(
        "Income: ",
        round(income, 2)
    ))

def print_percentage_paid_as_tax(income, cumulative_tax):
    print('{}{:.2f}%'.format(
        "Percentage paid as tax: ",
        round(cumulative_tax/income * 100, 2)
    ))

def print_all(income, cumulative_tax):
    print_income(income)
    print_acc_levy(income)
    print_cumulative_tax(cumulative_tax)
    print_percentage_paid_as_tax(income, cumulative_tax)
    exit

# Validation of arguments
if len(sys.argv) != 2:
    exit("Only give me one argument.")

income = sys.argv[1];

try:
    income = float(income)
except:
    exit("I only accept numbers.")

cumulative_tax = 0

# The first tax band.
tax_rate = 0.105
first_tax_band_limit = 14000

if income >= first_tax_band_limit:
    cumulative_tax += first_tax_band_limit * tax_rate
else:
    cumulative_tax += income * tax_rate
    print_all(income, cumulative_tax)

# The second tax band.
tax_rate = 0.175
second_tax_band_limit = 48000

if income >= second_tax_band_limit:
    cumulative_tax += (
        (second_tax_band_limit - first_tax_band_limit) * tax_rate
    )
else:
    cumulative_tax += (
        (income - first_tax_band_limit) * tax_rate
    )
    print_all(income, cumulative_tax)

# The third tax band.
tax_rate = 0.3
third_tax_band_limit = 70000

if income >= third_tax_band_limit:
    cumulative_tax += (
        (third_tax_band_limit - second_tax_band_limit) * tax_rate
    )
else:
    cumulative_tax += (
        (income - second_tax_band_limit) * tax_rate
    )
    print_all(income, cumulative_tax)

# The fourth tax band.
tax_rate = 0.33

cumulative_tax += (
    (income - third_tax_band_limit) * tax_rate
)
print_all(income, cumulative_tax)