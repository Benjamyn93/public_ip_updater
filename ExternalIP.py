import requests
import re
import subprocess
import easygui

r = requests.get("https://www.ipchicken.com")
b = r.content
btostring = str(b)
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', btostring )
#print(ip)

easygui.buttonbox('This is your external IP Address', 'IP Address', (ip))
