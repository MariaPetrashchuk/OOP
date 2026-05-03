import requests

print(requests.__version__)
r = requests.get('https://google.com')
print(r.status_code)