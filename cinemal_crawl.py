import bs4
import requests

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
    # convert to list in order to preserve the order of movies
    divs_ns_item = list(soup.find_all("div", class_='ns-item'))

    movies_names_clean = []
    movies_showtime_clean = []

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
    return movies_names_clean,movies_showtime_clean


def main():
    url = "http://www.manorpgh.com/"
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')

    movies_names_clean,movies_showtime_clean = crawl_movies_and_showtime(soup)

    print(movies_names_clean)
    print(movies_showtime_clean)





if __name__ == "__main__":
    main()
