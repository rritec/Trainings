# Import packages urllib
from urllib.request import urlopen, Request
# provide any url
url = "https://www.rritec.com/"
# packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Print the data type of response
print("The Data Type of response object is : " + str((type(response))))
# Extract the response: html
html = response.read()
# Print the html
print(html)
# Be polite and close the response!
response.close()