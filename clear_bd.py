import datetime
import sqlite3
import Config

def clear_bd ():
    connect_bd = sqlite3.connect(Config.DB_PATH)
    cursor = connect_bd.cursor()

    date_now=datetime.date.today()
    print(date_now)
    cursor.execute("""select ID,date_news from News where post_tg=1""")
    for _id, date_news in cursor.fetchall():
        date_news=datetime.datetime.strptime(date_news,'%Y-%m-%d')
        delta=date_now-date_news.date()
        if (delta.days>1):
            print('delete old news where id=', _id)
            cursor.execute("""Delete from News where ID=:ID""", {"ID": _id})
    connect_bd.commit()



clear_bd()