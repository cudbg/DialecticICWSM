import requests
from random import choice
from string import ascii_uppercase
import logging
import time


try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def randString(count):
	return (''.join(choice(ascii_uppercase) for i in range(count))) + str(time.time())


def AnalyzeLIWC(content_string):
	headers = {'Content-Type':'application/json','X-API-SECRET-KEY':'nvcQaeY9wQSh5CLiZpnHsVhUyHcL4iJ27uSPwWl2D28', 'X-API-KEY': '58d74719e53b0b05af52cf05'}
	

	print(headers)
	content = {"content_tags": [], "language": "english","content_source": 4,  "language_content": content_string}

	js = {"name":randString(20),"person_tags": [], "gender":0, "content":content, "person_handle": randString(20) }

	r = requests.post('https://app.receptiviti.com/v2/api/person', headers=headers,json=js)

	# print(r)
	# print(r.json())

	return r


if __name__ == '__main__':
	AnalyzeLIWC("Hello world my name is Hamed!!")