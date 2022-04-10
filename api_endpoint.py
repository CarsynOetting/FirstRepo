import json
import SSL
import urllib.request, urllib.parse, urllib.error

serviceurl = input("URL address: ")
if len(serviceurl) < 1:
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

loc = input("What is the location you are trying to reach?: ")
