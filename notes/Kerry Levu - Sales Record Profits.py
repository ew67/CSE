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
item_type_strings = ['Fruit', 'Clothes', 'Beverages', 'Office', 'Cosmetics', 'Snacks',
                     'Personal', 'Household', 'Vegetables', 'Baby', 'Cereal']
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
            # Finds Largest Single Order
            # if float(profit) > float(max_profit[1]):
            #     max_profit.pop(1)
            #     max_profit.insert(1, profit)
            #     max_profit.pop(0)
            #     max_profit.insert(0, item_type)
            # print(max_profit)
            if 'Fruits' in item_type:
                Fruit_profit.append(float(profit))
            if 'Clothes' in item_type:
                Clothes_profit.append(float(profit))
            if 'Meat' in item_type:
                Meat_profit.append(float(profit))
            if 'Beverages' in item_type:
                Beverages_profit.append(float(profit))
            if 'Office Supplies' in item_type:
                Office_profit.append(float(profit))
            if 'Cosmetics' in item_type:
                Cosmetics_profit.append(float(profit))
            if 'Snacks' in item_type:
                Snacks_profit.append(float(profit))
            if 'Personal Care' in item_type:
                Personal_profit.append(float(profit))
            if 'Household' in item_type:
                Household_profit.append(float(profit))
            if 'Vegetables' in item_type:
                Vegetables_profit.append(float(profit))
            if 'Baby' in item_type:
                Baby_profit.append(float(profit))
            if 'Cereal' in item_type:
                Cereal_profit.append(float(profit))
        Fruit_total = round(sum(Fruit_profit), 2)
        Clothes_total = round(sum(Clothes_profit, 2))
        Meat_total = round(sum(Meat_profit, 2))
        Beverages_total = round(sum(Beverages_profit, 2))
        Office_total = round(sum(Office_profit, 2))
        Cosmetics_total = round(sum(Cosmetics_profit, 2))
        Snacks_total = round(sum(Snacks_profit, 2))
        Personal_total = round(sum(Personal_profit, 2))
        Household_total = round(sum(Household_profit, 2))
        Vegetables_total = round(sum(Vegetables_profit, 2))
        Baby_total = round(sum(Baby_profit, 2))
        Cereal_total = round(sum(Baby_profit, 2))
        item_type_list = [Fruit_total, Clothes_total, Beverages_total, Office_total, Cosmetics_total, Snacks_total,
                          Personal_total, Household_total, Vegetables_total, Baby_total, Cereal_total]
        highest_total_profit = max(item_type_list)
        index_of_highest_profit = item_type_list.index(highest_total_profit)
        print("The highest total profit is %s generating %d." % (item_type_strings[index_of_highest_profit],
                                                                 highest_total_profit))
        print("Done...")

