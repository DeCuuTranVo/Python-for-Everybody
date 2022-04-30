# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def get_link_at_position(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = list(soup('a'))
    # print(type(tags))
    # print(type(list(tags)))
    
    # print(tags[position -1].get('href', None))

    return tags[position -1].get('href', None)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
link_count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("Retrieving:", url[5:])

for i in range(link_count):
    url = get_link_at_position(url, position)
    print("Retrieving:", url)





