## From url extract all the API's behind it.
import requests
import re

# User will give the url as input:
url = input("Enter a url: ")

# Send a GET request to the URL
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Get the HTML content of the response
html_data = response.text #With this we can get all the html code behind the website.

# Define a regular expression pattern to match urls
url_pattern = re.compile(r'https?://\S+')

# Find all urls in the HTML data using the regular expression
urls = url_pattern.findall(html_data)

# using for loop to print all the api's:
for url in urls:
    print(url)
