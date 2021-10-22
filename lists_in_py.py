# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    N = int(input())
    final_lst = []
    for i in range(N):
        stmt = input()
        s1 = stmt.split()
        if s1[0] == 'insert':
            final_lst.insert(int(s1[1]),int(s1[2]))
        elif s1[0] == 'print':
            print(final_lst)
        elif s1[0] == 'remove':
            final_lst.remove(int(s1[1]))
        elif s1[0] == 'append':
            final_lst.append(int(s1[1]))
        elif s1[0] == 'sort':
            final_lst.sort()
        elif s1[0] == 'pop':
            final_lst.pop()
        elif s1[0] == 'reverse':
            final_lst.reverse()
        

