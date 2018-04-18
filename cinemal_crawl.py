import bs4
import requests


def main():
    url = "http://www.manorpgh.com/"
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    divs_ns_item = soup.find_all("div", class_='ns-item')
    num_movies = len(divs_ns_item)
    movies_names = []
    movies_showtime = []
    for tag in divs_ns_item:
        name = tag.h2.get_text()
        movies_names.append(name)
    print(movies_names)



if __name__ == "__main__":
    main()
