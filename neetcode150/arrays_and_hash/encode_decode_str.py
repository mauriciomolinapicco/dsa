class Solution:
    def encode(self, strs) -> str:
        encoded = ""
        encoded += str(len(strs))
        encoded += "|"
        for word in strs:
            tamanio = len(word)
            encoded += str(tamanio)
            encoded += "#"
            encoded += str(word)
            print(encoded)
        return encoded
        # 3|4hola3que7gracias

    def decode(self, s: str) -> List[str]:
        words_amount = ""
        for c in s:
            if c != "|":
                words_amount += c
            else:
                break
        words_amount = int(words_amount)

        s = s.split("|")[1:]
        s = ("").join(s)

        result = []
        p = 0
        count = 0
        word_started = False
        word_length = ""
        word = ""

        while count < int(words_amount):
            print(s)
            print("Palabra: " + word)
            if word_started:
                if p < int(word_length):
                    word += s[p]
                else:
                    count += 1
                    word_started = False
                    result.append(word)
                    s = s[p:]
                    p = 0
                    word_length = ""
                    word = ""
                    print(result)
                    continue
            else:
                print(s)
                if s[p] != "#":
                    word_length += s[p]
                else:
                    word_started = True
                    s = s[p+1:]
                    p = 0
                    print("largo: " + word_length + " resto de s: " + s)
                    continue
            p += 1
        return result