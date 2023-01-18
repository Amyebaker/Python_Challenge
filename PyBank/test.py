# Program to read CSV with "date" and "Profit/Loss" data, analyse results, and output to screen and text file

# import the os module to join the file paths across operating systems
import os

# import Module for reading CSV files
import csv

budget_path = os.path.join('.', 'PyBank','Resources', 'budget_data.csv')

# Path for output text file
output_data = os.path.join('.', 'analysis', 'output_data.txt')

#Open CSV file
with open(budget_path) as budget_file:
	# read the CSV file
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Store header info
    csv_header = next(budget_reader)

    # Set initial variables to 0
    total_months = 0
    total_profit_loss = 0
    greatest_increase = 0
    greatest_decrease = 0
    total_change = 0
    opening_profit_loss = 0
    previous_row = ["",0]

    for row in budget_reader:
            
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row[1])

        if opening_profit_loss == 0:
            opening_profit_loss = int(row[1])
        else:
            closing_profit_loss = int(row[1])
                
            monthly_increase_decrease = int(row[1]) - int(previous_row[1])
                # Calculate the greatest increase in profits (date and amount) over the entire period
        if greatest_increase < monthly_increase_decrease:
            greatest_increase = monthly_increase_decrease
            greatest_increase_month = str(row[0])

                # Calculate the greatest decrease in losses (date and amount) over the entire period
        if greatest_decrease > monthly_increase_decrease:
            greatest_decrease = monthly_increase_decrease
            greatest_decrease_month = str(row[0])

                # Save previous row so we can make comparison in the next iteration
        previous_row = row

        # Calculate the average changes in Profit/Losses over the entire period
        average_change = (closing_profit_loss - opening_profit_loss) / (total_months - 1)

# Print average change to 2 decimal places
formatted_average_change = "{:.2f}".format(average_change)
# Print data to screen
print("Financial Analysis")
print("----------------------------")
# Print total months
print(f"Total Months: {total_months}")
# Print total profit/loss
print(f"Total: ${total_profit_loss}")
# Print average changes
print(f"Average Change: ${formatted_average_change}")
# Print greatest increase in profits
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
# Print greatest decrease in profits
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
# Print data to text file
write_file = open(output_data, 'w')
write_file.write(f"Financial Analysis\n")
write_file.write(f"----------------------------\n")
write_file.write(f"Total Months: {total_months}\n")
write_file.write(f"Total: ${total_profit_loss}\n")
write_file.write(f"Average Change: ${formatted_average_change}\n")
write_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
write_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
write_file.close()

