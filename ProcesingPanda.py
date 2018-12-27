# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:49:33 2018

@author: vicser
"""

import pandas as pd
import numpy as np


dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.csv', sep=',')
print(dataFrame)

dataFrame['DIFF']=dataFrame['MAX']-dataFrame['MIN']

print(dataFrame)
dataFrame['DIFF_Min'] = dataFrame['TEMP'] - dataFrame['MIN']

# Create a new column and convert temp fahrenheit to celsius:
dataFrame['TEMP_Celsius'] = (dataFrame['TEMP'] - 32) / (9/5)


print(dataFrame)


# Select first five rows of dataframe

w_temps = dataFrame.loc[dataFrame['YEARMODA'] >= 20160615]
print(w_temps)

w_temps2 = dataFrame.loc[(dataFrame['TEMP_Celsius'] > 15) &(dataFrame['YEARMODA'] >= 20160615)]
print(w_temps2)

w_temps2 = w_temps2.reset_index(drop=True)
print(w_temps2)
w_temps3=w_temps2;

# Set temp_celsius as none in the first five rows
w_temps3.loc[:4, 'TEMP_Celsius'] = None
print(w_temps3)

# Drop no data values based on temp_celsius column
w_temps_clean = w_temps3.dropna(subset=['TEMP_Celsius'])
#w_temps_clean = w_temps2.fillna(0)

print(w_temps_clean.reset_index(drop=True))


# Sort dataframe, ascending
sorted_temp_a = dataFrame.sort_values(by='TEMP', ascending=False)

print(sorted_temp_a)

# Create new column, and round celsius values
dataFrame['Celsius_rounded'] = dataFrame['TEMP_Celsius'].round(0)
print(dataFrame)

# Get unique celsius values
unique = dataFrame['Celsius_rounded'].unique()
print(list(unique))


# define output filename
output_fp = "Kumpula_temps_June_2016.csv"

# Save dataframe to csv
dataFrame.to_csv(output_fp, sep=',', index=False, float_format="%.2f")

# Specify output filename
excel_output_fp = "Kumpula_temps_above15_June_2016.xlsx"

# Initialize ExcelWriter
writer = pd.ExcelWriter(excel_output_fp)

#Write data to excel
w_temps.to_excel(writer, sheet_name="Kumpula_temperatures", index=False, float_format="%.1f")













s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

