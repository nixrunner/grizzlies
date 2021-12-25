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
    chain = []
    if operation == 'floor':
        for entry in str:
            if  entry >= num:
                chain.append(entry)
    elif operation == 'ceil':
        for entry in str:
            if  entry < num:
                chain.append(entry)
    return chain

