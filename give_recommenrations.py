import pandas as pd
import csv



'''
This file gives recommentations for each movie based on genres.
It's for handin of Data File submission.
Unlike demo.py is executed every time the product runs,
this file only needs to be executed once to get the cinema_clean.csv file.
'''
__author__= "Can Liu"

path_classic_movies = "./DataFile/classic_movies.csv"
path_cinema_crawl = "./DataFile/cinema_clean.csv"
path_merge = "./DataFile/merge.csv"
df_classic_movies = pd.read_csv(path_classic_movies)
genres_list = list(df_classic_movies.genre)

with open(path_cinema_crawl,'r') as csvinput:
    with open(path_merge, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('recommendations')
        all.append(row)

        for row in reader:
            genre = row[-1]

            if genre in genres_list:
                recommendations_df = df_classic_movies.loc[df_classic_movies['genre'] == genre]['recommendations']
            else:
                recommendations_df = df_classic_movies.loc[df_classic_movies['genre'] == '(no genres listed)']['recommendations']
            recommendations_list = list(recommendations_df)
            str = recommendations_list[0]

            row.append(str)
            all.append(row)
        writer.writerows(all)

