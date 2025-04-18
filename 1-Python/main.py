# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:28:14 2025

@author: maith
"""

#main.py
from salary import calculate_salary
from validation import validate_experience,validate_role
from display import display_salary

def main():
    try:
        name=input("Enter employee name: ")
        experience=int(input("Enter years of experience: "))
        role=input("Enter job role(Intern,Junior,Mid-Level,Senior,Manager)")
        
        #Validate inputs
        experience=validate_experience(experience)
        role=validate_role(role)
        
        #Calculate salary
        salary=calculate_salary(experience,role)
        
        #display
        display_salary(name,experience,role,salary)
        
    except ValueError as e:
        print(f"Error(e)")
        
