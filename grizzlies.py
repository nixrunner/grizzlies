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

def median(str):
    if len(str) % 2 == 1 :
        index = math.floor(len(str)/2)
        return str[index]
    else:
        index1 = math.floor(len(str)/2)
        index2 = index1 - 1
        return (str[index1] + str[index2])/2

def stdev(str):
    variance = 0
    total = 0
    avg = average(str)
    length = len(str)
    for entry in str:
        total = float(pow(avg - entry,2)) + total
    variance = total/length
    return math.sqrt(variance)

def extract(str,num,operation):
    stack = []
    if operation == 'floor':
        for entry in str:
            if  entry >= num:
                stack.append(entry)
    elif operation == 'ceil':
        for entry in str:
            if  entry < num:
                stack.append(entry)
    return  stack

