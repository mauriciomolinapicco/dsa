class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            # pregunto si tiene siguiente
            if i + 1 < len(s):
                if roman[s[i]] >= roman[s[i+1]]:
                    # si i+1 es mayor a i sumo el valor, sino lo resto
                    num += roman[s[i]]
                else:
                    num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num 