import requests

r = requests.get("https://www.ipchicken.com")
print(r.content)