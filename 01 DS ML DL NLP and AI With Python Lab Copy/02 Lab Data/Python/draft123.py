# Import packages
from urllib.request import urlopen, Request
# Specify the url
url = "https://www.rritec.com/"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Print the data type of response
print("the Data Ttpe of response object is : " + str((type(response))))
# Extract the response: html
html = response.read()
# Print the html
print(html)
# Be polite and close the response!
response.close()

