from dataclasses import dataclass
from typing import List

@dataclass
class Coso:
    numerador: int
    denominador: int
    b: float
    vertical: bool

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        v: List[Coso] = []

        for i in range(n):
            for j in range(i + 1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                c = Coso(0, 0, 0.0, False)
                c.numerador = y2 - y1
                c.denominador = x2 - x1

                if c.denominador == 0:
                    c.b = 0.0
                    c.vertical = True
                else:
                    c.b = - (float(c.numerador) / float(c.denominador)) * float(x1) + float(y1)
                    c.vertical = False

                v.append(c)

        max_points = 1
        for recta in v:
            contador = 0
            verticales: dict[int, int] = {}
            for i in range(n):
                if recta.vertical:
                    key = points[i][0]
                    verticales[key] = verticales.get(key, 0) + 1
                    if verticales[key] > max_points:
                        max_points = verticales[key]
                else:
                    left = float(points[i][1])
                    right = (float(recta.numerador) / float(recta.denominador)) * points[i][0] + recta.b
                    if abs(left - right) < 1e-4:
                        contador += 1

            if contador > max_points:
                max_points = contador

        return max_points