class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        # Generate hash maps
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0) #.get en hash me retorna el valor o si no existe el segundo valor
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        #iterate through the keys
        for i in hashS:
            if hashS[i] != hashT.get(i, 0):
                return False
        return True
    


        def isAnagramSolutionB(self, s, t):
            # creo una lista para las letras de uno y a medida que aparecen en el otro las elimino
            letters_t = []

            if len(s) != len(t):
                return False

            letters_t = [char for char in t]

            for char in s:
                if char in letters_t:
                    letters_t.remove(char)

            return letters_t == []