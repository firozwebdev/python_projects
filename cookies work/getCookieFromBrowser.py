import requests
# import browsercookie
import urllib.request as urllib2
import re
import browser_cookie3

# cj = browsercookie.Firefox()
# r = requests.get('https://elements.envato.com',)
#
# print(r)

# title = lambda html: re.findall('<title>(.*?)</title>', html, flags=re.DOTALL)[0].strip()
# #
# url = 'https://elements.envato.com/'
# public_html = urllib2.urlopen(url).read()
# title(public_html)


# cj = browser_cookie3.firefox()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# login_html = opener.open("https://elements.envato.com/").read()
# title(login_html)

# import browser_cookie3
# import requests

# r = requests.get(url, cookies=cj)
# title(r.content)


# from urllib.request
# import Request, urlopen
cj = browser_cookie3.Firefox()
print(cj)
# req = Request(
#     url='https://elements.envato.com/',
#     headers={'User-Agent': 'Mozilla/5.0'},
#
# )
#
# webpage = urlopen(req).read()
# print(webpage)


# from urllib.request import Request, urlopen
#
# # Function to get the page content
# def get_page_content(url, head):
#   """
#   Function to get the page content
#   """
#   req = Request(url, headers=head)
#   return urlopen(req)
#
# url = 'https://example.com'
# head = {
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#   'Accept-Encoding': 'none',
#   'Accept-Language': 'en-US,en;q=0.8',
#   'Connection': 'keep-alive',
#   'refere': 'https://example.com',
#   'cookie': """your cookie value ( you can get that from your web page) """
# }
#
# data = get_page_content(url, head).read()
# print(data)

# s = requests.Session()
# s.get('https://elements.envato.com/',auth=('balarkpowersys@gmail.com','AZn20222426@@##'))
# print(s.cookies)

from requests import session
from bs4 import BeautifulSoup

payload = {
    'action'   : 'login',
    'username' : '',
    'password' : ''
}
login_url='https://elements.envato.com/sign-in'

with session() as c:
    c.post(login_url, data = payload)
    request = c.get('http://ideone.com/myrecent')
    print (request.headers)
    print (request.text)