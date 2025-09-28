"""our task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""

def mysort(s):
    minus = [c for c in s if c.islower()]
    mayus = [c for c in s if c.isupper()]
    odd = [c for c in s if (c.isdigit() and int(c)%2 != 0)]
    even = [c for c in s if (c.isdigit() and int(c)%2 == 0)]
    
    minus.sort()
    mayus.sort()
    odd.sort()
    even.sort()
    
    return "".join(minus) + "".join(mayus) + "".join(odd) + "".join(even)
    
s = input()
print(mysort(s))
