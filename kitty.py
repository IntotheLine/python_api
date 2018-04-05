#Kitty.py

from urllib2 import Request, urlopen, URLError

request = Request("https://placekitten.com/400/300")

try:
	response = urlopen(request)
	kittens = response.read()
	print(kittens(559:1000))
except URLError:
	print("All Cats are dead"), e 
  
  #https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1
