import requests
from block.block import Block


class Parser(Block):
	def __init__(self, currency_name, url):
		super().__init__()
		self.par_version = "Akkacij 1.0 12.01.2022"
		self.par_url = url
		self.par_name = currency_name
		
		self.par_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'}
		self.par_html_page = requests.get(self.par_url, headers=self.par_headers)
