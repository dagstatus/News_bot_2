# -*- coding: utf-8 -*-
import sqlite3
import Config
import telepot
import codecs
import Grabber
import time








def clearning_msg(input_msg):
    temp_str = str(input_msg).replace('[(', '')
    temp_str = temp_str.replace(',)]', '')
    return (temp_str)


def clearning_msg_text(input_msg):
    temp_str = str(input_msg).replace('[(', '')
    temp_str = temp_str.replace(',)]', '')
    temp_str=temp_str[1:-1]
    return (temp_str)


def News_message():
    bot = telepot.Bot(Config.token)


    connect_bd = sqlite3.connect('News_bot_2/BD/NEWS_BD.db')
    # Открываем базу
    cursor = connect_bd.cursor()
    cursor.execute("""select ID from News  where post_tg=0 limit 1""")
    news_id = clearning_msg(cursor.fetchall())
    final_msg = ''
    cursor.execute("""select title from News  where ID=:ID limit 1""", {"ID": news_id})
    final_msg=cursor.fetchall()
    final_msg=codecs.encode(clearning_msg_text(final_msg), 'utf-8')
    cursor.execute("""select link from News  where ID=:ID limit 1""", {"ID": news_id})
    link = cursor.fetchall()
    cursor.execute("""update News set post_tg=1 where ID=:ID""", {"ID": news_id})
    connect_bd.commit()
    #update after post in telegram and set post_tg=1
    bot.sendMessage('@news_05',final_msg)
    bot.sendMessage('@news_05',clearning_msg_text(link))
    connect_bd.close()




def check_new_news():
    have_mews=0
    connect_bd = sqlite3.connect('News_bot_2/BD/NEWS_BD.db')
    # Открываем базу
    cursor = connect_bd.cursor()
    cursor.execute("""select title from News  where post_tg=0 limit 1""")
    final_msg = cursor.fetchall()
    final_msg = codecs.encode(clearning_msg_text(final_msg), 'utf-8')
    if len(str(final_msg)) > 5:
        have_mews=1

    connect_bd.close()
    return (have_mews)





Grabber.add_news_to_bd()
if check_new_news()>0:
    News_message()





