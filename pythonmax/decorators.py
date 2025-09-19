def my_decorator(func):
    def wrapper():
        print("hacer esto antes de la funcion")
        func()
        print("hacer esto DESPUES de la funcion")
    return wrapper


@my_decorator
def funcion1():
    print("Soy una funcion")

funcion1()

"""OUTPUT
hacer esto antes de la funcion
Soy una funcion
hacer esto DESPUES de la funcion"""