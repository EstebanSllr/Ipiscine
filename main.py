import json
import classe
from serveur import serveur_port
from client import client_port
import calculat
from open_config import json_import
import result  

instances = []
list_parck = json_import()

for i in list_parck:
    if i["type"] == "serveur":
        serveur_objet = classe.serveur(i["name"], i["price"], i["port"])
        serveur_objet.port = serveur_port()
        i["port"] = serveur_objet.port
        print("\nserveur: " + str(serveur_objet.name) + " | port: " + str(serveur_objet.port))
        instances.append(serveur_objet)
    
    if i["type"] == "client":
        client_objet = classe.client(i["name"], i["price"], i["port"])
        client_objet.port = client_port()
        i["port"] = client_objet.port
        print("client: " + str(client_objet.name) +"  | port: " +str(client_objet.port))
        instances.append(client_objet)

#ici on appel la fonction 
result.afficher_resultats(instances) 

with open("config.json","w") as test:
    json.dump(list_parck, test, indent=4)