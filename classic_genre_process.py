import pandas as pd

def main():
    df_movies = pd.read_csv("./DataFile/classic_movies_raw.csv")
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


if __name__ == '__main__':
    main()


