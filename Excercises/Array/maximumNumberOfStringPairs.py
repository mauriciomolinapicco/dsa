# Best approach 
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        inverted = set()
        con = 0
        #Guardo una lista de las palabras invertidas
        for word in words:
            inv = word[::-1]
            # chequeo por las palabras que son capicuas para que no se 
            # sumen dos veces ya que la palabra va a ser igual cuando sea invertida
            if inv != word:
                inverted.add(inv)
        
        for word in words:
            if word in inverted:
                con += 1
        return con // 2

#Brute force
#O(n squared) runtime
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        n = len(words)
        con = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    con += 1

        return con
       