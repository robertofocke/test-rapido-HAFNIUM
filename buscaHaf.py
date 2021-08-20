import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings()

url=input('url: ')
rutasf=input('fichero con rutas: ')
with open(rutasf) as f:
        for linea in f:
                site=url+'/'+linea[:-1]
                resq=requests.get(site,verify=False)
                print (resq.status_code)
                if resq.status_code==200 and resq.text.find("<title>Error</title>")!=-1 and resq.text.find("<title>Outlook Web App</title>")!=-1:
                        print ('comprometido')
                        print (linea)

