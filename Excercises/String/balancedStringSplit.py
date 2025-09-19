# Dado un str formado por L,R devolver cuantos substrings balanceados (misma cnatidad de L y R)
# podemos splitear el str

class Solution(object):
    def balancedStringSplit(self, s):
        app = []
        opposite = {'L':'R', 'R':'L'}
        res = 0
        for char in s:
            if app == []:
                res += 1
                app.append(char)
            else:
                if opposite[char] in app:
                    app.remove(opposite[char])
                else:
                    app.append(char)
        return res
    

# Solucion mas efectiva: mantener un balance
class Solution(object):
    def balancedStringSplit(self, s):
        app = []
        opposite = {'L':'R', 'R':'L'}
        res = 0
        for char in s:
            if app == []:
                res += 1
                app.append(char)
            else:
                if opposite[char] in app:
                    app.remove(opposite[char])
                else:
                    app.append(char)
        return res