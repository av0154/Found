import json
import pprint
import requests

base_url = "https://192.168.56.1:8834"
verify = False 
access_key = "av0154"
secret_key = "Foundathon123"

def get(destination):
  return requests.get("{}/{}".format(base_url, destination),
                      verify  = verify,
                      headers = {"X-ApiKeys": "accessKey={}; secretKey={}".format(access_key, secret_key)})

def post(destination, data):
  return requests.post("{}/{}".format(base_url, destination),
                       verify  = verify,
                       headers = {"X-ApiKeys": "accessKey={}; secretKey={}".format(access_key, secret_key)},
                       data    = data)


scans_request = get("scans")
scans = scans_request.json()["scans"]

for scan in scans:
  hosts_request = get("scans/{}".format(scan["id"]))
  hosts = hosts_request.json()["hosts"]
  for host in hosts:
    host_details_request = get("scans/{}/hosts/{}".format(scan["id"], host["host_id"]))
    host_details = host_details_request.json()
    for vulnerability in host_details["vulnerabilities"]:
      
      if vulnerability["severity"] > 0:
       
        output = {"host": vulnerability["hostname"],
                  "vulnerability": vulnerability["plugin_name"],
                  "severity": vulnerability["severity"]}
        pprint.pprint(output)
