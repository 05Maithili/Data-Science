# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:20:15 2025

@author: maith
"""

import csv

def process_transaction(transaction):
    """dummy function to stimulate processing a transaction"""
    if "ERROR" in transaction[2]:
        # Stimulate an error for some transactions
        raise ValueError("Transaction failed!")
    return f"Processed transaction: {transaction}"

# Open and read the CSV file
with open("E:/1-Python/transaction.csv", "r") as file:
     reader = csv.reader(file)
     next(reader) #Skip the header
     
     for index, transaction in enumerate(reader,start =1):
         try:
             result = process_transaction(transaction)
             print(f"Row {index}: {result}")
         except ValueError as e:
             print(f" Error at Row {index}: {e}")
    