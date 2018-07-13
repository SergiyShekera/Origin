'''Парсит укр.нет и выводит в консоль 3 главных новости,
паралельно занося их в базу данных'''

import urllib.request
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MyTable(Base):
        __tablename__ = 'news_table'

        id = Column(Integer, primary_key=True)
        news = Column(Text)
       
        def __init__(self, news):
                self.news = news

        def __repr__(self):
                return "<MyTable(%s)>" % (self.news)
           
engine = create_engine('postgresql://postgres:root@localhost/test_db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)        

def site(url):

    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):

    soup = BeautifulSoup (html, "lxml")

    ddata = soup.find('article')
    for row in ddata.find_all('ul'):
        n = soup.find_all('li')
        n1 = n[0].text.strip()
        n2 = n[1].text.strip()
        n3 = n[2].text.strip()
        news = 'Три главные новости: \n'
        print(news + n1 + '\n' + n2 + '\n' + n3)
        print('')
        print('Занести ли новости в базу даннных?')
        i = input('для ответа введи -да- или -нет-')
        if i == ('да'):
            try:
                new_record = MyTable(f'{n1}')
                session.add(new_record)
                new_record = MyTable(f'{n2}')
                session.add(new_record)
                new_record = MyTable(f'{n3}')
                session.add(new_record)
                session.commit()
                print('Новости успешно занесенны в базу данных')
            except:
                print('--сбой при заносе в базу данных--')
                
        if i == ('нет'):
            continue

def par():
    parse(site('https://www.ukr.net'))
