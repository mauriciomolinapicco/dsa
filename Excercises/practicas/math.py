print(5/2) #2.5
print(5//2) #2

print(-3 // 2) #redondea para abajo, me da -2
# si quiero que redondee para arriba tengo que castearlo a int
print(int(-3 / 2))


import math 
print(math.floor(3.2))
print(math.ceil(4.0000001)) # 5

#maximum number
float("inf")
float("-inf")

#potencia
print(f"potencia a la 3 de 10: {math.pow(10, 3)}")