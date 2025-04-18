# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:08:44 2025

@author: maith
"""

import time
file_path='E:/1-Python/server.log'
def tail_log_file(file_path):
    """Generator that continously reads new lines from a logged"""
    with open(file_path,"r") as file:
        file.seek(0,2) # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1) # Wait for new logs to be added
                continue
            yield line.strip() # Yield new log line
            
# Example Usage: Process logs as they come in
for log in tail_log_file(file_path):
    if "ERROR" in log:
        print(f"Alert: {log}") #Trigger alert for error logs
          