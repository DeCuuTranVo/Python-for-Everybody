# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# print(soup)

# # Retrieve all of the anchor tags
tags = soup('span')

cumulative_sum = 0
cumulative_count = 0
# print(tags)
for tag in tags:
    # # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    cumulative_count += 1
    cumulative_sum += int(tag.contents[0])

print("Count", cumulative_count)
print("Sum", cumulative_sum)