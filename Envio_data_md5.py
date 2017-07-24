import requests
from login_logout import *
import hashlib

session = requests.sessions.Session()
url_in='http://0.0.0.0:5000/login_user/'

payload = {'username': 'renting', 'password': 'colombia'}

url_out='http://0.0.0.0:5000/logout_user'

session = login_fun(session,url_in,payload)

ruta = '/home/romel/Api_Cliente/viajes.xlsx.zip'
f= open(ruta, 'rb')

md5= hashlib.md5(f.read()).hexdigest()
f= open(ruta, 'rb')

token=session.cookies['csrftoken']

r =session.post('http://0.0.0.0:5000/send_data',files = {'file':f}, data={'csrfmiddlewaretoken': token,"MD5":md5,"name":"viajes"})
print r, r.text


session = logout_fun(session,url_out)
del session
