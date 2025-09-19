"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

"""
class Solution(object):
    def groupThePeople(self, groupSizes):
        n = len(groupSizes)
        # hash que va a almacenar como clave el tamano del grupo y dentro de esta clave va a 
        # tener la lista con los ID o posiciones de los que tienen ese group size 
        sizes = {}
        result = [] # sera una lista de listas
        for i, l in enumerate(groupSizes):
            # Si ya almacene algun ID con el size l le hago append sino creo una lista para el valor 
            # solamente con el valor i
            if l in sizes:
                sizes[l].append(i)
            else:
                sizes[l] = [i]

            #Esto es cuando el grupo se llena, lo que hago es append al array resultado y limpio la 
            # casilla para el valor del size del grupo para poder adicionar a la siguiente 
            # posible tanda que puede tener el mismo group size 
            if len(sizes[l]) == l:
                result.append(sizes[l])
                sizes[l] = []
        return result