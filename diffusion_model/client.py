import requests
import json

reqUrl = "127.0.0.1:5000/?prompt=panda eating ice cream"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "prompt" : "cute anime girl eating ice cream"
})

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)