############### Task 1 ###############

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
 