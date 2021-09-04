import json
import requests
from random import randrange
import time


url = "http://192.168.0.103/api/glybzbW9HU7WbJqfj8yvM5oT66RiUTriPGh4X0A5/lights/1/state"

hue = 2000
on = True

while True:
    time.sleep(0.001)
    if hue < 60000:
        hue = hue+200
        data_on = {"on": True, "sat":254,"bri":254, "hue":hue}
        r = requests.put(url, json.dumps(data_on), timeout=5)
        print("Hue Color: ", hue, "/60000")
        
    else:
        hue = 1
        data_on = {"on": True, "sat":254,"bri":254, "hue":hue}
        r = requests.put(url, json.dumps(data_on), timeout=5)
        print("Restart")

