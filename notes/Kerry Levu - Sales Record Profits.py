import csv


with open("SalesRecords.csv", 'r') as old_csv:
    with open("SalesEdited.csv", 'w', newline='') as new_csv:
        print("Processing...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        max_profit = [0, 0]
        next(reader)
        for row in reader:
            print(row)
            item_type = row[2]
            profit = row[13]
            if int(profit) > max_profit[0]:
                max_profit.clear()
                max_profit.insert(1, profit)
            print(max_profit)
        print("Done...")
