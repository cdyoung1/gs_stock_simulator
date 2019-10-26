import requests
import json

client_id = "dd4f5d92f0f74a9daa0c0797b0599f41"
client_secret = "83bc449a19bec7e893201ea52a36895b67b07bfd5d28cd528e430f0874b3e337"

# client_id = r'b07a38d8dc7747d9aa78335ed51237dc'
# client_secret = r'a8982c5a8d3c136773f33f36b725da11418b0820aeb1a05fa877c743bc8d482d'

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

gsid_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI"
request_query = {
                "fields" : "financialReturnsScore,growthScore,multipleScore,integratedScore"
}
request = session.get(url=gsid_url, json=request_query)
results = json.loads(request.text)
gsid_dict = dict()

for asset in results["data"]:
  gsid = asset["gsid"]
  del asset["date"], asset["gsid"], asset["updateTime"]
  gsid_dict[gsid] = asset
  

# print(gsid_dict)

data_url = "https://api.marquee.gs.com/v1/assets/data?"
# for i in range(len(gsid)):
#   data_url += ("" if i == 0 else "&") + "gsid=" + gsid

for i, gsid in enumerate(gsid_dict.keys()):
  data_url += ("" if i == 0 else "&") + "gsid=" + gsid
  # if i == 5: break;

data_url += "&fields=gsid,name,type,assetClass"

# # print(data_url)
# data_url = "https://api.marquee.gs.com/v1/assets/data?"
data_query = {
              "scroll" : "1m"
}
headers = {
          "Authorization" : "Bearer " + access_token
}
data_request = requests.get(url=data_url, headers = headers, json=data_query)
# print(data_requ)
print(data_request)
data_results = data_request.json()
print(data_results)