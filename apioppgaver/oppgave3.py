import requests

lenkeapi = "https://openweathermap.org/city/3143244"
def hønefossVær():
    try:
        henteapi = requests.get(lenkeapi)
        if henteapi.status_code==200:
            print ("nå viser jeg været")
        else:
            print ("nå viser jeg ikke været")
        innhold = henteapi.json()
        print (type(innhold))
        print (innhold)
    except:
        print ("noe gikk feil")
hønefossVær()

#denne her var litte granne vanskelig ville jeg ha sagt