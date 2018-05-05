import pandas as pd
import sys
# print(sys.path)
# sys.path.append('/Users/des/Desktop/95880python')
sys.path.append('../')

from FilmLens.cinemal_crawl import *
from FilmLens.review_word_cloud import *
from FilmLens.search2url import *
from FilmLens.review_scrap import *


def main():

    url = "http://www.manorpgh.com/"
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    movies_names_clean, movies_showtime_clean, movies_genre_clean = crawl_movies_and_showtime(soup)
    film_name_list = name2url(movies_names_clean)

    using = True
    review_scraped = False
    while(using):
        print('----------Main Menu--------------------')
        print("Welcone to FilmLens!")
        print('^_^')
        print('Enter E to exit from FilmLens.')
        print('')
        print('These movies are showing at Manor Cinema recently:')

        length = len(movies_names_clean)
        for i in range(length):
            print(i, movies_names_clean[i])

        print('')
        if not review_scraped:
            print('Please wait. Programe is scraping reviews from these movies.....')
            scrap_from_film_name_list(film_name_list)
            review_scraped = True

        choise = input('Please enter a number to select a movie:')
        if choise == 'E':
            using=False
            continue
        else:
            choise = int(choise)

            goon = True
            while(goon):

                print('--------------Showtime----------------')
                print("Showtime of the movie: ", movies_names_clean[choise], " is")
                print("days: ", movies_showtime_clean[choise]['days'])
                print("date: ", movies_showtime_clean[choise]['date'])
                print("time: ", movies_showtime_clean[choise]['time'])
                print('')
                see_next = input('continue?y/n :')

                if see_next == 'n':
                    print(see_next)
                    print(see_next == 'n')
                    print(see_next == 'y')
                    goon = False
                    continue
                else:
                    print('-------------Review & Recommendation-----------------')
                    print("Genre of the movie: ", movies_names_clean[choise], " is")
                    print(movies_genre_clean[choise])
                    print(' ')
                    print("You may also like movies with similar genre:")

                    df = pd.read_csv("./DataFile/classic_movies.csv")
                    strr = list(df.loc[df['genre'] == movies_genre_clean[choise]]['recommendations'])[0]

                    lines = strr.strip('[]').split(',')
                    for item in lines:
                        print(item.strip())
                    txt_file_path = "./DataFile/reviews_film_" + film_name_list[choise] + "_clean" + ".txt"
                    show_word_cloud(txt_file_path)
                    back = input('Press y to go back:')
                    goon = False
                    continue



if __name__ == "__main__":
    main()