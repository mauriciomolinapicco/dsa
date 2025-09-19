# Best solution!! Two pointers
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        left, right = 0, len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        
        return True
    

class Solution(object):
    def isPalindrome(self, x):
        cadena = str(x)
        invertida = ""
        for i in range(len(cadena) - 1, -1, -1):
            invertida += cadena[i]
        # cadena_invertida = cadena[::-1]
        print(invertida)
        return invertida == cadena
    