# Write your code here.# Write your code here.
""" pytest -v -x assignment1-test.py # can use just -x, adding -v lists the passing tests """


######## task 1 ########

""" def hi():
    return "Hello"

print(hi())
 """
######### task 2 ########

""" def greet(name):
    return f"Hello {name}"

print(greet("Ariel"))
 """
######### task 3 ########

""" def calc(num1, num2, oper = "multiply"):
    try:
        match oper:
            case "multiply":
                return num1 * num2    
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "int_divide":
                return num1 // num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "power":
                return num1 ** num2
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("Can't divide by a string")
    
print(calc(5, 5,"add")) """

######### task 4 ########

""" def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion(25, "str"))            
print(type(data_type_conversion(25, "str"))) """

######### task 5 ########

""" def grading_system(*args):
    try:    
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80: 
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else: 
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
print(grading_system(16,5,51,9)) """
        
######### task 6 ########

""" def repeat(string, count):
    result = ""
    for i in range(count):
        result = result + string
    return result

print(repeat("heart break", 20)) """

######### task 7 ########

""" def student_scores(metric,**kwargs):
    if metric == "mean":
        scores = kwargs.values()
        sum_scores = sum(scores)
        count_scores = len(scores)
        return sum_scores / count_scores            
    elif metric == "best":
        highest_score = 0
        highest_score_name = ""
        for name, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                highest_score_name = name
        return highest_score_name

print(student_scores("mean", Kali=1.0, Pacey=10.0, Joey=20.0, Rex=30.0, Ashoka=90.0))
print(student_scores("best", Kali=1.0, Pacey=10.0, Joey=20.0, Rex=30.0, Ashoka=90.0)) """

######### task 8 ########

""" def titleize(tittle):
    little_word = ["a", "on", "an", "the", "of", "and", "is", "in"]
    indiv_words = tittle.split()
    title_words = []
    for i, word in enumerate(indiv_words):
        if i == 0 or i == len(indiv_words) - 1:
            title_words.append(word.capitalize())
        elif word in little_word:
            title_words.append(word.lower())
        else:
            title_words.append(word.capitalize())
    return " ".join(title_words)

print(titleize("the undocumented americans")) """
 
######### task 9 ########

def hangman(secret, guess):
    final_answer = ""
    for letter in secret:
        if letter in guess:
            final_answer += letter
        else:
            final_answer += "_"
    return final_answer


######### task 10 ########


