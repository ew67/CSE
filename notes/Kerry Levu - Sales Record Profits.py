import csv

Fruit_profit = []
Clothes_profit = []
Meat_profit = []
Beverages_profit = []
Office_profit = []
Cosmetics_profit = []
Snacks_profit = []
Personal_profit = []
Household_profit = []
Vegetables_profit = []
Baby_profit = []
Cereal_profit = []

with open("SalesRecords.csv", 'r') as old_csv:
    with open("SalesEdited.csv", 'w', newline='') as new_csv:
        print("Processing...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        max_profit = [0, 0, 0]
        next(reader)
        item_type_list = []

        for row in reader:
            region = row[0]
            item_type = row[2]
            profit = row[13]
            # Finds Largest Single Order
            if float(profit) > float(max_profit[1]):
                max_profit.pop(1)
                max_profit.insert(1, profit)
                max_profit.pop(0)
                max_profit.insert(0, item_type)
            print(max_profit)
            if item_type not in item_type_list:
                item_type_list.append(item_type)
            print(item_type_list)
            
        print("Done...")

