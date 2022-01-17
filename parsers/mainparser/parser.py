import requests


class Parser:
	def __init__(self, currency_name, url):
		self.url = url
		self.name = currency_name
		
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'}
		self.html_page = requests.get(self.url, headers=self.headers)
