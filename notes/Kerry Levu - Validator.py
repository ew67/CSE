import csv


def digit_check(num: str):
    if len(num) == 16:
        print("%s is a 16 digit number." % num)
        return True
    print("%s is not a 16 digit number." % num)
    return False


def reverse(num: str):
    print(num[::-1])


def multi_odd_index(num: str):
    list_num = list(num)
    for x in num:
        current_index = 0
        new_number = x * 2
        list_num.pop(current_index)
        list_num.insert(current_index, new_number)
    print(list_num)


def validate(num):
    digit_check(num)
    reverse(num)
    multi_odd_index(num)
    pass


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


cc_number = "1477190440641750"

digit_check(cc_number)

reverse(cc_number)

multi_odd_index(cc_number)
