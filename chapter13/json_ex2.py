import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
# print(type(data))
# print(data)
print('Retrieved', len(data), 'characters')

cum_count = 0
cum_sum = 0

info = json.loads(data)
# print(info)
# print(dir(info))
# print(type(info))
# print('User count:', len(info))

for item in info["comments"]:
    cum_count += 1
    cum_sum += item["count"]

print("Count:", cum_count)
print("Sum: ", cum_sum)
# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1511842.json