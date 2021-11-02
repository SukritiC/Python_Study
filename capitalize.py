import re
# Complete the solve function below.
def convert_to_uupercase(m):
    return m.group(1) + m.group(2).upper()
def solve(s):
    return re.sub("(^|\s)(\S)", convert_to_uupercase, s)