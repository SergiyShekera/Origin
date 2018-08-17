import imaplib
import email

from imaplib import IMAP4_SSL


def auth():
    
    USER = input('Your login: ')
    PASSWORD = input('Your password: ')

    HOST = "imap.gmail.com"
    PORT = 993

    connection = IMAP4_SSL(host=HOST, port=PORT)
    connection.login(user=USER, password=PASSWORD)
    connection.select('INBOX')
    
    return connection


def search(connection):
    
    connection.select('INBOX')
    typ, data = connection.search(None, "ALL")
    
    return data
    

def get_data(num, connection):
    
    res, msg = connection.fetch(num, '(RFC822)')
    r = msg[0][1].decode('utf-8')
    m = email.message_from_string(r)
    
    if m.is_multipart():
        
        for part in m.walk():
            
            if part.get_content_type() == "text/plain":
                
                body = part.get_payload(decode=True) 
                body = body.decode()
                
    else:
        
        body = b.get_payload(decode=True)

    fr = m['From']

    print('From - ' + fr)
    print(' ')
    print(body)
    

def message_data(connection):
        
    data = search(connection)
    
    for num in data[0].split()[:-6:-1]:
        
        print('------------------------------------')
        print('Message №' + num.decode("utf-8") )
        
        get_data(num, connection)
        
        print('------------------------------------')
        print(' ')
        


def get_messages_data():

    try:      
        connection = auth()
        message_data(connection)
        
    except:        
        print('Incorrect login or password')
    




