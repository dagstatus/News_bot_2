from urllib  import parse
from xml.etree import ElementTree 
import requests
import datetime

from .base_feed import BaseFeed

class YandexMakhachkalaFeed(BaseFeed):

	def parse_link(self, ya_link):
		url = parse.parse_qs(parse.urlparse(ya_link).query)
		url = url['cl4url'][0] if 'cl4url' in url else ya_link
		if 'http' not in url[:4]:
			url = 'http://'+url
		return url

	def parse(self):
		print('%s: parsing data' % self.name)
		# TODO: logging
		r = requests.get(self.url)
		root = ElementTree.fromstring(r.content)
		entries = []
		for child in root[0].findall('item'):
			entries.append({
				'link': self.parse_link(child.find('link').text),
				'title': child.find('title').text,
				'date_news': datetime.date.today()
			})

		self.entries = entries