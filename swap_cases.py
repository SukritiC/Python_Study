# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    s1 = ""
    for i in s:
        if i.isupper():
            s1 += i.lower()
        elif i.islower():
            s1 += i.upper()
        else :
            s1 += i
            
    return s1

