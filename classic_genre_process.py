import pandas as pd
import csv

'''
This file takes an file(classic_movies_raw.csv) downloaded from the website as an input.
Then gives genre of each movie by choosing the first genre.
'''

__author__= "Can Liu"

def save_clean(path):
    """Read from the raw file that store the classic movies and their genres.
    In the raw file, each movie has more than one genre,
    here we simply take the first genre.

    Arguments:
        path {string} -- path to the raw file.
    """
    df_movies = pd.read_csv(path)
    length = len(df_movies['genres'])

    for i in range(length):
        genres = df_movies['genres'][i]
        if "|" in genres:
            genre = genres.split("|")[0]
            df_movies['genres'][i] = genre
        else:
            df_movies['genres'][i] = genres

    df_clean = pd.DataFrame()
    df_clean['title'] = df_movies['title']
    df_clean['genres'] = df_movies['genres']
    df_clean.to_csv("./DataFile/classic_movies_clean.csv", encoding='utf-8', index=False)
    return "./DataFile/classic_movies_clean.csv"


def transpose(path):
    """Save the clean file needed for Data File submission.
    Change the row to be genres, and columns to be a list of movies.

    Arguments:
        path {string} -- path to the raw file.
    """
    df_clean = pd.read_csv(path)
    grouped_df = df_clean.groupby('genres')

    content = []
    content.append(['genre','recommendations'])
    for key, item in grouped_df:
        last_5_movies = list(grouped_df.get_group(key)['title'].iloc[-5:])
        l = []
        l.append(key)
        l.append(last_5_movies)
        content.append(l)

    with open("./DataFile/classic_movies.csv", 'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(content)


def main():
    raw_path = "./DataFile/classic_movies_raw.csv"
    clean_path = save_clean(raw_path)
    processed_path = transpose(clean_path)


if __name__ == '__main__':
    main()


