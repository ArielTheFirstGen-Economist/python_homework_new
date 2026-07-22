############### Task 1 ###############
""" 
import traceback

try:

    with open('diary.txt','a') as file:

        day = input("What happened today: ")

        file.write(day + "\n")
        
        while True:
            new_entry = input("What else: ")
            if new_entry == "done for now":
                break
            file.write(new_entry + "\n")
except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"An exception occurred.")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}") 
 
 """
############### Task 2 ##### ##########

import csv

def read_employees():
    my_dict = {}
    new_list = []

    try: 
         with open("../csv/employees.csv",'r') as file:
            reader = csv.reader(file)
            line_count = 0

            for row in reader:
                if line_count == 0:
                    my_dict["fields"] = row
                else:
                    new_list.append(row)                    
                line_count += 1
            my_dict["rows"] = new_list
            print("\ntask 2")
            return my_dict

    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")
        exit()

employees = read_employees()

print(employees) 


############### Task 3 ###############

def column_index(name):
    return employees["fields"].index(name)

## call the function
employee_id_column = column_index("employee_id")
    
print("\ntask 3")    
print(employee_id_column)
 
############### Task 4 ###############

def first_name(row_number):

    col_idx = column_index("first_name")

    value = employees["rows"][row_number][col_idx]
    
    print("\ntask 4")
    return value

test_name = first_name(0)

print({test_name})

############### Task 5 ###############

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    filtered_data = filter(employee_match, employees["rows"])
    print("\ntask 5")
    return list(filtered_data)

id_test = employee_find(10)

print(id_test)

############### Task 6 ###############

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   print("\ntask 6")
   return matches

id_two_test = employee_find_2(6)

print(id_two_test)

############### Task 7 ###############
# we will sort the employees by last name

def sort_by_last_name():
    col_idx = column_index("last_name")
    employees["rows"].sort(key = lambda row : row[col_idx])
    print("\ntask 7") 
    return employees["rows"]
sort_by_last_name()


print(employees)

############### Task 8 ###############
# In this function we will return a dict for the employee data

def employee_dict(row):
    new_dict = {}
    for i in range(len(employees["fields"])):
        field_name = employees["fields"][i]
        if field_name != "employee_id": new_dict[field_name] = row[i]
    print("\ntask 8") 
    return new_dict

test = employee_dict(employees["rows"][0])
print(test)

############### Task 9 ###############

def all_employees_dict():
    newer_dict = {}
    id_col = column_index("employee_id")
    for row in employees["rows"]:
        emply_id = row[id_col]
        new_data = employee_dict(row)
        newer_dict[emply_id] = new_data
    print("\ntask 9") 
    return newer_dict
""" all_data = all_employment_dict() """
print(all_employees_dict())

############### Task 10 ###############

import os

def get_this_value():
    value = os.getenv("THISVALUE")
    print("\ntask 10")
    return value
print(get_this_value())

############### Task 11 ###############

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    print("\ntask 11")

set_that_secret("This is a fun class")
    
print(custom_module.secret)

############### Task 12 ###############

import csv

def read_minutes():
    min_one_dict = {"fields": [], "rows": []}
    min_two_dict = {"fields": [], "rows": []}

    try:
        with open("../csv/minutes1.csv",'r') as file:
            reader = csv.reader(file)
            min_one_dict["fields"] = next(reader)
            
            for row in reader:
                min_one_dict["rows"].append(tuple(row))
        
        with open("../csv/minutes2.csv", 'r') as file2:
            reader2 = csv.reader(file2)
            min_two_dict["fields"] = next(reader2)

            for row in reader2:
                min_two_dict["rows"].append(tuple(row))
            
        print("\ntask 12")
        return min_one_dict, min_two_dict

    except Exception as e:
        print(f"An exception occured. {type(e).__name__}")
        exit()

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

############### Task 13 ###############

def create_minutes_set():
    num_set1 = set(minutes1["rows"])
    num_set2 = set(minutes2["rows"])

    merged_data = num_set1.union(num_set2)

    print("\ntask 13")
    return merged_data

minutes_set = create_minutes_set()
print(minutes_set)
############### Task 14 ###############

from datetime import datetime

def create_minutes_list():
    orginal_data = list(minutes_set)
    cleaned_data = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), orginal_data)
    print("\ntask 14")
    return list(cleaned_data)

minutes_list = create_minutes_list()

print(minutes_list)

############### Task 15 ###############

def write_sorted_list():
    sorted_data = sorted(minutes_list, key=lambda x: x[1])
    converted_data = map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_data)
    final_string_list = list(converted_data)

    try:
        with open("./minutes.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(final_string_list)
        print("\ntask 15")
        return final_string_list
    
    except Exception as e:
        print(f"An exception occured. {type(e).__name__}")
        exit()

new_data = write_sorted_list()
print("Check Folder")