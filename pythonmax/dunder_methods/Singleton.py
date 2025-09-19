class Singleton:

    _instance = None   # es una variable de clase 

    def __new__(cls):

        """si la variable de clase _instance es None es que no hay ninguna instancia creada"""
        if cls._instance is None:
            
            """
            Este es el comportamiento por defecto de __new__, lo unico que no pregunta si hay una clase creada, 
            simplemente crea una por cada vez que se inicializa, lo que no queremos con el patron Singleton
            """
            cls._instance = super().__new__(cls)
            print("Creando instancia...")

        return cls._instance
    

c1 = Singleton() # se hace el print "creando instancia"
c2 = Singleton()  # no se hace ya que no se crea una nueva instancia

print(f"Son la misma instancia: {c1 is c2}")