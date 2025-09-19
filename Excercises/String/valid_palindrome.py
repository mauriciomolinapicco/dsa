"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1: Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

s = "race a car"
# ejemplo para limpiar a la cadena de cualquier caracter no alfanumerico
cadena = ''.join([char for char in s if char.isalpha() or char in '1234567890']).upper()
print(cadena)

class Solution(object):
    def isPalindrome(self, s):
        cadena = ''.join([char for char in s if char.isalpha() or char in '1234567890']).upper()
        left, right = 0, len(cadena) - 1

        while left < right:
            if cadena[left] != cadena[right]:
                return False
            left += 1
            right -= 1
        return True