"""

Simple GET http request:

Here is a quick example using the Requests module.

Need to install Requests first:
» pip install requests

More info:
https://requests.readthedocs.io/en/master/

"""

# begin by importing the Requests module

import requests

# this is the url we are sending the http request to

url = "https://httpbin.org/get"

# here we execute the GET request, passing the url string we just defined above

resp = requests.get(url)

# Now, we have a request response object called: resp
# We will get all the information we need from the resp object

# getting the status code for the GET request
# this is useful when adding code to determine if the request was successful
# and/or handling errors

print(f"Status code: {resp.status_code}")

# Here we get the content of the response (in Unicode)

print(f"Response text: \n{resp.text}")
