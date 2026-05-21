import random


port_client_libre = list(range(1,17))
port_serveur_libre = list (range(1,4))
list_parc = []



def client_port(storage_client):

        if (len(port_client_libre) == 0):

            raise Exception("all port is used")

        else:

            random_index_client = random.randint(0, len(port_client_libre) -1)

            storage_client = port_client_libre.pop(random_index_client)

            print ("le port du client ... est: " + str(storage_client))


client_port(0)

print (port_client_libre)



def serveur_port(storage_serveur):

    if (len(port_serveur_libre) == 0):

        raise Exception("all port is used")

    else:

        random_index_serveur = random.randint(0, len(port_serveur_libre) -1)

        storage_serveur = port_serveur_libre.pop(random_index_serveur)

        print ("le port du serveur ... est: "+ str (storage_serveur))


serveur_port(0)

print(port_serveur_libre)




def config():


    with open("config.txt", "r") as fichier:



        for line in fichier:

            line_clear = line.strip()

            element_cut = line_clear.split(".")

            list_parc.append(element_cut)



config()

print (list_parc)