import re

with open("dfs.txt", "r") as f:
    elements = f.read().split()

elements_length = len(elements)
print(elements_length)

keyword = ["False", "class", "finally", "is", "return",
           "None", "continue", "for", "lambda", "try",
            "True", "def", "from", "nonlocal", "while", 
           "and", "del", "global", "not", "with",
            "as", "elif", "if", "or", "yield", 
            "assert", "else", "import", "pass", 
           "break", "except", "in", "raise", "and",
           "or", "not", "int", "double", "float"]
input_keyword_list = []

identifier_pattern = "[A-Z]*[a-z]+"
input_identifiers_list = []

math_operators = ["+","-","*","/","//","%","**","=", "==", "!="]
input_math_operators_list = []

logical_operators = ["and","or","not","<",">","<=",">="]
input_logical_operators_list = []

numerical_values_int = "[0-9]+"
numerical_values_float = "[0-9]*[.][0-9]+"
input_numerical_values_list = []  

input_others_list = []

for index in range(elements_length):
    if elements[index] in keyword:
        if elements[index] in input_keyword_list:
            continue
        input_keyword_list.append(elements[index])
    elif elements[index] in math_operators:
        if elements[index] in input_math_operators_list:
            continue
        input_math_operators_list.append(elements[index])
    
    elif elements[index] in logical_operators:
        if elements[index] in input_logical_operators_list:
            continue
        input_logical_operators_list.append(elements[index])

    elif elements[index] in re.findall(identifier_pattern, elements[index]):
        if elements[index] in input_identifiers_list:
            continue
        input_identifiers_list.append(elements[index])

    elif elements[index] in re.findall(numerical_values_int, elements[index]) or re.findall(numerical_values_float, elements[index]) :
        if elements[index] in input_numerical_values_list:
            continue
        input_numerical_values_list.append(elements[index])

    else:
        if elements[index] in input_others_list:
            continue
        input_others_list.append(elements[index])

print("Keyword:",input_keyword_list)
print("Identifier:",input_identifiers_list)
print("Math Operators:",input_math_operators_list)
print("Logical Operators:",input_logical_operators_list)
print("Numerical Values:",input_numerical_values_list)
print("Others:",input_others_list)
