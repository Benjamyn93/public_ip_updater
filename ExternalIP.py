import requests
import re
import subprocess
import easygui
import pyperclip

### defines variable for a get request to grab the ip address using the requests module

r = requests.get("https://www.ipchicken.com")

### grabs the content object from the outpuut returned in the above variable.
### The content is what contains the html or text on the site

b = r.content

### Converts the above variable into a string or else the regex we use on it will not work with the re module

btostring = str(b)

### Runs a regex command to find ip addresss from the above variable

ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', btostring )

### Converts the above variable into a string or else the below easygui module will not take the input

stringIP = str(ip)

### Pop up box which displays your current ip address.
### It uses the returned output of the above variable to display your ip address.

easygui.buttonbox('This is your external IP Address', 'IP Address', (ip))

### Adds the returned output of the stringIP variable a.ka. your ip address to your clipboard

pyperclip.copy(stringIP)
