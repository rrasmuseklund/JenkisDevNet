import requests
import json
base_url = "https://172.20.20.2/restconf/data/"
headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}


system_endpoint = "Cisco-IOS-XE-native:native"
system_response = requests.get(url=f"{base_url}{system_endpoint}", auth=("admin","admin"), headers=headers, verify=False)
for info in system_response.json()["Cisco-IOS-XE-native:native"]["platform"]:
    print(info)