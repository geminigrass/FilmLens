import matplotlib.pyplot as plt
from wordcloud import WordCloud

# path_file = 'DataFile/data_of_reviews/reviews_film7_clean.txt'
# reviews_of_one_film = open(path_file).read()
# wordcloud = WordCloud().generate(reviews_of_one_film)
#
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

dict = {
    0:'DataFile/reviews_film0_clean.txt',
    1:'DataFile/reviews_film1_clean.txt',
    2:'DataFile/reviews_film2_clean.txt',
    3:'DataFile/reviews_film3_clean.txt',
    4:'DataFile/reviews_film4_clean.txt',
    5:'DataFile/reviews_film5_clean.txt',
    6:'DataFile/reviews_film6_clean.txt',
    7:'DataFile/reviews_film7_clean.txt',
    8:'DataFile/reviews_film8_clean.txt',
}
def show_word_cloud(choise):
    print(choise.__class__)
    print(choise)
    path_file = dict[choise]
    print(path_file)

    reviews_of_one_film = open(path_file).read()
    wordcloud = WordCloud().generate(reviews_of_one_film)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# def main():
#     show_word_cloud(2)
#
# if __name__ == "__main__":
#     main()