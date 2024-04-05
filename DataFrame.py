import pandas as pd 
import numpy as np

dataFrame = pd.read_csv("C:\\Users\\iti\\Desktop\\Employees.csv")
print("Our DataFrame....",dataFrame)


dataFrame.drop_duplicates(inplace=True)
print(dataFrame)

dataFrame['Age'] = dataFrame['Age'].round()
print(dataFrame)

conversion_rate = 47.38
dataFrame['Salary(EGP)'] = dataFrame['Salary(USD)'] * conversion_rate
print(dataFrame)

average_age = dataFrame['Age'].mean()
print("Average age:", average_age)

median_salary = dataFrame['Salary(EGP)'].median()
print("Median salary:", median_salary)


gender_ratio = dataFrame['Gender'].value_counts(normalize=True)
print("Ratio between males and females:")
print(gender_ratio)
     



