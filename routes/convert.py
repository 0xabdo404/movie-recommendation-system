import ast
import pandas as pd

# Convert string representation of list of dictionaries to list of names
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
    L.append(i['name'])
    return L

# Convert string representation of list of dictionaries to list of names, limited to 3
def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
           break
    return L

# Convert string representation of list of dictionaries to list of names, limited to 5
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L