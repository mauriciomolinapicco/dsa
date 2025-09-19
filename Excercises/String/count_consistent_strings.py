# cuantas palabras de la lista word estan contenidas solo por letras del str allowed
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        con = 0
        for word in words:
            flag = True
            for c in range(len(word)):
                if word[c] not in allowed:
                    flag = False
                    break
            if flag:
                con += 1
        return con
        