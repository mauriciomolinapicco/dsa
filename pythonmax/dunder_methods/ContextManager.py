class DatabaseConnection:
    def __init__(self, name):
        self.name = name
        self.connected = False
    
    def __enter__(self):
        self.connected = True
        print(f"Connecting to the db {self.name}")
        """El return es el valor que va a tener la variable. Ejemplo db en:
        with DatabaseConnection("Example db") as db:
        """
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connected = False
        print(f"Closed the connection...")
        if exc_type:
            print(f"An exception ocurred: {exc_value}")
        return True


with DatabaseConnection("Example db") as db:
    print(f"Is connected? {db.connected}")