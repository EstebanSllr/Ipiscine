class serveur:
    def __init__(self, name, price, port):
        self.type = "serveur"
        self.name = name
        self.price = price
        self.port = port

class client:
    def __init__(self, name, price, port):
        self.type = "client"  
        self.name = name
        self.price = price
        self.port = port