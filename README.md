# Financial Analysis - PyBank

### Objective

The Python script *`main.py`* analyzes the financial records of one fictional company and calculates each of the following:

- The total number of months included in the dataset
- The net total amount of **Profit/Losses** over the entire period
- The average of the changes in **Profit/Losses** over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

In addition, the script prints the analysis to the terminal and saves it to a text file *financial_analysis.txt*:

```
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```


By default, the script uses Python lists:

```
# Toggle which scripts to run (1 to run, 0 to skip)
usingLists = 1
usingDicts = 0
```

To use dictionaries, update the script:

    usingLists = 0
    usingDicts = 1

save it and rerun it.

### Tools / Techniques Used:

- Python

### About Data

The dataset *Resources/budget_data.csv* contains a set of financial data.

- **Number of records:**	86
- **Columns**:
  - Date
  - Profit/Losses