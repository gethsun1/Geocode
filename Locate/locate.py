
from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML


api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'


address = input('Enter address: ')
if len(address) < 1:
    address = 'Nairobi, Kenya'


url = api_url + ENCODE({'address': address})


data = OPEN(url).read()

tree = XML.fromstring(data)

res = tree.findall('result')


lat = res[0].find('geometry').find('location').find('lat').text

lng = res[0].find('geometry').find('location').find('lng').text


lat = float(lat)
lng = float(lng)
lat_c = 'S' if lat < 0 else 'N'
lng_c = 'W' if lng < 0 else 'E'


location = res[0].find('formatted_address').text


print("==>", location, "<==")
print('Latitude: {0:.3f}{1}'.format(abs(lat), lat_c))
print('Longitude: {0:.3f}{1}'.format(abs(lng), lng_c))
