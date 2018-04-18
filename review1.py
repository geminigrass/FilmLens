import requests, pandas, numpy, matplotlib.pyplot
from bs4 import BeautifulSoup
import math
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


url_rotten = "https://www.rottentomatoes.com/m/"



# get text from BeautifulSoup selected elements list
def get_text_from_elements(elements):
    return [e.text.strip() for e in elements]
# get reviews from one pge
def get_reviews_from_one_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    reviews_html = soup.select('.the_review')
    return reviews_html
# get all reviews of first n pages
def get_reviews_from_several_pages(url_base, n):
    i = 0
    url = url_base + "1"
    reviews_html = get_reviews_from_one_page(url)
    while i < n:
        url = url_base + str(i)
        reviews_html = reviews_html + get_reviews_from_one_page(url)
        i = i + 1
    return reviews_html



# get total number of page of reviews
def get_page_nums(film_name):
    url_first_page = url_rotten + film_name + "/reviews/"
    page = requests.get(url_first_page)
    soup = BeautifulSoup(page.content, "html.parser")
    review_nums_html = soup.select('.pageInfo')
    print(review_nums_html)
    print(type(review_nums_html))
    review_nums_str = get_text_from_elements(review_nums_html)[0]
    print(review_nums_str)
    print(type(review_nums_str))
    page_nums = re.findall(r"\d+",review_nums_str)
    page_nums = int(page_nums[1])
    print(page_nums)
    return page_nums

# convert from list to txt file
def get_txt(reviews_list, txt_file_name):
    # reviews_text = get_text_from_elements(reviews_html)
    fileObject = open(txt_file_name, 'w')
    for word in reviews_list:
        fileObject.write(word)
        fileObject.write('\n')
    fileObject.close()




film_name_list_1 = ["the_death_of_stalin", "isle_of_dogs_2018", "the_leisure_seeker", "ready_player_one"]
film_name_list_2 = ["final_portrait", "you_were_never_really_here", "avengers_infinity_war", "Deadpool 2"]
# film_name_list = film_name_list_1 + film_name_list_2
film_name_list = ["the_death_of_stalin", "isle_of_dogs_2018"]
i = 0
# list_reviews_html_str = list()
for film_name in film_name_list:
    txt_file = "film" + str(i) + ".txt"
    page_nums = get_page_nums(film_name)
    url_base = url_rotten + film_name + "/reviews/?page="
    reviews_html = get_reviews_from_several_pages(url_base, page_nums)
    # reviews_html_str = ''.join(reviews_html)
    # list_reviews_html_str.append(reviews_html_str)
    reviews_text = get_text_from_elements(reviews_html)
    get_txt(reviews_text, txt_file)
    i = i + 1
# print(list_reviews_html_str[0], list_reviews_html_str[1])








# text_from_file_with_apath = open('/film1.txt').read()
#
# wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
# wl_space_split = " ".join(wordlist_after_jieba)
#
# my_wordcloud = WordCloud().generate(wl_space_split)
#
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
