# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:38:01 2025

@author: maith
"""

def validate_experience(exp):
    '''Validate that experience is a non-negative integer'''
    if not isinstance(exp,int) or exp <0:
        raise ValueError("Experience must be a non-negative integer")
    return exp

def validate_role(role):
    '''Validate job role'''
    valid_roles={"Intern","Junior","Mid-Level","Senior","Manager"}
    if role not in valid_roles:
        raise ValueError(f"Invalide {role} Choose From {valid_roles}")
    return role    