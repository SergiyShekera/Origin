from pogoda import kyiv, kharkiv, odessa, lvov
from pogoda import berlin, london, barselona, madrid
from pogoda import newyork
from news import par
from send_mail import send_mail
from parser_BITCOIN import parser_BITCOIN

print('Программа запущена')

def start():    
    print('Нажми ENTER для перехода в меню')  
    print('Введи -выкл- для выхода из программы')
    a = input()
    if a ==('выкл'):
        pass
    else:
        if __name__ == '__main__':
            choise()

def choise():
    print('Выбирай, новости или погода? ')
    print('Также можешь узнать курс биткоина, введи -биткоин- ')
    print('Для выхода из прогррамы введи -выкл- ')
    a = input('')
    if a == ('новости'):
        if __name__ == '__main__':
            news()
    if a == ('погода'):
        if __name__ == '__main__':
            pogoda()
    if a == ('биткоин'):
        if __name__ == '__main__':
            bitcoin()            
    if a ==('выкл'):
        pass
    else:
        if __name__ == '__main__':
            start()
        
def news():
    a = input('для показа новостей введи -новости-'
              '\nдля отправки новостей имеющихся в базе данных на емейл введи -емейл- ')
    if a == ('новости'):
        par()
    if a ==('емейл'):
        send_mail()
    if __name__ == '__main__':
        choise()

def pogoda():
    i = (
        'В каком из городов хочешь узнать погоду?' 
         '\nвот список доступных городов: киев, львов, харьков, одесса, берлин, лондон, мадрид, барселона, нью-йорк'
        '\nвведи название города: '
        )  
    a = input(i)
    if a == ('киев'):
        kyiv()
    if a == ('харьков'):
        kharkiv()
    if a == ('одесса'):
        odessa()
    if a == ('львов'):
        lvov()
    if a == ('берлин'):
        berlin()
    if a == ('лондон'):
        london()
    if a == ('барселона'):
        barselona()
    if a == ('мадрид'):
        madrid()
    if a == ('нью-йорк'):
        newyork()
    if __name__ == '__main__':
        choise()

def bitcoin():
    parser_BITCOIN()
    
    if __name__ == '__main__':
        choise()


if __name__ == '__main__':
    start()
