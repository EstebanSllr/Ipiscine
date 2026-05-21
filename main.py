from fonction import serveur_port,client_port,config

port_client_libre = list(range(1,17))
port_serveur_libre = list (range(1,4))

list_parc = config()

serveur_verif = ["serveur","SERVEUR","Serveur"]

if list_parc[0][0] in serveur_verif:

    port_serveur = serveur_port(port_serveur_libre)

    print(port_serveur)