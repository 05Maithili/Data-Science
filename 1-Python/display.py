# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:18:06 2025

@author: maith
"""

#display.py
def display_salary(name,experience,role,salary):
    print("\n== Salary Details ==")
    print(f"Employee name: {name}")
    print(f"Role: {role}")
    print(f"Experience: {experience} years")
    print(f"Calculated Salary: ${salary:,.2f}")
    print("============")