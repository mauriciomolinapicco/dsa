
# mostWordsFound in a sentence
class Solution(object):
    def mostWordsFound(self, sentences):
        most_words = 0
        for sentence in sentences:
            words = 1
            for char in sentence:
                if char == " ":
                    words += 1
            if words > most_words:
                most_words = words
        return most_words
        