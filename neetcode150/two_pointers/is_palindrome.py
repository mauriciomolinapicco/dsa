""" 
solucion limpiando la cadena antes de procesar
"""
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = [c for c in s if (c.isdigit() or c.islower())]
        l = 0
        r = len(s) - 1
        while l <= r:
            c1 = s[l]
            c2 = s[r]
            if c1 != c2:
                return False
            l += 1
            r -= 1
        return True


"""
sin limpiar la cadena antes de procesar
"""
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l <= r:
            c1 = s[l]
            c2 = s[r]
            if not c1.islower() and not c1.isdigit():
                l += 1
                continue
            if not c2.islower() and not c2.isdigit():
                r -= 1
                continue

            if c1 != c2:
                return False
            l += 1
            r -= 1
        return True


