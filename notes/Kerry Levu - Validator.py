import csv


def drop_last_digit(num: str):
    num = num[0:15]
    return num


def digit_check(num: str):
    if len(num) == 16:
        print("%s is a 16 digit number." % num)
        return True
    print("%s is not a 16 digit number." % num)
    return False


def reverse(num: str):
    return num[::-1]


def multi_odd_index(num: str):
    list_num = list(num)
    current_index = -1
    for x in list_num:
        current_index = current_index + 1
        if current_index % 2 == 1:
            pass
        elif current_index % 2 == 0:
            multiplied_value = int(x) * 2
            if multiplied_value > 9:
                multiplied_value = multiplied_value - 9
            list_num.pop(current_index)
            list_num.insert(current_index, multiplied_value)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
    print(list_num)
    return list_num


def sum_all(num: str):
    total = (sum(num))
    print(total)
    return total


def mod_10(num: str):
    mod = num % 10
    print(mod)
    return mod

def last_int_add(num: str):
    last_dig = num[15]
def mod_10_check(num: str):
    if num % 10 == 0:
        print("The credit card is valid!")

def validate(num):
    digit_check(num)
    modified_num = drop_last_digit(num)
    reversed_num = reverse(modified_num)
    sum_num = multi_odd_index(reversed_num)
    total = sum_all(sum_num)
    mod_10(total)






# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         for row in reader:
#             old_number = row[0]  # String
#             if validate(old_number):
#                 writer.writerow(row)
#         print("OK")


validate("4556737586899855")
