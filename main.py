import json
import classe
from serveur import serveur_port
from client import client_port


with open("config.json","r") as open_folder:
    list_parck = json.load(open_folder)

for i in list_parck:

    if i["type"] == "serveur":

        serveur_objet = classe.serveur(i["type"],i["name"],i["price"],i["port"])

        serveur_objet.port = serveur_port()

        print(serveur_objet.name)
       
    
    if i["type"] == "client":

        client_objet = classe.client(i["type"],i["name"],i["price"],i["port"])

        client_objet.port = client_port()
        
        print("client: " + str(client_objet.name) +" port: " +str(client_objet.port))
