import requests
from bs4 import BeautifulSoup

url = 'http://192.168.1.254/cgi-bin/broadbandstatistics.ha'

def getIP():
  try:
    res = requests.get(url)
    if res.status_code != 200:
      return ('FAIL', f'{res.status_code}')
    else:
      bbs = BeautifulSoup(res.text, features="html.parser")
      row = [ x for x in bbs.find(class_='table75').children if x != "\n"][4]
      return ('GOOD', f'{row.td.string}')
  except Exception as e:
    return ('FAIL', f'{e}')

