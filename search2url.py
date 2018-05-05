import urllib.parse

import bs4
import requests
import re
import shlex


def name2url(str_list):
    film_name_list = []
    for str_name in str_list:
        to_search = urllib.parse.quote(str_name, safe='')

        search_url = 'https://www.rottentomatoes.com/search/?search=' + to_search

        search_html = requests.get(search_url).content
        search_soup = bs4.BeautifulSoup(search_html, 'html.parser')

        div_cfpitem =search_soup.find('div',{"id": "main_container"}).find_all('script')[0].text
        # print(div_cfpitem.__class__)
        result_str = re.search(r'(/m/.*)', div_cfpitem).group(0).split(',')[0].strip('\"').strip("/m/")

        # div_cfpitem = search_soup.find('div', {"id": "main_container"}).find_all('script')[0].text
        # print(div_cfpitem.__class__)
        #
        # print(div_cfpitem)
        # result_str = re.findall(r'("year":2018,"url":"/m/.*)', div_cfpitem)
        # print(len(result_str))
        # print(result_str)
        # break


    #     href = div_cfpitem.a['href'].strip('/m/')
    #     print("href :",href)
        film_name_list.append(result_str)
    #     print('------------------------')
    return film_name_list

# ans = name2url(['Isle of Dogs',"Avengers: Infinity War",'Tully','RGB','Deadpool','Deadpool 2','Solo: A Star Wars Story'])
# print(ans)







