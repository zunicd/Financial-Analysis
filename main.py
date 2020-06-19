# Toggle which scripts to run (1 to run, 0 to skip)
usingLists = 1
usingDicts = 0

if usingLists:
    print('\n===== Using Lists =====\n')

    # Script for analyzing financial records (using lists)

    # Import modules
    import os
    import csv

    # Set path for file
    budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

    # Open csv file in read mode
    with open(budget_csv, 'r') as budget:
        budget_data = csv.reader(budget, delimiter=',')

        # Set header and first data row
        header = next(budget_data)
        row_1 = next(budget_data)

        # Initialize profit variables
        profit = int(row_1[1])
        profit_old = profit

        #  Initialize lists
        change_l = []
        date_l = []

        # Loop through file 
        for row in budget_data:
            # read profit in current row and add it to total sum
            profit_current = int(row[1])
            profit += profit_current
            # Calculate profit change between two months and append both lists
            change = profit_current - profit_old
            change_l.append(change)
            date_l.append(row[0])
            # Save profit for next iteration
            profit_old = profit_current               

    # Zip two lists together
    profit_change = zip(date_l, change_l)

    # Create list of tuples: (date, change)
    pcl = list(profit_change)

    # Sum second elements in tuples (change)
    total_change = sum(k[1] for k in pcl)

    # Calculate average change 
    lines = len(change_l)
    avrg = total_change / lines

    # Adding 1 because we skipped the 1st data row earlier
    months = lines + 1

    # Sort the list per second element in tuple, ascending
    pcls = sorted(pcl, key = lambda k: k[1])
    # Greatest decrease - 1st tuple in list
    decr_d, decr_ch = pcls[0][0], pcls[0][1]
    # Greatest increase - last tuple in list
    incr_d, incr_ch = pcls[-1][0], pcls[-1][1]

    # Prepare output with financial analysis
    output = ("\nFinancial Analysis\n"
        "----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${profit}\n"
        f"Average Change: ${avrg:.2f}\n"
        f"Greatest Increase in Profits: {incr_d} (${incr_ch})\n"
        f"Greatest Decrease in Profits: {decr_d} (${decr_ch})\n"
            )

    # Display financial analysis
    print (output)

    # Export financial analysis to text file
    analysis = os.path.join('financial_analysis.txt')
    with open(analysis, 'w') as f:
        print(output, file=f)


if usingDicts:
    print('\n===== Using Dictionaries =====\n')

    # Script for analyzing financial records (using dictionaries)

    # Import modules
    import os
    import csv

    # Set path for file
    budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

    # Open csv file in read mode
    with open(budget_csv, 'r') as budget:
        budget_data = csv.reader(budget, delimiter=',')

        # Set header and first data row
        header = next(budget_data)
        row_1 = next(budget_data)

        # Initialize profit variables
        profit = int(row_1[1])
        profit_old = profit

        # Initialize dictionary, keys = Date, values = profit change
        profit_change_d = {}

        # Loop through file 
        for row in budget_data:
            # read profit in current row and add it to total sum
            profit_current = int(row[1])
            profit += profit_current
            # Calculate profit change between two months and add it to dictionary
            change = profit_current - profit_old
            profit_change_d[row[0]] = change
            # Save profit for next iteration
            profit_old = profit_current               

    # Calculate total change - sum of dictionary values
    total_change = sum(profit_change_d.values())
    # Calculate average change 
    lines = len(profit_change_d)
    avrg = total_change / lines

    # Adding 1 because we skipped the 1st data row earlier
    months = lines + 1

    # Greatest increase - maximum of dictionary values
    incr_d, incr_ch = max(profit_change_d.items(), key = lambda k: k[1])
    # Greatest decrease - minimum of dictionary values
    decr_d, decr_ch = min(profit_change_d.items(), key = lambda k: k[1])

    # Prepare output with financial analysis
    output = ("\nFinancial Analysis\n"
        "----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${profit}\n"
        f"Average Change: ${avrg:.2f}\n"
        f"Greatest Increase in Profits: {incr_d} (${incr_ch})\n"
        f"Greatest Decrease in Profits: {decr_d} (${decr_ch})\n"
            )

    # Display financial analysis
    print (output)

    # Export financial analysis to text file
    analysis = os.path.join('financial_analysis.txt')
    with open(analysis, 'w') as f:
        print(output, file=f)
