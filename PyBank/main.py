import os
import csv
path = os.path.join("budget_data.csv")

with open(path) as budget_data:
    # using the csv.reader method to read the data
    reader = csv.reader(budget_data)
    # skipping the first row because it's not valuable for our analysis
    header = next(reader)
    # set a counter before the for loop, put it inside the for loop and let it add 1 at every iteration
    Total_month = 0
    for row_of_data in reader:
        #print(row_of_data[2])  
          Total_month += 1
          import pandas as pd
          df=pd.read_csv("budget_data.csv")

df.head()

x=0
for i in df['Profit/Losses']:
    x+=i
print(x)

df['PPl']= df['Profit/Losses'].shift(1)
df.head()

df['PC']=df['Profit/Losses']-df['PPl']
df.head()

Total_PC=df['PC'].sum()
Total_PC

AVG_change= Total_PC/(Total_month-1)
AVG_change

Greatest_increase_index= df['PC'].idxmax()
Greatest_increase_index

Greatest_increase= df['PC'][df['PC'].idxmax()]
Greatest_increase

Greatest_increase_date = df['Date'][25]
Greatest_increase_date

Greatest_decrease_index= df['PC'].idxmin()
Greatest_decrease_index

Greatest_decrease_date = df['Date'][44]
Greatest_decrease_date

Greatest_decrease= df['PC'][df['PC'].idxmin()]
Greatest_decrease

print ("Total Month is :",Total_month)

print(f"Greatest Increase in Profits: {Greatest_increase_date} (${str(Greatest_increase)})")

print(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${str(Greatest_decrease)})")
