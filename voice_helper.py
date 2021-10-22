import time
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import webbrowser
import os
import psutil
import requests


adress = ''



now = datetime.datetime.now()

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    return talk


def command():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language = 'ru-RU').lower()
        print(f'[log] Уловила: {task}')
    except:
        print('Я вас не раслышала, повторите')
        task = command()

    return task



def working(task):
    if 'пятница' in task:
        talk('Слушаю')
        

    elif 'расскажи что мы приготовили' in task:
        talk("""
Я голосовой помощник, меня зовут пятница, я умею выполнять огромное количество функций

от того что бы открыть какое нибудь приложение до того что бы выполнить поиск в Ютуб и Гугл

я и мой создатель расчитываем на долгосрочную перспективу и в дальнейшем будем усовершенствовать меня

благодарим вас за то что выслушали

что бы больше узнать о моих способностях спросите меня что ты можешь





            """)

    elif 'что ты можешь' in task:
        talk('я вывела все комманды на экран')
        print("""

1.перезагрузи компьютер
2.который час
3.сколько время
4.открой гугл 
5.погода на сегодня
6.расскажи что-нибудь интересное
7.открой youtube
8.открой vk
9.открой инстаграм
10.открой pubg
11.открой кс
12.открой steam
13.открой discord
14.переведи слово
15.загугли, найди в гугле
16.найди на YouTube


            """)

    elif 'привет' in task:
        talk('Здраствуйте')

    elif 'проанализируй компьютер' in task:
        talk('Анализирую...')
        use = psutil.cpu_percent(interval=None, percpu=False)
        talk("процессор загружен на " + str(use) + " процента" )
        print("[log] процессор загружен на " + str(use) + " процента" )

    elif 'ладно на сегодня всё' == task:
        talk('Останавливаю')
        sys.exit()

    elif 'стоп' == task:
        talk('Останавливаю')
        sys.exit()

    elif 'спасибо' == task:
        talk("Пожалуйста")

    elif 'перезагрузи компьютер' == task:
        talk("перезагружаю")
        os.system("shutdown /r /t 1")

    elif 'я не с тобой' == task:
        talk("извините босс")

    elif 'переведи ' in task:
        word = task
        word = word.replace('переведи','').strip()
        word = word.replace('перевести','').strip()
        word = word.replace('переводить','').strip()
        word = word.replace('перевод','').strip()
        word = word.replace('слово','').strip()
        word = word.replace('слова','').strip()
        webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=en&text={}'.format(word))


    elif 'найди в гугле' in task:
        word = task
        word = word.replace('найди в гугле','').strip()
        word = word.replace('загугли','').strip()
        webbrowser.open('https://www.google.ru/search?q={}'.format(word))

    elif 'загугли' in task:
        word = task
        word = word.replace('найди гугле','').strip()
        word = word.replace('загугли','').strip()
        webbrowser.open('https://www.google.ru/search?q={}'.format(word))

    elif 'найди на youtube' in task:
        word = task
        word = word.replace('найди на youtube','').strip()
        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(word))

    elif 'который час' in task:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif 'сколько время' in task:
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif 'открой яндекс' in task:
        talk("открываю")
        webbrowser.open('https://yandex.ru/')

    elif 'открой почту' in task:
        talk("открываю")
        webbrowser.open('https://mail.ru/')

    elif 'открой гугл' in task:
        talk("открываю")
        webbrowser.open('https://google.ru')

    elif 'погода на сегодня' in task:
        talk("открываю")
        url = 'https://yandex.ru/pogoda'
        webbrowser.open(url)

    elif 'когда ты была создана' in task:
        talk("я была создана 5 июня 2020 года")

    elif 'слушай пятница' in task:
        talk("слушаю босс")

    elif 'как дела' in task:
        talk("отлично")

    elif 'поболтаем' in task:
        talk("конечно босс")

    elif 'что делаешь' in task:
        talk("помогаю вам босс")

    elif 'как тебя зовут' in task:
        talk("меня зовут пятница")

    elif 'открой youtube' in task:
        talk("открываю")
        webbrowser.open('https://www.youtube.com')

    elif 'открой vk' in task:
        talk("открываю")
        webbrowser.open('https://vk.com/')

    elif 'открой инстаграм' in task:
        talk("открываю")
        webbrowser.open('https://www.instagram.com/')

    elif 'открой pubg' in task:
        talk("открываю")
        file_path = r"C:\SteamLibrary\steamapps\common\PUBG\TslGame\Binaries\Win64\TslGame.exe"
        os.system("start "+file_path)

    elif 'открой cs go' in task:
        talk("открываю")
        file_path = r"D:\steam\steamapps\common\Counter-Strike Global Offensive\csgo.exe"
        os.system("start "+file_path)

    elif 'открой саблайм' in task:
        file_path = r"D:\Sublime Text 3\sublime_text.exe"
        os.system("start "+file_path)

    elif 'открой steam' in task:
        talk("открываю")
        file_path = r'D:\steam\steam.exe' 
        os.system("start "+file_path)

    elif 'открой discord' in task:
        talk("открываю")
        file_path = r'D:\Yandex\ds\Discord' 
        os.system("start "+file_path)





if now.hour >= 6 and now.hour < 12:
    talk("Доброе утро босс!")
elif now.hour >= 12 and now.hour < 18:
    talk("Добрый день босс!")
elif now.hour >= 18 and now.hour < 22:
    talk("Добрый вечер босс!")
else:
    talk("Доброй ночи босс!")
    

while True:
    working(command())
