import requests
import json

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : "dd4f5d92f0f74a9daa0c0797b0599f41",
    "client_secret" : "83bc449a19bec7e893201ea52a36895b67b07bfd5d28cd528e430f0874b3e337",
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
print(access_token_dict)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/coverage"

request_query = {
                    "where": {
                        "gsid": ["75154", "193067", "194688", "902608", "85627"]
                    },
                    "startDate": "2017-01-15",
                    "endDate":"2018-01-15"
               }

request = session.get(url=request_url, json=request_query)
results = json.loads(request.text)
data_dict = dict()

# for 

print(results)