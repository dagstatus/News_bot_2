import sqlite3

from feeds import YandexMakhachkalaFeed
from Config import feeds_args, DB_PATH


def main(db_connect):
    # db_connect = sqlite3.connect(DB_PATH)
    feeds = [
        YandexMakhachkalaFeed(feeds_args['YandexMakhachkala']['url'], db_connect)
    ]

    for feed in feeds:
        feed.start()

if __name__ == '__main__':
    main()

