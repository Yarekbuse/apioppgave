import requests

lenkeapi = "https://catfact.ninja/fact"
def kattefakta():
    try:
        henteapi = requests.get(lenkeapi)
        if henteapi.status_code==200:
            print ("ting funker")
        else:
            print ("noe gikk feil")
        innhold = henteapi.json()
        print (type(innhold))
        print (innhold)
    except:
        print ("noe gikk feil")
kattefakta()