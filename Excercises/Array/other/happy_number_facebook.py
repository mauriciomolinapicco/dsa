"""
Question asked by facebook
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
"""
    EXPLICACION: cuando la suma de los cuadrados de todos los digitos da 1 puedo cerrar el ciclo, 
    porque seguira siendo siempre 1. Cuando no da uno, o sea no es un happy number, tengo que detectarlo de alguna forma.
    Lo hago porque cuando NO ES un happy number, cuando entra en el bucle infinito siempre se va a repetir un numero.
    Por eso tengo un HashSet seen que contiene todos las sumas que ya pasaron. 

"""

class Solution(object):
    def isHappy(self, n):
        seen = set()
        while True:
            sum = 0
            for num in str(n):
                sum += int(num) ** 2
            if sum == 1:
                return True #es happy number
            if sum in seen:
                return False # la suma ya habia pasado antes, por lo que es un ciclo infinito
            seen.add(sum)
            n = sum # ahora sum es el nuevo valor sobre el que tengo que iterar
        