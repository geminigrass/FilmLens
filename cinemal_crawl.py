import bs4
import requests
import numpy as np
import csv


'''
This file defined several functions that are used for scraping movie name, show time, genre from Manor Cinema

'''

__author__= "Can Liu"

# do not modify, provided by professor Brain
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
    """Return the names, show time and genre of all movies showing at Manor Cinema revently.

    Arguments:
        soup {BeautifulSoup} -- BeautifulSoup object loaded with the html page text

    Returns:
        movies_names_clean,movies_showtime_clean,movies_genre_clean
         -- the the names, show time and genre of movies in a clean format
    """
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
    """Return the genre of a movie on the description page of a movie.

        Arguments:
            url {string} -- url to the description page

        Returns:
            genre of that movie
        """

    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    genres = soup.find("div",{'id':'main'}).h4.get_text()
    if "/" in genres:
        genres = genres.split('/')[-1]
    return genres.strip()


def save_cinema_raw(soup):
    """Save the raw file needed for Data File submission

        Arguments:
            soup {BeautifulSoup} -- BeautifulSoup object loaded with the html page text
        """

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
    """Save the clean file needed for Data File submission

    Arguments:
            soup {BeautifulSoup} -- BeautifulSoup object loaded with the html page text
    """

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

    # This line is used for data file handin
    save_cinema_raw(soup)

    movies_names_clean,movies_showtime_clean,movies_genre_clean = crawl_movies_and_showtime(soup)
    # This line is used for data file handin
    save_cinema_clean(movies_names_clean, movies_showtime_clean,movies_genre_clean)

if __name__ == "__main__":
    main()
