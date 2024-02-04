# Extract APIs from any URL:

This Python script extracts all the URLs (APIs) from a given website.

It uses `requests` libraries to make HTTP requests.

The code is well-documented with detailed docstrings explaining each method.

I made this code dynamic and so easy that anyone can understand!!

### Requirements:
1. Python
2. requests library :  Simplifies the process of making HTTP requests
3. re library : for regular expression

```python
import requests
import re

url = input("Enter a url: ")

response = requests.get(url)

print("Status Code:", response.status_code)

html_data = response.text 

url_pattern = re.compile(r'https?://\S+')

urls = url_pattern.findall(html_data)

for url in urls:
    print(url)

``` 