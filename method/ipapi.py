import requests

url = 'https://ipapi.co/ip'

def getIP():
  try:
    res = requests.get(url)
    if res.status_code != 200:
      return ('FAIL', f'{res.status_code}')
    else:
      return ('GOOD', f'{res.text}')
  except Exception as e:
      return ('FAIL', f'{e}')

