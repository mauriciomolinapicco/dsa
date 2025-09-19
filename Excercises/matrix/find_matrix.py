"""
2610. Convert an Array Into a 2D Array With Conditions
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""

class Solution(object):
    def findMatrix(self, nums):
        seen = {}
        # recorro y guardo la cantidad de veces que aparece cada numero
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        res = []

        # el numero minimo de filas que voy a tener es la de la mayor cantidad que aparezca 
        # porque no puede haber items repetidos. Por cada valor itero n veces siendo n la cantidad de veces
        # que aparece. Si no existe la fila la creo (preguntando si i<len(res))
        for key, val in seen.items():
            for i in range(val):
                if i < len(res):
                    res[i].append(key)
                else:
                    res.append([key])
        
        return res