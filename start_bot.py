# -*- coding: utf-8 -*-
import telebot
import time
import telebot
from bs4 import BeautifulSoup
import requests
import numpy as np
import sqlite3
import os
timing = time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36',
}

sp_comment_main = []
##ЯНДЕКС КАРТЫ
try:
    with open("file2.txt", 'r', encoding="utf-8") as f:
        content = f.read()
except:
    with open("file2.txt", 'w', encoding="utf-8") as f:
        f.write('1')
while True:
    try:

        print(time.time() - timing)
        if time.time() - timing > 2400:
            response = requests.get(url='https://yandex.ru/maps/org/visage_concept/1097194736/reviews/?ll=47.496211%2C42.982898&z=16', headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            name = data.body.select('.business-review-view__author')
            date = data.body.select('.business-review-view__date')
            comment = data.body.select('.business-review-view__body-text')
            stars1 = data.body.select('.inline-image.business-rating-badge-view__star._size_m')

            numb = 0
            numb1 = 0
            sp_stars = []
            sp_stars1 = []

            sp = []
            sp_date = []
            sp_comment = []
            sp_main = [
                [],
                [],
                [],
                [],
                [],
            ]
            for name_otz in name:
                for i in name_otz:
                    sp.append(str(i))
            for date_otz in date:
                for i in date_otz:
                    sp_date.append(str(i))

            for comment_otz in comment:
                for i in comment_otz:
                    sp_comment.append(str(i))

            for i in sp:
                try:
                    indx3 = i.index('itemprop="name">') + 16
                    indx4 = i.index("</span>")
                    name1 = i[indx3:indx4]
                    name1 = 'Яндекс карты:' + '\n' + str(name1)
                    sp_main[0].append(name1)
                except ValueError:
                    pass
            for i in sp:
                try:
                    indx3 = i.index('href="') + 6
                    indx4 = i.index('" target="_blank"')
                    ssl = i[indx3:indx4]
                    ssl = 'Ссылка: ' + str(ssl)
                    sp_main[4].append(ssl)
                except ValueError:
                    pass

            for i in sp_date:
                try:
                    indx3 = i.index('span>') + 5
                    indx4 = i.index("</span>")
                    date1 = i[indx3:indx4]
                    sp_main[1].append(date1 + '.')
                except ValueError:
                    pass
            for i in sp_comment:
                sp_main[2].append(i)

            for i in stars1:
                sp_stars.append(str(i))


            for i in sp_stars:
                numb = 0
                if '_empty' in str(i):
                    numb += 1
                sp_stars1.append(numb)


            sp_stars3 = np.add.reduceat(sp_stars1, np.arange(0, len(sp_stars1), 5))
            for i in sp_stars3[1:]:
                mark = 'Оценка: ' + str(5 - int(i)) + '.'
                sp_main[3].append(mark)

            TOKEN = '#bot token'
            bot = telebot.TeleBot(TOKEN)
            num = 0
            num_main = 0
            with open("file2.txt", 'r', encoding="utf-8") as f:
                content = f.read()
                if str(sp_main[2][0]) == str(content):
                    print('есть')

                else:
                    info = str(sp_main[0][0] + '\n' + sp_main[1][0] + '\n' + sp_main[2][0] + '\n' +
                               sp_main[3][0] + sp_main[4][0])
                    bot.send_message(#id of bot, info)
                    sp_comment_main.append(sp_main[2][0])
                    comment = str(sp_main[2][0])
                    time.sleep(int(3))
                    with open("file2.txt", "w", encoding="utf-8") as f:
                        os.system(r'nul>file2.txt')
                        f.write(comment)
    except IndexError:
        pass