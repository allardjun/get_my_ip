#!/usr/bin/env python3

# run this on ricotta
# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/
from requests import get
import os

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

with open("ricotta","w") as f:
    f.write(f"ssh jun@{format(ip)} -p 23")

os.system("chmod a+x ricotta")

os.system("scp ricotta jun@ficus.ps.uci.edu:bin/ricotta")


