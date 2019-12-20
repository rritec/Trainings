
from urllib.request import urlopen,Request
url = 'https://www.facebook.com'
my_request = Request(url)
my_response = urlopen(my_request)
print(type(my_response))
#print(my_response.read())
