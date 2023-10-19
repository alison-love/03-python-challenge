#TEST

import os
import csv

# set variables
net_total = 0
profit_loss = []

greatest_increase = float('-inf')
greatest_decrease = float('inf')

increase_month = None
decrease_month = None

previous_profit = None

# path to csv
budget_data_csv = os.path.join("/Users/alisonlove/Bootcamp/Module Challenges/python-challenge/Resources/budget_data.csv")

# open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    financial_header = next(csv_reader)
    
    #start count for number of months
    num_months = 0

    # 
    for row in csv_reader:
        #add one to months as a new month occurs
        num_months += 1

        date_str = row[0]
        profit = int(row[1])
        net_total += profit
        profit_loss.append(profit)

        if previous_profit is not None:
            monthly_change = profit - previous_profit

            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                increase_month = date_str

            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                decrease_month = date_str

        previous_profit = profit

# Calculate average change
total_change = sum(profit_loss[i] - profit_loss[i-1] for i in range(1, len(profit_loss)))
average_change = total_change / (num_months - 1)

output_path = os.path.join("/Users/alisonlove/Bootcamp/Module Challenges/python-challenge/Analysis/financial.analysis.txt")
with open(output_path, 'w') as file:

    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total months: {num_months}\n")
    file.write(f"Total profit/loss: ${net_total}\n")
    file.write(f"Average change: ${average_change:.2f}\n")
    file.write(f"Greatest increase: {increase_month} (${greatest_increase})\n")
    file.write(f"Greatest decrease: {decrease_month} (${greatest_decrease})\n")

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total months: {num_months}")
    print(f"Total profit/loss: ${net_total}")
    print(f"Average change: ${average_change:.2f}")
    print(f"Greatest increase: {increase_month} (${greatest_increase})")
    print(f"Greatest decrease: {decrease_month} (${greatest_decrease})")





#ELECTION DATA

#set variables
total_votes = 0
candidates = {}
winner = ""
highest_votes = 0
        
#csv path
election_data_csv = os.path.join("/Users/alisonlove/Bootcamp/Module Challenges/python-challenge/Resources/election_data.csv")

#open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #store the header
    election_header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#analyze the results
for candidate, votes in candidates.items():
    if votes > highest_votes:
        highest_votes = votes
        winner = candidate

output_path = os.path.join("/Users/alisonlove/Bootcamp/Module Challenges/python-challenge/Analysis/election.analysis.txt")
with open(output_path, 'w') as file:

 # Write and print the results to the file and console respectively
    file.write("Election Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("---------------------------\n")
    
    print("***************************************")
    print("Election Analysis")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    
    for candidate, votes in candidates.items():
        file.write(f"{candidate}: {votes/total_votes*100:.3f}% ({votes})\n")
        print(f"{candidate}: {votes/total_votes*100:.3f}% ({votes})")
    
    file.write("---------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------\n")
    
    print("---------------------------")
    print(f"Winner: {winner}")