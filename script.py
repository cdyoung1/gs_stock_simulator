import requests
import json

# client_id = "dd4f5d92f0f74a9daa0c0797b0599f41"
# client_secret = "83bc449a19bec7e893201ea52a36895b67b07bfd5d28cd528e430f0874b3e337"

client_id = r'b07a38d8dc7747d9aa78335ed51237dc'
client_secret = r'a8982c5a8d3c136773f33f36b725da11418b0820aeb1a05fa877c743bc8d482d'

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : client_id,
    "client_secret" : client_secret,
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

coverage_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/coverage?limit=1000"
request = session.get(url=coverage_url)
results = json.loads(request.text)
gsid_list = []

for c in results['results']:
  gsid_list.append(c['gsid'])

print(gsid_list)

# assets_url = "https://api.marquee.gs.com/v1/assets?"

# for i in range(2):
#   separator = ("" if i == 0 else "&")
#   assets_url += separator + "gsi=" + gsid_list[i]

# assets_request = session.get(url=assets_url)
# assets_results = json.loads(assets_request.text)

# print(assets_results)