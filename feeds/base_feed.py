
class BaseFeed:

	def __init__(self, url, db_connect):
		self.name = type(self).__name__
		self.url = url
		self.db = db_connect
		self.c = self.db.cursor()
		self.entries = []

	def start(self):
		self.parse()
		self._save_entries()

	def parse(self):
		pass

	def _save_entries(self):
		print('%s: save to db' % self.name)
		# TODO: logging
		if self.entries is None or len(self.entries) == 0:
			return

		for entry in self.entries:
			self.c.execute("""select count(*) from News where link=:link""", {"link":entry['link']})
			if self.c.fetchone()[0] > 0:
				continue
			self.c.execute("""insert into News (title,link) values (:title,:link)""", entry)
		self.db.commit()
