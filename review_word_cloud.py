import matplotlib.pyplot as plt
from wordcloud import WordCloud

path_file = 'DataFile/data_of_reviews/reviews_film0_clean.txt'
reviews_of_one_film = open(path_file).read()
wordcloud = WordCloud().generate(reviews_of_one_film)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()