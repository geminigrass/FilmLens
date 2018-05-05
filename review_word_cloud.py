import matplotlib.pyplot as plt
from wordcloud import WordCloud

__author__= "Yizhuan Jiang"
def show_word_cloud(choise):
    path_file = choise
    reviews_of_one_film = open(path_file).read()
    wordcloud = WordCloud().generate(reviews_of_one_film)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
