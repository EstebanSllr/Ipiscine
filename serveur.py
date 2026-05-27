import random

port_serveur_libre = list (range(1,4))

def serveur_port():

    
    try:
           
        random_index_serveur = random.randint(0, len(port_serveur_libre) -1)

        return port_serveur_libre.pop(random_index_serveur)

    except ValueError as e:
        print("\nto much serveur (max 3)")
        print("error code: "+ str(e) +"\n")
        exit(1)