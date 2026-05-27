# result.py
import calculat

def afficher_resultats(instances): 
    prix_serveurs = calculat.serveur_calcul(instances)
    prix_clients = calculat.client_calcul(instances)
    prix_total = calculat.total_calcul(instances)

    print("-" * 30)
    print(f"Total Serveurs : {prix_serveurs} €")
    print(f"Total Clients  : {prix_clients} €")
    print(f"Total Global   : {prix_total} €")
    print("-" * 30)