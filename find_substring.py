def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        if sub_string[0:1] in string:
            # print(i)
            string = string[string.find(sub_string):len(string)]
            # print(string)
        if sub_string in string:
            count  += 1
        string = string[1:]
    return count

if __name__ == '__main__':
    a=1