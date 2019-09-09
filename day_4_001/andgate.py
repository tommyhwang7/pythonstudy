def and_gate(left,right):
    if (left == 1) and (right == 1):
        return 1
 
    return 0

def or_gate(left,right):
    if (left == 1) or (right ==1):
        return 1
    
    return 0

def xor_gate(left,right):
    if (left == right):
        return 0
    
    return 1

def not_gate(left):
    if (left == 0):
        return 1
    return 0
