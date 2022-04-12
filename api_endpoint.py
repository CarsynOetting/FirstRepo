import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = input("URL address: ")
    if len(serviceurl) < 1:
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'

else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)


while True:
    address = input("What is the location you are trying to reach?: ")

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    if len(address) < 1:break
    un = urllib.request.urlopen(url, context=ctx)
    data = un.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place = js['results'][0]['place_id']

    print(place)
