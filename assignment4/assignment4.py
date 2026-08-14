############### Task 1 ###############

################ 1.1

import pandas as pd

data_frame = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}


task1_data_frame = pd.DataFrame(data_frame)

print("\n Task 1.1 \n")
print(task1_data_frame)

################ 1.2

Salary = [70000, 80000, 90000]

task1_with_salary = task1_data_frame.copy()

task1_with_salary['Salary'] = Salary

print("\n Task 1.2 \n\n", task1_with_salary)

################ 1.3

task1_older = task1_with_salary.copy()

res = task1_older.Age 

task1_older['Age'] = task1_older['Age'] + 1

print("\n Task 1.3 \n\n", task1_older)

################ 1.4

employees = pd.DataFrame(task1_older)

employees.to_csv("employees.csv", index=False)

print("\n Task 1.4 \n", employees)



############### Task 2 ###############

################ 2.1 Reading CSV

try:
    task2_employees = pd.read_csv('employees.csv')

    print("\n Success \n ", task2_employees)


except Exception as e:
    print(f"An exception occurred. {type(e).__name__}")
    exit()

################ 2.2 Creating JSON

new_employees = [
    {"Name": 'Eve', "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": 'Frank', "Age": 40, "City": "Seattle", "Salary": 95000}             
]

pd.DataFrame(new_employees).to_json ('additional_employees.json', orient='split', compression='infer', index=True)

json_employees = pd.read_json('additional_employees.json', orient='split', compression='infer')

""" pd.DataFrame(json_employees) """

print("\n Task 2.2 \n ", json_employees)

################ 2.3 Combining Data Frame

employees_cont = json_employees.copy()

# I created a copy just to keep the origial data

""" new_employees_df = pd.DataFrame(json_to_df) """

more_employees = pd.concat([task2_employees, employees_cont], ignore_index=True)

print("\n Task 2.3 \n ", more_employees)



############### Task 3 ###############

################ 3.1 Head

first_three = more_employees.head(3)

print("\n Task 3.1 \n ", first_three)

################ 3.2 Tail 

last_two = more_employees.tail(2)

print("\n Task 3.2 \n ", last_two)

################ 3.3 Shape

employee_shape = more_employees.shape

print("\n Task 3.3 \n ", employee_shape)

################ 3.4 Summary

print("\n Task 3.4 \n ")

more_employees.info()

############### Task 4 ###############

################ 4.1 Loading data

try:
    dirty_data = pd.read_csv('dirty_data.csv')

    print("\n Succesfully read data \n", dirty_data)

except Exception as e:
    print(f"An exception occurred. {type(e).__name__}")
    exit()

clean_data = dirty_data.copy()

print("\n Task 4.1 clean data set \n", clean_data)

################ 4.2 Removing duplicates

print("\n Find duplicates\n",clean_data.duplicated())

clean_data.drop_duplicates(inplace=True)

print("\n Task 4.2 Removing duplicates \n", clean_data)

################ 4.3 Cleaning age column

clean_data["Age"] = clean_data["Age"].replace("unknown", pd.NA)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

print("\n Task 4.3 Cleaning Age \n", clean_data)

################ 4.4 Cleaning salary column

""" print(clean_data["Salary"].unique()) """

clean_data["Salary"] = clean_data["Salary"].replace(" unknown", pd.NA)

clean_data["Salary"] = clean_data["Salary"].replace(" n/a", pd.NA)

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce").round(2)

print("\n Task 4.4 Cleaning Salary \n", clean_data)

################ 4.5 filling data

import numpy as np

mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)

median_sal = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_sal)

print("\n Task 4.5 Filling Data \n", clean_data)


################ 4.6 Date formated

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")

print("\n Task 4.6 Date formated \n", clean_data)

################ 4.7 Formated Name & Deparment

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()

clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()

print("\n Task 4.7 Formated Name & Deparment \n", clean_data)