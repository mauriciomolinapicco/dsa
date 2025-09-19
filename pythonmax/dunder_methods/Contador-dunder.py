class Contador():
    def __init__(self):
        self.value = 0

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f"Value= {self.value}"

    def __repr__(self):
        return f"The value is {self.value}"

    def __add__(self, other): #other is whatever is on the right side of the +
        if isinstance(other, Contador):
            return self.value + other.value

        try:
            #seria el caso que se pasa un int en lugar de un Contador
            return self.value + int(other)
        except:
            raise ValueError("Invalid parameter")
        
c1 = Contador()
c1.count_up()
c1.count_up()

c2 = Contador()
c2.count_up()

print(c1,c2)
print(c1+c2) # antes de crear la funcion __add__ me da error al hacer +. Puedo hacer un metodo para esto
print(c1+"asfd")