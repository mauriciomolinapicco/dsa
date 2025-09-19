class Solution(object):
    # recorro todos los caracteres y si son de abertura los guardo en 
    # el stack y si no chequeo que deben estar en la ultima posicion 
    # del stack
    def isValid(self, s):
        stack = [] # creo una pila
        hash = {'}':'{', ')':'(', ']':'['}
        for caracter in s:
            if caracter in hash:
                if stack and stack[-1] == hash[caracter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(caracter)
        return not stack