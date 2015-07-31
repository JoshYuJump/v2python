import requests

r = requests.get('http://localhost:5000/client/login')
print r.text
print '=' * 6
print r.history
