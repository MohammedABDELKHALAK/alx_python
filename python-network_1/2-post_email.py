import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.text)
else:
    print("Request failed with status code: {}".format(response.status_code))
