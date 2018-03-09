
class BaseFeed:

	def __init__(self, url, db_connect, ignore_ll):
		self.name = type(self).__name__
		self.url = url
		self.db = db_connect
		self.c = self.db.cursor()
		self.entries = []
		self.ignore_ll=ignore_ll

	def start(self):
		self.parse()
		self._save_entries()

	def parse(self):
		pass

	def _save_entries(self):
		Ignore_count=0
		print('%s: save to db' % self.name)
		# TODO: logging
		if self.entries is None or len(self.entries) == 0:
			return

		for entry in self.entries:
			ignore_find=False
			self.c.execute("""select count(*) from News where title=:title""", {"title":entry['title']})
			if self.c.fetchone()[0] > 0:
				continue
			for igg_l in self.ignore_ll:
				if (str(entry['link']).find(igg_l))>-1:
					ignore_find=True
					Ignore_count=Ignore_count+1
			if ignore_find==True:
				continue
			self.c.execute("""insert into News (title,link,date_news) values (:title,:link,:date_news)""", entry)
		self.db.commit()
		print('%s: Ignored' % self.name, Ignore_count)
