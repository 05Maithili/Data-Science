# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 08:22:43 2025

@author: maith
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fdata = pd.read_csv(r"E:\2-Python\fdata.csv")
fdata.columns = ["date","open","high","low","close"]

# Histogram
plt.hist(fdata.date, bins = 20, edgecolor="black", alpha=0.6)
plt.title("Date Distribution")
plt.xlabel("Date")
plt.ylabel("Frequency")
plt.show()

# Scatter