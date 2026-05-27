import random

port_serveur_libre = list (range(1,4))

def serveur_port():

    
    if (len(port_serveur_libre) == 0):

        raise Exception("all port is used")
    
    else:

        random_index_serveur = random.randint(0, len(port_serveur_libre) -1)

        return port_serveur_libre.pop(random_index_serveur)

