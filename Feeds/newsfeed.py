import urllib.request as RE
import xml.etree.ElementTree as ET

url = 'http://rss.cnn.com/rss/edition.rss'
data = RE.urlopen(url).read()
tree = ET.fromstring(data)

print('This are the latest News at the BBC:\n')

for i in tree.iter('item'):
    print('{}\n{}\n'.format(i.find('title').text, i.find('description').text))
