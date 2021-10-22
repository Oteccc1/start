# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36',
}
path = 'pars.csv'
sp_prc = []
with open(path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Цена', 'Товар', 'Артикул'])
    for i_page in range(2200):
        try:
            link = 'https://www.tsum.ru/catalog/' + f'?page={i_page}'
            print('Страница ' + str(i_page))
            response = requests.get(link, headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            html, url1 = data.body.select('.product__image-first'), data.body.select('.product__image-wrapper')
            price = data.body.select('.price_type_new')
            sp = []
            num = 0
            #print(price)
            for i in price:
                sp_prc.append(str(i))
            for prcc in sp_prc:
                indx3 = prcc.index('-sc90="">') + 9
                indx4 = prcc.index("</span>")
                price1 = prcc[indx3:indx4]
            for y in html:
                url = y['title']
                for i in url1:
                    sp.append(i['href'])
                if len(url) < 63:
                    continue
                else:
                    name = y['title'][:(url.index('цене')) - 4]
                    art = y['title'][(url.index('арт.') + 5):(url.index(' |'))]
                    price = y['title'][(url.index('цене')) + 4:(url.index('арт.') + 5) - 8]
                writer.writerow([price, name, art])
        except ValueError:
            pass
    slow = {}
    for i_page in range(128):
        try:
            link = f'https://bianco-boutique.ru/catalog/?view=blocks&page_count=20&sort=property_sort&by=asc&PAGEN_1={i_page}'
            print('Страница ' + str(i_page))
            response = requests.get(link, headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            brand = data.body.select('.catalog-item-name')
            price = data.body.select('.b-price')
            artic = data.body.select('.short-description')
            sp = []
            sp1 = []
            num = 2
            for y in brand:
                num += 1
                url = y["href"]
                name = y["title"]
                for i in price:
                    sp.append(str(i))
                for i in artic:
                    sp1.append(str(i))
                pr = sp[num - 1]
                ar = sp1[num - 3]
                indx = (pr.index('ce">') + 4)
                indx_2 = (pr.index('</span>'))
                indx_3 = (ar.index('product-article">') + 17)
                indx_4 = (ar.index('</span>'))
                price1 = pr[indx:indx_2]
                article = ar[indx_3:indx_4]
                writer.writerow([price1, name, article])
        except ValueError:
            pass

    name1 = ''
    for i_page in range(1, 980):
        try:
            link = f'https://www.rendez-vous.ru/catalog/page/{i_page}'
            print(i_page)
            response = requests.get(link, headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            name = data.body.select('.item-image-thumbnail')
            art = data.body.select('.item')
            sp = []
            sp1 = []
            sp2 = []
            num = 0
            for y in name:
                name = y['alt']
                sp.append(name)
            for b in art:
                sp1.append(str(b))
            for artcl in sp1:
                indx3 = artcl.index('name') + 8
                indx4 = artcl.index("id") - 4
                indx5 = artcl.index("'price': '") + 10
                indx6 = artcl.index(", 'brand':") - 6
                art = artcl[indx3:indx4]
                prc = artcl[indx5:indx6]
                name = sp[num]
                num += 1
                if name == name1:
                    continue
                else:
                    writer.writerow([prc, name, art])
        except ValueError:
            pass


    for i_page in range(1, 30):
        link = 'https://monacomoda.com/catalog/man/' + f'?PAGEN_1={i_page}'
        print('Страница ' + str(i_page))
        response = requests.get(link, headers=headers, verify=True)
        data = BeautifulSoup(response.text, 'html.parser')
        name = data.body.select('.lazy')
        price = data.body.select('.price')
        url = data.body.select('.name')
        sp = []
        sp1 = []
        sp_art = []
        sp_art1 = []
        num = 1
        num2 = 0
        for y in name:
            num += 1
            name = y['alt']
            for i in url:
                sl = i['href']
                sp1.append(sl)
                for u in price:
                    sp.append(str(u))
            pprc = sp[num - 2]
            link = 'https://monacomoda.com' + sp1[num - 2]
            response = requests.get(link, headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            art = data.body.select('.ask-question')
            for articl in art:
                sp_art.append(str(articl))
            for article in sp_art:
                indx_4 = article.index('<strong>') + 8
                indx_5 = article.index('</strong> </p>')
            sp_art1.append(article[indx_4:indx_5])
            art1 = sp_art1[num2]
            pricee = pprc[(pprc.index('ce">') + 67):(pprc.index('</a>') - 15)].lstrip().rstrip()
            writer.writerow([art1, name, pricee])
            num2 += 1

    for i_page in range(1, 119):
        link = 'https://monacomoda.com/catalog/woman/' + f'?PAGEN_1={i_page}'
        print('Страница ' + str(i_page))
        response = requests.get(link, headers=headers, verify=True)
        data = BeautifulSoup(response.text, 'html.parser')
        name = data.body.select('.lazy')
        price = data.body.select('.price')
        url = data.body.select('.name')
        sp = []
        sp1 = []
        sp_art = []
        sp_art1 = []
        num = 1
        num2 = 0
        for y in name:
            num += 1
            name = y['alt']
            for i in url:
                sl = i['href']
                sp1.append(sl)
                for u in price:
                    sp.append(str(u))
            pprc = sp[num - 2]
            link = 'https://monacomoda.com' + sp1[num - 2]
            response = requests.get(link, headers=headers, verify=True)
            data = BeautifulSoup(response.text, 'html.parser')
            art = data.body.select('.ask-question')
            for articl in art:
                sp_art.append(str(articl))
            for article in sp_art:
                indx_4 = article.index('<strong>') + 8
                indx_5 = article.index('</strong> </p>')
            sp_art1.append(article[indx_4:indx_5])
            art1 = sp_art1[num2]
            pricee = pprc[(pprc.index('ce">') + 67):(pprc.index('</a>') - 15)].lstrip().rstrip()
            writer.writerow([art1, name, pricee])
            num2 += 1