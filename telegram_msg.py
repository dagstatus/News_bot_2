# -*- coding: utf-8 -*-
import sqlite3
import Config
import telepot
import codecs
import Grabber
import time


def News_message(db_connect):
    bot = telepot.Bot(Config.token)

    cursor = db_connect.cursor()
    cursor.execute("""select ID, title, link from News  where post_tg=0""")
    for _id, title, link in cursor.fetchall():
        bot.sendMessage('@news_05', '%s\n\n%s' % (title, link))
        cursor.execute("""update News set post_tg=1 where ID=:ID""", {"ID": _id})


def check_new_news(db_connect):
    cursor = db_connect.cursor()
    cursor.execute("""select count(*) from News where post_tg=0""")
    if cursor.fetchone()[0] > 0:
        return True

    return False


def main():
    db_connect = sqlite3.connect(Config.DB_PATH)
    Grabber.main(db_connect)
    if check_new_news(db_connect)>0:
        News_message(db_connect)
    db_connect.commit()
    db_connect.close()


if __name__ == '__main__':
    main()








