class Solution(object):
    def finalValueAfterOperations(self, operations):
        cont = 0
        for i in operations:
            if i in ["++X", "X++"]:
                cont += 1
            else: 
                cont -= 1
        return cont