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

#Calculate the number of months in the data
Total_Months = len(number_months)

#Calculate the sum of profits
Total_Amount = sum(profit)

#Calculate de Differences between each month and then the average change
Differences = [profit[n]-profit[n-1] for n in range(1,len(profit))]
Average_Change = round(sum(Differences)/len(Differences),2)

#Calculate the greatest increase in losses
Max_Increase = max(Differences)

#Obtain the index of the greatest loss to get the month of the year
index1= Differences.index(Max_Increase)
month_max_profit = number_months[index1+1]

#Calculate the minimum increase in losses
Max_Decrease = min(Differences)

#Obtain the index of the greatest loss to get the month of the year
index2= Differences.index(Max_Decrease)
month_min_profit = number_months[index2+1]

combined_list = zip(number_months,profit,Differences)
list(combined_list)

#Print all analysis to terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {Total_Months}" )
print(f"Total: ${Total_Amount}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {month_max_profit} (${Max_Increase})")
print(f"Greatest Decrease in Profits: {month_min_profit} (${Max_Decrease})")

#Export Data to TXT FILE inside Analysis Folder
txtpath = os.path.join( 'Analysis', 'financial_analysis.txt')
f=open(txtpath,"w+")
f.write("Financial Analysis\r\n")
f.write("---------------------\r\n")
f.write(f"Total Months: {Total_Months}\r\n" )
f.write(f"Total: ${Total_Amount}\r\n")
f.write(f"Average Change: ${Average_Change}\r\n")
f.write(f"Greatest Increase in Profits: {month_max_profit} (${Max_Increase})\r\n")
f.write(f"Greatest Decrease in Profits: {month_min_profit} (${Max_Decrease})\r\n")
f.close()