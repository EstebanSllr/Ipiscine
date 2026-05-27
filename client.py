import random

port_client_libre = list(range(1,17))


def client_port():

    try:

        random_index_client = random.randint(0, len(port_client_libre) -1)

        return port_client_libre.pop(random_index_client)
    
    except ValueError as e:

        print("\nto much client (max 16)")
        print("code error: " +str(e) + "\n")


     