import csv


def validate(num: str):
    first_num = int(old_number[0])
    second_num = int(old_number[1])
    if first_num % 2 == 1:
        return True
    if second_num % 2 == 0:
        return True
    return False

# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         # old_number = int(row[0]) + 1
#         old_number = row[0]
#         print(old_number)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")
