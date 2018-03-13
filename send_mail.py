'''отправляет новости из базы данных на емейл'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from news import MyTable

email = "sergey3345@ukr.net"

def send_mail():
    email = input('Введи свой емейл: ')
    try:
        #подключение к базе данных
        engine = create_engine('postgresql://postgres:root@localhost/test_db')
        Session = sessionmaker(bind=engine)
        session = Session()
    except:
        print('Сбой при подключении к базе данных')
    
    try:        
        fromaddr = "qwerqwerqwertyzxc@gmail.com"#создал новый емейл чисто для отправки писем через питон
        mypass = "102938475611"
        toaddr = email
        records = session.query(MyTable).order_by('news')
        news = str(([record for record in records]))
        news = news.replace('>]', '').replace('>', '')
        news = news.replace('[<MyTable', '').replace('<MyTable', '')
 
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Сводка главных новостей"

        body = (news)#содержимое сообщения
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('Письмо с новостями успешно отправленно')
    except:
        print('--error--збой программы--error--')
        
