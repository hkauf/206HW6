# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

# Retrieve all of the anchor tags
position = 18
count = 7

def newlink(url, position):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	new_url = tags[position-1].get('href')
	return new_url

for item in range(count):
	x = newlink(url, position)
	url = x
final = urllib.request.urlopen(url, context=ctx).read()
finalsoup = BeautifulSoup(final, 'html.parser')
print (finalsoup.title.string.split(' ')[2])