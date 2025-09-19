# given a list of words return the words translated to morse code

def char_to_morse(self, words):
    abc = "abcdefghijklmnopqrstuvwxyz"
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    mapa = {}
    res = []

    for a, m in zip(abc, morse):
        mapa[a] = m
    
    for word in words:
        cadena = ""
        for char in word:
            cadena += mapa[char]
        res.append(cadena)
    
    return res