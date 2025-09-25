""" 
resumiendo consigna:
separar el string en k pedazos y que cada pedazo no tenga repetidos
"""
def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0,len(string), k)]
    
    for s in substrings:
        seen = set()
        subst = ""
        for char in s:
            if char in seen:
                continue
            seen.add(char)
            subst += char
        print(subst)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
