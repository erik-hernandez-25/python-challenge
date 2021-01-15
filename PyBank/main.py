# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')
number_months = []
profit = []
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #Months
        number_months.append(row[0])
        profit.append(int(row[1]))

Total_Months = len(number_months)
Total_Amount = sum(profit)
print(f"Total Months: {Total_Months}" )
print(Total_Amount)

