import bs4
import requests
import numpy as np
import csv

def test():
    print('--------')

# do not modify
def get_text_from_elements(elements):
    """Uses list comprehension to parse out the cleaned text strings from a list of
    elements returned from a BeautifulSoup selection.

    Arguments:
        elements {list} -- list of elements returned from a BeautifulSoup selection

    Returns:
        list -- list of cleaned text contained within the element list
    """

    return [e.text.strip() for e in elements]



def crawl_movies_and_showtime(soup):
    base_url = "http://www.manorpgh.com"
    # convert to list in order to preserve the order of movies
    divs_ns_item = list(soup.find_all("div", class_='ns-item'))

    movies_names_clean = []
    movies_showtime_clean = []
    movies_genre_clean = []

    for tag in divs_ns_item:

        name = tag.h2.get_text()
        movies_names_clean.append(name)

        id = tag.get('id').split('_')[1]
        show_time = soup.find(id='time_' + id).div
        ns_date = get_text_from_elements(show_time.select('.ns-date'))[0]
        ns_days = get_text_from_elements(show_time.select('.ns-days'))[0]
        ns_time = get_text_from_elements(show_time.select('.ns-time'))[0]
        time_dict = {'date': ns_date, 'days': ns_days, 'time': ns_time}
        movies_showtime_clean.append(time_dict)

        href = tag.a['href']
        new_link =base_url + href
        genre = get_genre(new_link)
        movies_genre_clean.append(genre)

    return movies_names_clean,movies_showtime_clean,movies_genre_clean

def get_genre(url):
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    genres = soup.find("div",{'id':'main'}).h4.get_text()
    if "/" in genres:
        genres = genres.split('/')[-1]
    return genres.strip()


def save_cinema_raw(soup):
    # convert to list in order to preserve the order of movies
    divs_ns_item = list(soup.find_all("div", class_='ns-item'))
    divs_ns_showtime = list(soup.find_all("div", class_='ns-showtime'))

    contents = []
    contents.append(['names','showtimes'])
    num = len(divs_ns_item)
    for i in range(num):
        l = []
        l.append(str(divs_ns_item[i]))
        l.append(str(divs_ns_showtime[i]))
        contents.append(l)

    with open("./DataFile/cinema_raw.csv", 'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(contents)

def save_cinema_clean(names, showtimes, genre):
    contents = []
    contents.append(['names', 'showtimes','genre'])
    num = len(names)
    for i in range(num):
        l = []
        l.append(names[i])
        l.append(showtimes[i])
        l.append(genre[i])
        contents.append(l)
    with open("./DataFile/cinema_clean.csv", 'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(contents)


def main():
    url = "http://www.manorpgh.com/"
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # save_cinema_raw(soup)

    movies_names_clean,movies_showtime_clean,movies_genre_clean = crawl_movies_and_showtime(soup)
    length = len(movies_names_clean)
    for i in range(length):
        print(i, movies_names_clean[i])
    # save_cinema_clean(movies_names_clean, movies_showtime_clean,movies_genre_clean)

if __name__ == "__main__":
    main()
