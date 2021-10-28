# Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------

# Enter your code here. Read input from STDIN. Print output to STDOUT
num = input()
lst = num.split()
n = int(lst[0])
m = int(lst[1])

# n = 7
# m = 21

if m == n*3:
    dash = m
    mid = 1
    dash -= 3
    l_dash = int(dash/2)
    for _ in range(int(n/2)):        
        for _ in range(l_dash):
            print('-',end="")               
        for _ in range(mid):
            print('.|.',end="")        
        mid += 2
        for _ in range(l_dash):
            print('-',end="")
        l_dash -= 3
        print()
    str = "WELCOME"
    no = int((m - 7)/2)
    for _ in range(no):
        str = "-"+str+"-"
    print(str)
    mid -= 2
    l_dash +=3
    for _ in range(int(n/2)):        
        for _ in range(l_dash):
            print('-',end="")               
        for _ in range(mid):
            print('.|.',end="")        
        mid -= 2
        for _ in range(l_dash):
            print('-',end="")
        l_dash += 3
        print()