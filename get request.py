import requests
r = requests.get('http://google.com', headers={'X-Platform': 'RaspberryPi'})
print (r.status_code)
print (r.headers)
print (r.text[0:100])
