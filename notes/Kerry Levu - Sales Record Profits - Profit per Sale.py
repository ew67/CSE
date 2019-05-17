import csv

total_units_sold = {}
total_profit = {}
with open("SalesRecords.csv", 'r') as old_csv:
    with open("SalesEdited.csv", 'w', newline='') as new_csv:
        print("Processing...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        max_profit = [0, 0]
        next(reader)
        for row in reader:
            region = row[0]
            item_type = row[2]
            profit = float(row[13])
            unit_price = float(row[9])
            unit_cost = float(row[10])
            total_sold = float(row[8])
            unit_profit = profit / total_sold
            if item_type in total_units_sold:
                total_units_sold[item_type] += float(total_sold)
            else:
                total_units_sold[item_type] = float(total_sold)
            if item_type in total_profit:
                total_profit[item_type] += float(profit)
            else:
                total_profit[item_type] = float(profit)
        print(total_units_sold)
        highest_total_profit = max(total_units_sold, key=total_units_sold.get)
        print("The highest total profit is %s generating %f." % (highest_total_profit,
                                                                 max(total_units_sold.values())))
        print("Done...")
        print()
