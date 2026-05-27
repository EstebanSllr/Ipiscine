def serveur_calcul(liste_instances):
    
    total = 0
    
    for obj in liste_instances:
        if obj.type == "serveur":
            total += int(obj.price)
    return total 


def client_calcul(liste_instances):  
    
    total = 0
    
    for obj in liste_instances:
        if obj.type == "client":
            total += int(obj.price)
    return total  


def total_calcul(liste_instances):  
    
    total_serveurs = serveur_calcul(liste_instances)
    total_clients = client_calcul(liste_instances)
    return total_serveurs + total_clients