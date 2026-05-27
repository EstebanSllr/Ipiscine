import json

def json_import():
    
    try:
        with open ("config.json","r") as open_folder:
            return json.load(open_folder)

    except FileNotFoundError as e:
        print("json incorrect")
        print("error code",e)
        exit(1)