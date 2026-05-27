import random

port_client_libre = list(range(1,17))


def client_port():
     
    
        if (len(port_client_libre) == 0):

            raise Exception("all port is used")

        else:
    
            random_index_client = random.randint(0, len(port_client_libre) -1)

            return port_client_libre.pop(random_index_client)




     
     




