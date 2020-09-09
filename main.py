import csv
import sys

with open("budget_data.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    rows = list(csv_reader)
    total_rows = len(rows)
    tot = 0
    prev = 0
    diff_list = []
    maxchange = 0
    minchange = 0

    for row in rows:
        current = int(row['Profit/Losses'])

        tot = tot + current
        # build list of changes for average
        if current != prev:
            change = int(current - prev)
            diff_list.append(change)
            # account for no change on 1st value
            if row == rows[0]:
                diff_list.pop(0)
                change = 0
            # conditional to find max and min changes
            if change > maxchange:
                maxchange = change
                max_date = row['Date']
            if change < minchange:
                minchange = change
                min_date = row['Date']
            prev = current

# remove the first value has no bearing on the calc and take length
# diff_list.pop(0)
divider = len(diff_list)
avg = (sum(diff_list) / divider)

# DONE - The average change in Profit/Losses over the entire period
# DONE - The greatest increase in profits (date and amount) over the entire period
# DONE - The greatest decrease in losses (date and amount) over the entire peroid

with open("results.txt", 'w')as f:
    sys.stdout = f
    print("Financial Analysis")
    print("-" * 25)
    print("Total Months {}".format(total_rows))
    print("Total: ${}".format(tot))
    print("Average Change: ${}".format(round(avg, 2)))
    print("Greatest Increase in Profits: {} (${})".format(max_date, maxchange))
    print("Greatest Decrease in Profits: {} (${})".format(min_date, minchange))
f.close()
sys.stdout = sys.__stdout__

with open('results.txt', 'r') as file:
    print(file.read())
