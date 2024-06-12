"""
TD07
Marc Rougagnou
Groupe DS4
"""

#%% Exercice 1
import json
import requests
url="http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=UkhfSA9xV3VSf1tsVCIAKVkxBTALfQYhUS0GZQlsXiMIYwRlVTUGYFA%2BVCkGKVdhWXRQMwA7BjYAa1cvD30HZlI4XzMPZFcwUj1bPlR7ACtZdwVkCysGIVEwBmEJbV4jCGkEYFUwBnpQN1QoBjVXZ1l1UC8APgY5AGJXNw9nB2NSM184D2pXN1IiWyZUYgAyWWwFZQs1Bj1RMgYwCWNeOgg%2BBGFVNAZhUCFUMgY%2FV2pZYlA1ADcGNwBiVy8PfQcdUkJfJg8sV3dSaFt%2FVHkAYVk0BTE%3D&_c=0202debf05db9d1cf5f500618f9af326"


try:
    api_request=requests.get(url)
    data=json.loads(api_request.content)
except Exception as e:
    data="Error ... "
#%% partie D

print(type(data))
for k in data.items():
    print(k)

#%% partie E

for k, v in data.items():
    if k=="request_state" or k=="request_key" or k=="message" or k=="model_run" or k=="source":
        print(k,v,"\n")

#%% partie F

del(data["request_state"])
del(data["request_key"])
del(data["message"])
del(data["model_run"])
del(data["source"])

#%% partie G

print(data['2024-06-10 08:00:00'],"type ",type(data['2024-06-10 08:00:00']))

#%% partie h

print(data['2024-06-10 08:00:00']["temperature"]["2m"])   
print(data['2024-06-10 08:00:00']["temperature"]["sol"])

#%% partie i

print(data['2024-06-10 08:00:00']["humidite"])

#%% partie j

from datetime import datetime 

dt=datetime.strptime("2024-06-09 08:00:00", "%Y-%m-%d %H:%M:%S")
print(type(dt))
print(dt)

#%% partie k

lesDates=[datetime.strptime(k, "%Y-%m-%d %H:%M:%S") for k in data.keys()]
lesTempA2m=[data[k]["temperature"]["2m"]-273.15 for k in data.keys()]
lesTempAuSol=[data[k]["temperature"]["sol"]-273.15 for k in data.keys()]
lesHumiditesA2m=[data[k]["humidite"]["2m"] for k in data.keys()]

#%% partie  i
import matplotlib.pyplot as plt

#%% partie m
fig,(ax,ax1)=plt.subplots(2)
ax.plot(lesDates,lesTempA2m,"y-o")
ax.plot(lesDates,lesTempAuSol,"b-o")
ax1.plot(lesDates,lesHumiditesA2m,"r-o")
ax1.grid()
ax.grid()
ax.axes.set_ylabel("température")
ax1.axes.set_ylabel("humidité")

#%% partie avec pandas
"""
import pandas as pd
import json
import requests
url="http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=UkhfSA9xV3VSf1tsVCIAKVkxBTALfQYhUS0GZQlsXiMIYwRlVTUGYFA%2BVCkGKVdhWXRQMwA7BjYAa1cvD30HZlI4XzMPZFcwUj1bPlR7ACtZdwVkCysGIVEwBmEJbV4jCGkEYFUwBnpQN1QoBjVXZ1l1UC8APgY5AGJXNw9nB2NSM184D2pXN1IiWyZUYgAyWWwFZQs1Bj1RMgYwCWNeOgg%2BBGFVNAZhUCFUMgY%2FV2pZYlA1ADcGNwBiVy8PfQcdUkJfJg8sV3dSaFt%2FVHkAYVk0BTE%3D&_c=0202debf05db9d1cf5f500618f9af326"

dfjson=pd.read_json(url,orient='index')
print(dfjson)

#dfjson = dfjson.drop(dfjson["request_state","source","request_key","message","model_run"], axis=0)


#dfjson.index=pd.to_datetime( )
#dfsplited = pd.json_normalize( )


"""
import pandas as pd
import requests

url = "http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=UkhfSA9xV3VSf1tsVCIAKVkxBTALfQYhUS0GZQlsXiMIYwRlVTUGYFA%2BVCkGKVdhWXRQMwA7BjYAa1cvD30HZlI4XzMPZFcwUj1bPlR7ACtZdwVkCysGIVEwBmEJbV4jCGkEYFUwBnpQN1QoBjVXZ1l1UC8APgY5AGJXNw9nB2NSM184D2pXN1IiWyZUYgAyWWwFZQs1Bj1RMgYwCWNeOgg%2BBGFVNAZhUCFUMgY%2FV2pZYlA1ADcGNwBiVy8PfQcdUkJfJg8sV3dSaFt%2FVHkAYVk0BTE%3D&_c=0202debf05db9d1cf5f500618f9af326"

# Désactiver la vérification SSL
response = requests.get(url, verify=False)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    dfjson = pd.DataFrame.from_dict(data, orient='index')
    print(dfjson)  # Afficher les premières lignes du DataFrame
else:
    print(f"Erreur lors de la requête : {response.status_code}")








