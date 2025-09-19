class Solution(object):
    """
    input = string with stars
    tengo que eliminar el character que esta a la izquierda de la * y la *
    Ejemplo input = leet**cod*e
        el output seria = lecoe
    """
    def removeStars(self, s):
        # podria usar un string pero como es inmutable, las operaciones son mas lentas ya que tiene que recrear el str entero
        # con una lista, el tiempo para hacer append y pop en O(1), en str seria O(n)
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)