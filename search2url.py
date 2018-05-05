import urllib.parse

import bs4
import requests
import re


def name2url(str_list):
    film_name_list = []
    for str_name in str_list:
        to_search = urllib.parse.quote(str_name, safe='')

        search_url = 'https://www.rottentomatoes.com/search/?search=' + to_search

        search_html = requests.get(search_url).content
        search_soup = bs4.BeautifulSoup(search_html, 'html.parser')

        div_cfpitem =search_soup.find('div',{"id": "main_container"}).find_all('script')[0].text
        result_str = re.search(r'(/m/.*)', div_cfpitem).group(0).split(',')[0].strip('\"').strip("/m/")
        film_name_list.append(result_str)
    return film_name_list








