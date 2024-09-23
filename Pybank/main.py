# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# To track Greatest Increase
Greatest_increase = float("-inf")
# To Store the date of the greatest increase
Greatest_increase_date = None
# To Store previous value
previous_value = None
# To track Greatest Decrease
Greatest_decrease = float("inf")
# To Store the Greatest Decrease Date
Greatest_decrease_date = None
# List to store change values
Net_changes = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    #Converting Value to float
    previous_value = float(first_row[1])

    #Adding First Value to Net Total
    total_net += previous_value

    # Process each row of data
    for row in reader:
        # Creating a List of the Dates
        Dates = row[0]

        # Track the total Months
        
        #Getting the Months by spliting with "-"
        Month_split = row[0].strip().split("-")[0]
        #Adding to  total months counter
        total_months += 1
        # Adding +1 as the first row was extracted
        Final_total_months = total_months + 1

        # Converting values to float 
        profit_losses = float(row[1])
        # Track the total
        total_net += profit_losses 

        # Calculating the number of changes from every month
        if previous_value is not None:
            # Calculating the Change from month to month
            change =  profit_losses - previous_value
            # Storing change values in list
            Net_changes.append(change)
            
        # Calculate the greatest increase in profits (month and amount)
            #Checking if the current change value is greater then the current recorded Greatest Increase
            if change > Greatest_increase:
                #Update Greatest Increase value
                Greatest_increase = change
                # Capturing the date of the increase
                Greatest_increase_date = Dates

        # Calculate the greatest decrease in losses (month and amount)
            #Checking if the current change value is less then the current recorded Greatest decrease
            if change < Greatest_decrease:
                # Update Greatest Decrease Value
                Greatest_decrease = change
                # Capturing the date of the decrease
                Greatest_decrease_date = Dates
      
        # Updating the previous value
        previous_value = profit_losses

# Calculate the average net change across the months
average_change = sum(Net_changes)/len(Net_changes)


# Generate the output summary/Print outputs
print("Fincanial Analysis")
print("-------------------------")
print(f"Total Months: {Final_total_months}")
print(f"Total: ${total_net:.0f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase:.0f})")
print(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease:.0f})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Fincanial Analysis\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Months: {Final_total_months}\n")
    txt_file.write(f"Total: ${total_net:.0f}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase:.0f})\n")
    txt_file.write(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease:.0f})\n")