class Solution(object):        
    def groupAnagrams(self, strs):
        result = []
        diccionario = {}

        for i in range(len(strs)):
            l = diccionario.get(str(sorted(strs[i])), [])
            l.append(i)
            diccionario[str(sorted(strs[i]))] = l
        
        for k, l in diccionario.items():
            sub_list = [strs[i] for i in l]
            result.append(sub_list)

        return result
    