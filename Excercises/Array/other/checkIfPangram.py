# check if the sentence has all the letters in the english alphabet

class Solution(object):
    def checkIfPangram(self, sentence):
        alph = set()
        for letter in sentence:
            alph.add(letter)

        # it contains ONLY LOWERCASE ENGLISH LETTERS, so i just have to check if the total length is 26
        return len(alph) == 26
