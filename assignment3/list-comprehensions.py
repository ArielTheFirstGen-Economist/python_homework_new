############### Task 3 ###############

import csv

def read_employees():
    my_dict = {}
    new_list = []

    try:
        with open("../csv/employees.csv", 'r') as file:
            reader = csv.reader(file)
            line_count = 0

            for row in reader:
                if line_count == 0:
                    my_dict["fields"] = row
                else:
                    new_list.append(row)
                line_count += 1
            my_dict["rows"] = new_list
            print("\ntask 3")
            return my_dict

    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")
        exit()

employees = read_employees()

print(employees)

employee_row = employees["rows"]

full_names = [
    row[1] + " " + row[2] for row in employee_row
]

print("\nTheir full name are:")
print(full_names)

e_names = [
    name for name in full_names if "e" in name
]

print("\nNames with the letter 'e':")

if e_names:
    print(e_names)
else:
    print("No names with 'e' were found!")