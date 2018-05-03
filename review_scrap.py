import requests
import pandas, numpy, matplotlib.pyplot
from bs4 import BeautifulSoup
import math
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
# import pynlpir
import codecs
import string
import csv


url_rotten = "https://www.rottentomatoes.com/m/"
film_name_list_1 = ["avengers_infinity_war", "avengers_infinity_war", "the_death_of_stalin", "final_portrait", "isle_of_dogs_2018"]
film_name_list_2 = ["you_were_never_really_here", "tully_2018", "rbg", "deadpool_2"]
film_name_list = film_name_list_1 + film_name_list_2


# get text from BeautifulSoup selected elements list
def get_text_from_elements(elements):
    return [e.text.strip() for e in elements]
# get reviews from one pge
def get_reviews_from_one_page(url, review_type):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    if review_type == "audience":
        reviews_html = soup.select('.user_review')
    else:
        reviews_html = soup.select('.the_review')
    return reviews_html
# get all reviews of first n pages
def get_reviews_from_several_pages(url_base, page_nums, review_type):
    i = 0
    if review_type == "audience":
        url = url_base + "1" + "&type=user"
    else:
        url = url_base + "1"
    reviews_html = get_reviews_from_one_page(url, review_type)
    while i < page_nums:
        if review_type == "audience":
            url = url_base + str(i) + "&type=user"
        else:
            url = url_base + str(i)
        reviews_html = reviews_html + get_reviews_from_one_page(url, review_type)
        i = i + 1
    return reviews_html



# get total number of page of reviews
def get_page_nums(film_name):
    url_first_page = url_rotten + film_name + "/reviews/"
    page = requests.get(url_first_page)
    soup = BeautifulSoup(page.content, "html.parser")
    review_nums_html = soup.select('.pageInfo')
    # print(type(review_nums_html))
    # print(review_nums_html)
    # print(len(review_nums_html))
    if len(review_nums_html) == 0:
        url_first_page = url_rotten + film_name + "/reviews/?type=user"
        page = requests.get(url_first_page)
        soup = BeautifulSoup(page.content, "html.parser")
        review_nums_html = soup.select('.pageInfo')
        # print(review_nums_html)
        review_type = "audience"
    else:
        review_type = "critic"
    review_nums_str = get_text_from_elements(review_nums_html)[0]
    print(review_nums_str)
    print(type(review_nums_str))
    page_nums = re.findall(r"\d+",review_nums_str)
    page_nums = int(page_nums[1])
    print(page_nums)
    return page_nums, review_type

# convert from list to txt file
def get_txt(reviews_list, txt_file_name):
    # reviews_text = get_text_from_elements(reviews_html)
    fileObject = open(txt_file_name, 'w')
    for word in reviews_list:
        fileObject.write(word)
        fileObject.write('\n')
    fileObject.close()

def list_to_lower(list):
    return [x.lower() for x in list]
def get_list_of_str(list):
    return [str(x) for x in list]

def save_reviews_raw(reviews_html, txt_file):
    # convert to list in order to preserve the order of movies
    # divs_ns_item = list(soup.find_all("div", class_='ns-item'))
    # divs_ns_showtime = list(soup.find_all("div", class_='ns-showtime'))

    contents = []
    # contents.append(['names','showtimes'])
    num = len(reviews_html)
    for i in range(num):
        l = []
        l.append(str(reviews_html))
        # l.append(str(divs_ns_showtime[i]))
        contents.append(l)
    with open(txt_file, 'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(contents)


# film_name_list = ["the_death_of_stalin"]
director_list = [""]
i = 0
# list_reviews_html_str = list()
for film_name in film_name_list:
    txt_file = "film" + str(i) + ".txt"
    page_nums, review_type = get_page_nums(film_name)
    url_base = url_rotten + film_name + "/reviews/?page="
    reviews_html = get_reviews_from_several_pages(url_base, page_nums, review_type)
    print("type of reviews_html: ",type(reviews_html))
    txt_file = "./DataFile/reviews_film" + str(i) + "_raw" + ".csv"
    save_reviews_raw(reviews_html, txt_file)
    # reviews_raw = get_list_of_str(reviews_html)
    # get_txt(reviews_raw, txt_file)

    reviews_text = get_text_from_elements(reviews_html)
    # print("type of reviews_text: ", type(reviews_text))
    # transfer reviews to lower
    reviews_text = list_to_lower(reviews_text)
    # get list of words from sentences in reviews list
    reviews_words = []
    for sentence in reviews_text:
        words = sentence.split()
        reviews_words = reviews_words + words
    # get  reviews of lower words
    # get_txt(reviews_words, txt_file)
    reviews_words = [''.join(c for c in s if c not in string.punctuation) for s in reviews_words]
    # delete stop words
    stopwords = []
    st = codecs.open('stopwords.txt', 'rb',encoding='utf-8')
    for line in st:
        line = line.strip()
        stopwords.append(line)
    film_words_to_delete = ['film', 'movie', 'theater', 'show', 'make', 'i', 'im','people', 'see','watch']
    film_name_words = film_name.split("_")
    words_to_delete = film_words_to_delete + stopwords + film_name_words
    for word in reviews_words:
        if word in words_to_delete:
            reviews_words.remove(word)
    for word in reviews_words:
        if word in film_words_to_delete:
            reviews_words.remove(word)
    txt_file = "./DataFile/reviews_film" + str(i) + "_clean" + ".txt"
    get_txt(reviews_words, txt_file)
    i = i + 1
