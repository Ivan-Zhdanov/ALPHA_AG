from bs4 import BeautifulSoup
import requests
import re
import numpy
from Sounds_download_to_mp3 import sound_to_mp3


def parse_sounds(URL):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                   'Accept': '*/*'}

    # URL = 'https://zvukipro.com/ptici/3044-zvuki-sosnovogo-lesnogo-pevuna.html'
    # URL = 'https://zvukipro.com/atmosphera/3332-atmosfernyj-zvuk-inoplanetnogo-vtorzhenija.html'
    # URL = 'https://zvukipro.com/program/3066-zvuki-operacionnoj-sistemy-linux-mint.html'
    responce = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(responce.text, "html.parser")


    # Удаление br
    content = soup.find('div', class_='fstory')
    for li_un in content.findAll('div', class_='dleaudioplayer'):
        li_un.unwrap()
    try:
        content.find('div', class_='borya66').decompose()
    except:
        pass
    # content.find('div', class_='zagolovy33').decompose()
    content.find('div', class_='borya669').decompose()
    content.find('div', class_='sodad').decompose()
    content.find('div', class_='scont clrfix').decompose()
    content.find('div', class_='error67').decompose()
    # content.find('div', class_='zagolov22').decompose()
    content.find('div', id='vk_comments').decompose()
    content.find('div', class_='soderjanie22').decompose()
    content.find('div', class_='ya-share2').decompose()
    content.find('div', class_='yandexpoh').decompose()
    try:
        content.find('div', class_='publicite').decompose()
    except:
        pass

    for att in content.find('span', class_='attachment'):
        att.decompose()
    content.find('div', class_='pad').decompose()
    content.find('ins', class_='adsbygoogle').decompose()
    try:
        content.find('div', class_='zagolov22').decompose()
    except:
        pass
    content.find('div', class_='katavasa').decompose()
    content.find('h1').decompose()
    content.find('div', class_='soderjanie222').decompose()
    for sod in content.findAll('div', class_='soderjanie'):
        sod.decompose()
    content.find('div', class_='zagolovy').decompose()


    for span in content.findAll('span'):
        span.decompose()
    content.find('br').decompose()
    for ul in content.findAll('ul'):
        ul.unwrap()

    content.find('script').decompose()
    for sc in content.findAll('script'):
        sc.decompose()

    # Вывод контента после удаления вяких тегов
    # print(content)
    #
    content2 = re.sub('<!--(.+?)-->', '', str(content))
    content3 = content2.replace('<br/>', '')
    # print(content3)



    # Удаление блока на скачивание
    soup4 = BeautifulSoup(content3,'html.parser')
    dws = soup4.find_all('span', class_='attachment')
    for dw in dws:
        dw.decompose()
    # print(soup4)
    names = soup4.get_text()
    # print(names)

    name = names.split("\n")
    name2 = list(filter(None, name))
    # print(name2)

    # Создание списка с названиями
    result = [string.replace('\xa0', ' ') for string in name2]
    print(result)

    lis = soup4.findAll('li')
    # for li in lis:
        # print('11111111111',li.find_previous_sibling())



    soup2 = BeautifulSoup(str(content3), "html.parser")
    # for name in soup2.find_all('li'):
    #     print('ИМЯ ', name.find_previous().text)

    sounds = []

    for li in soup2.find_all('li'):
        sounds.append(li['data-url'])
        # print('Звуковые файлы', li)

    print(sounds)

    # value = []
    # # Создание суммарного словаря после страницы
    # i = 0
    # for el in result:
    #     value.append(el)
    #     value.append(sounds[i])
    #     i = i + 1


    # Список четных и нечетных значений
    # print(value)

    return [result, sounds]

if __name__ == '__main__':
    # parse_sounds()
    y = []
    with open('urls_zvuki.txt', 'r') as file:
        u = file.readlines()
        for el in u:
            y.append(el.replace("\n", ''))
    i = 1865
    for url in y[1865:]:
        i = i + 1
        print(i)
        print(url)
        parse_result = parse_sounds(url)
        # print(parse_result)
        mp3_list = parse_result[1]
        # print(mp3_list)

        # скачивание по ссылке файла в mp3
        for url_mp3 in mp3_list:
            sound_to_mp3(url_mp3)
