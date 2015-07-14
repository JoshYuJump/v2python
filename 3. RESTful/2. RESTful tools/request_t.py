import requests

# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2421.0 Safari/537.36"}
# r = requests.get('http://127.0.0.1:5000/index', headers=headers, timeout=1)
# print r.text

r = requests.get('http://127.0.0.1:5000/login', auth=('josh', '123456'))
print r.text