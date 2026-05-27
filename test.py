import random

port_serveur_libre = list (range(1,4))

def serveur_port():

    
    try:
        len (port_serveur_libre) == 0
    except ValueError as e:
        print("port all used")
        print("error code ",e)
        exit(1)
    
    

        random_index_serveur = random.randint(0, len(port_serveur_libre) -1)

        return port_serveur_libre.pop(random_index_serveur)