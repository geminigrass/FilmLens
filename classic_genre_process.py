import pandas as pd
import csv



def save_clean(path):
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
    # path = "./DataFile/classic_movies_clean.csv"# TODO:
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
    # processed_path = transpose("")#TODO


if __name__ == '__main__':
    main()


