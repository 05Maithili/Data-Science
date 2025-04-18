# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:35:13 2025

@author: maith
"""

'''
Scenario 
Imagine a customer support team where new tickets
are assigned to available agents in a round-robin manner.
Each agent should receive the next ticket in sequence.
If the last agent is reached, the cycle should restart
from the first agent automatically.
'''
import itertools

# List of available support agents
agents= ["Alice", "Bob","Charlie","David"]

# Create a cycling iterator over  the agents
agent_cycle = itertools.cycle(agents)

# Stimulate incoming support tickets
tickets = ["Ticket-101","Ticket-102", "Ticket-103","Ticket-104","Ticket-105","Ticket-106"]

#Assign tickets to agents in a round-robin manner
assignments = {ticket: next(agent_cycle) for ticket in tickets}

# Print the assignments
for ticket, agent in assignments.items():
    print(f"{ticket} -> Assigned to: {agent}")

#