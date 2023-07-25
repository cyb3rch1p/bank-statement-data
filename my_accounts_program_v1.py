#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 16:23:17 2023

@author: admin
"""

import pandas as pd
import numpy as np

# read a csv file
bs = pd.read_csv('feb_2022_bs.csv', index_col=False)
pd.options.display.max_rows = 350

print(bs.to_string())

bs["Debit Amount"].fillna(0.0, inplace = True)
bs["Credit Amount"].fillna(0.0, inplace = True)
bs["Transaction Type"].fillna('OSC', inplace = True)


# this works, now to remove the m hart transfers and other irrelevant data
not_zero = bs[(bs['Debit Amount'] > 0) & (bs['Transaction Description'] != 'M HART')
              & (bs['Transaction Type'] != 'TFR') & (bs['Transaction Description'] != 'ADELE WEEKLY') & (bs['Transaction Description'] != 'SAVE THE CHANGE')
              & (bs['Transaction Description'] != 'MANSELTON STORES') & (bs['Transaction Description'] != 'Netflix.com')]
print(not_zero[['Transaction Description', 'Debit Amount']])

print('Total for Month: ', not_zero['Debit Amount'].aggregate(np.sum))
