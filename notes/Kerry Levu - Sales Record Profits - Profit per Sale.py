import csv

total_units_sold = {}
total_profit = {}
profit_per_dict = {}
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
            if item_type in total_units_sold:
                total_units_sold[item_type] += float(total_sold)
            else:
                total_units_sold[item_type] = float(total_sold)
            if item_type in total_profit:
                total_profit[item_type] += float(profit)
            else:
                total_profit[item_type] = float(profit)
        for key, value in total_profit.items():
            profit_per = value / total_units_sold[item_type]
            if key in profit_per_dict:
                profit_per_dict[key] += float(profit_per)
            else:
                profit_per_dict[key] = float(profit_per)
        highest_profit_per = max(profit_per_dict, key=profit_per_dict.get)
        print("The highest profit per units sold is %s, %f." % (highest_profit_per, max(profit_per_dict.values())))
        print("Done...")
