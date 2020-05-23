import os
import pandas as pd
data = pd.read_csv("Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
data.head()
data.tail()
import datetime
end_date=datetime.datetime(2017, 2, 1)
start_date=datetime.datetime(2010, 1, 1)

num_month=(end_date.year-start_date.year)*12+(end_date.month-start_date.month)+1

print("Total month:", num_month)

print
