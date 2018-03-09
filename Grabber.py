import sqlite3

from feeds import YandexMakhachkalaFeed
from Config import feeds_args, DB_PATH, ignore_links


def main():
    db_connect = sqlite3.connect(DB_PATH)

    feeds = [
        YandexMakhachkalaFeed(feeds_args['YandexMakhachkala']['url'], db_connect,ignore_links)
    ]

    for feed in feeds:
        feed.start()

if __name__ == '__main__':
    main()

