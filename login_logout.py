import requests

def login_fun(session,url,dic):
    session.post(url=url, data=dic)
    return session

def logout_fun(session,url):
    session.get(url)
    return session
