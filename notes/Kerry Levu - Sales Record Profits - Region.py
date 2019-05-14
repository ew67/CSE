import csv

region_type_list = {}

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
            profit = row[13]
            if region in region_type_list:
                region_type_list[region] += float(profit)
            else:
                region_type_list[region] = float(profit)
        print(region_type_list)
        highest_total_profit = max(region_type_list, key=region_type_list.get)
        print("The highest total profit is %s generating %f." % (highest_total_profit,
                                                                 max(region_type_list.values())))
        print("Done...")
        print()

