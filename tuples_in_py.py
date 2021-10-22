# Task
# Given an integer,n , n and  space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t) .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    s = []
    for i in integer_list:
        s.append(i)
    tup = tuple(s)
       
    print(hash(tup))
    # print(s)
