import math

def average(str):
    total = 0
    for entry in str:
        total = entry + total
    return total/len(str)

def min(str):
    reference = str[0]
    for entry in str:
        if(entry <= reference):
            reference = entry
        else:
            pass
    return reference
    
def max(str):
    reference = str[0]
    for entry in str:
        if(entry >= reference):
            reference = entry
        else:
            pass
    return reference

