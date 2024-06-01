#Task = summarise the number of imports and exports per month for each port
    #This table only has imports in it for some reason, so have only looked at them
#Step 1: Import the data - see what's going on
#Step 2: Make a month column from the date column
#Step 3: Slice subset of just port, month, and quantity so that it is easier to work with
#Step 4: Make a pivot table to show the sum of import quantity by month for each port

#admin
import pandas as pd
data = pd.read_csv('lemis_partial.csv')
#summarising the data
data.info()
print(data.columns)
#Some general summaries because I am practising
print(data[["quantity", "value"]].median())
print(data[["quantity", "value"]].mean())
print("The mean of the quantity by taxonomic group is:\n",
      data[["quantity", "taxa"]].groupby("taxa").mean())
print("The mean of the value by taxonomic group is:\n",
      data[["value", "taxa"]].groupby("taxa").mean())
#slice month from the date column and make a new column
data["month"] = data.disposition_date.str[3:5]
print(data.columns)
#slice month, port, quantity int new subset to make it easier to look at
subset = data[['port','month','quantity','unit']]
print(subset)
print("The number of imports reported as different units are:\n",
      data[["quantity", "unit"]].groupby("unit").count())
#print(subset[["month", "port","quantity"]].groupby("month").sum('quantity'))
#print(subset.groupby('month','port')['quantity'].agg(['sum','count']))
table = pd.pivot_table(subset, values =['quantity'],index=['port'],
                       columns=['month'], aggfunc=['count'])
#There are a lot of different units which are not comparable (e.g. number, kg), so to get an idea of quantity we have to restrict to just imports of whole animals
subset_no = subset[(subset["unit"] == 'NO')]
table_no = pd.pivot_table(subset, values =['quantity'],index=['port'],
                       columns=['month'], aggfunc=['sum'])
print(subset_no)
print(table)
print(table_no)






