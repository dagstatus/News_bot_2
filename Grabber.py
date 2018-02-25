# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sqlite3


def update_news (url_news,poisk):
    s=requests.get(url_news)
    b=BeautifulSoup(s.text,"html.parser")
    news_title= b.select(poisk)
    result_list=[]
    for x in news_title:
        temp_str=str(x)
        temp_str = temp_str.replace('<title>', '')
        temp_str = temp_str.replace('</title>', '')
        temp_str = temp_str.replace('<description>', '')
        temp_str = temp_str.replace('</description>', '')
        temp_str = temp_str.replace('<guid>', '')
        temp_str = temp_str.replace('</guid>', '')

        result_list.append(temp_str)


    return result_list

def cler_links (links):
    clear_links=[]
    for z_link in links:
        temp_str=str(z_link)
        temp_str = temp_str.replace('https://news.yandex.ru/yandsearch?cl4url=', '')
        temp_str = temp_str.replace('&amp;from=rss', '')
        temp_str = temp_str.replace('%2F', '/')
        clear_links.append(temp_str)
    return (clear_links)

def add_news_to_bd():
    zagolovki = update_news('https://news.yandex.ru/Makhachkala/index.rss', 'item title')
    news_full = update_news('https://news.yandex.ru/Makhachkala/index.rss', 'item description')
    links = cler_links(update_news('https://news.yandex.ru/Makhachkala/index.rss', 'item guid'))

    connect_bd = sqlite3.connect('News_bot_2/BD/NEWS_BD.db')
    # Открываем базу
    cursor = connect_bd.cursor()

    for x in range(len(zagolovki)):
        cursor.execute("""select title from News  where title=:title""",{"title":zagolovki[x]})
        result_sql = cursor.fetchall()

        if len(str(result_sql)) < 5:
            cursor.execute("""insert into News (title,description,link) values (:title,:description,:link)""",{"title": zagolovki[x], "description": news_full[x], "link": links[x]})

    connect_bd.commit()
    connect_bd.close()
    #Закрываем базу




add_news_to_bd()





