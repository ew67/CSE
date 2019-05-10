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
            # print(max_profit)
            if 'Fruits' in item_type:
                Fruit_profit.append(float(profit))
                total = sum(Fruit_profit)
                print(total)
            if 'Clothes' in item_type:
                Clothes_profit.append(float(profit))
                total = sum(Clothes_profit)
            if 'Meat' in item_type:
                Meat_profit.append(profit)
                total = sum(Meat_profit)
            if 'Beverages' in item_type:
                Beverages_profit.append(profit)
                total = sum(Beverages_profit)
            if 'Office Supplies' in item_type:
                Office_profit.append(profit)
                total = sum(Office_profit)
            if 'Cosmetics' in item_type:
                Cosmetics_profit.append(profit)
                total = sum(Cosmetics_profit)
            if 'Snacks' in item_type:
                Snacks_profit.append(profit)
                total = sum(Snacks_profit)
            if 'Personal Care' in item_type:
                Personal_profit.append(profit)
                total = sum(Personal_profit)
            if 'Household' in item_type:
                Household_profit.append(profit)
                total = sum(Household_profit)
            if 'Vegetables' in item_type:
                Vegetables_profit.append(profit)
                total = sum(Vegetables_profit)
            if 'Baby' in item_type:
                Baby_profit.append(profit)
                total = sum(Baby_profit)
            if 'Cereal' in item_type:
                Cereal_profit.append(profit)
                total = sum(Cereal_profit)
        print("Done...")

