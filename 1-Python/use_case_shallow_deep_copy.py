# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:07:22 2025

@author: maith
"""

import copy

report_template = {
    "name":"",
    "scores":[0,0,0],
    "remarks":"Pending"
    }

# Shallow copy for a new student
student1_report = copy.copy(report_template)
student1_report["name"] ="Alice"
student1_report["scores"][0] = 85

print(report_template["scores"]) # Output: [85, 0,0] (unexpected)
########################################## 
import copy

report_template = {
    "name":"",
    "scores":[0,0,0],
    "remarks":"Pending"
    }

# Deep copy for complete isolation
student1_report = copy.deepcopy(report_template)
student1_report["name"] = "alice"
student1_report["scores"][0] = 85

print(report_template["scores"]) # Output:[0, 0, 0]

############################################
import copy

params = {
    "layers":[64,128,256],
    "activation":"relu"
    }

experiment1 = copy.deepcopy(params)
experiment2 = copy.deepcopy(params)

experiment1["layers"][0] = 32

print(params["layers"]) # No changes in base params
print(experiment1["layers"])
############
# use case of filter
users = [
    {"name":"Alice", "role":"admin"},
    {"name":"Bob", "role":"editor"},
    {"name":"Charle","role":"admin"},
    ]

admins = list(filter(lambda user: user["role"] == "admin", users))
print(admins)