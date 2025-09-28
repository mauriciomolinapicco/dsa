"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools. 
To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. 
Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.
"""

s = input()
count = 1
result = ""

for i in range(len(s)):
    if i == len(s)-1:
        t = (count, int(s[i]))
        result += str(t)
        break
    if s[i] == s[i+1]:
        count += 1
    else:
        t = (count, int(s[i]))
        result += str(t)
        result += " "
        count = 1

print(result)