class Solution(object):
    def findWordsContaining(self, words, x):
        #words es una lista de palabras y x un caracter. TEngo que devolver los indices de las words que contengan el char x
        lista = []
        for i in range(len(words)):
            if x in words[i]:
                lista.append(i)
        return lista