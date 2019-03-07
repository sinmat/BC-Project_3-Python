
import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")
#print(csvpath)

with open(csvpath, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")

	months = -1
	total = 0
	av = 0
	profit_loss = []
	Months = []
	profit_loss_last_month = 0
	profit_loss_diff = []
	
	for row in csvreader:
		months += 1

		if months == 0:
			continue

		total = total + int(row[1])
		av = total/months
		profit_loss.append(int(row[1]))
		Months.append(str(row[0]))
		profit_loss_diff.append(int(row[1]) - profit_loss_last_month)
		profit_loss_last_month = int(row[1])

	profit_loss_max = max(profit_loss_diff)
	profit_loss_min = min(profit_loss_diff)
	av = (profit_loss[-1] - profit_loss[0]) / (len(profit_loss)-1)
	
	

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}") 
print(f"Total: ${total}") 
print(f"Average: ${round(av, 2)}")
print(f"Greatest Increase in Profits: {Months[profit_loss_diff.index(profit_loss_max)]} (${profit_loss_max})")
print(f"Greatest Decrease in Profits: {Months[profit_loss_diff.index(profit_loss_min)]} (${profit_loss_min})")

#python /path/to/script/myscript.py > /path/to/output/myfile.txt