import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)
# print(tree)
counts = tree.findall('.//count')
# print(len(counts))
# print(type(counts))
# print(counts[0].text)

counts_length = len(counts)
cumulative_sum = 0

for item in counts:
    cumulative_sum += int(item.text)

print("Count:", counts_length)
print("Sum:", cumulative_sum)

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1511841.xml