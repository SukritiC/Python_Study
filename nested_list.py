# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#
# Example
#
# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:


if __name__ == '__main__':
    info = {}
    second_lowest = []
    sec_max = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if name not in info:
            info[name] = score
    info = dict(sorted(info.items(), key=lambda item: item[1]))
    l = len(info)
    max_key = list(info)[-1]
    max_score = info[max_key]
    min_key = list(info)[0]
    min_score = info[min_key]
    # print(max_score,"  ",min_score)
    # print(info)
    for key, val in info.items():
        # print(val)
        if val > min_score:
            sec_max = val
            break
    flipped = {}
    for key, value in info.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print(flipped[sec_max])    # print(max_key)
    flipped[sec_max].sort()
    for i in flipped[sec_max]:
        print(i)

