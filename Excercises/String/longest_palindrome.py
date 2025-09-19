class Solution(object):
    #freakin great solution
    def longestPalindrome(self, s):
        mapa = {}
        res = 0
        
        for char in s:
            mapa[char] = mapa.get(char, 0) + 1
        
        for cant in mapa.values():
            if cant > 1:
                # if cant % 2 == 0:
                #     res += cant
                # else: 
                #     res += cant - 1
                #EN LUGAR DE PREGUNTAR SI ES PAR O NO DIRECTAMENTE LE AGREGO LA PARTE PAR asi: 
                res += cant // 2 * 2

        if res % 2 == 0 and res < len(s):
            res += 1

        return res
            
        