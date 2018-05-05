# FilmLens

Course: python for developers
Steps:
1. Run python3 demo.py command on your terminal  and you can see a list of films on showing in Manor theater.
2. Then it notices you the programme is scrapping reviews from rotten tomato
2. For about ten seconds, it notices you scrapping is done.
3. Please enter the index of movie you have interest in and it shows you showing schedule of the movie.
4. Enter 'y' to continue have a view at word cloud image of the movie, close the figure window and enter 'y' in terminal to go back to list of all movies.


Please always enter the valid input.

For video demo, please refer to https://youtu.be/QgzSPVFGpNA

### Data Source: All data files are put in DataFile folder including:
	1. classic_movies.csv is a file we download form internet whose content is genres and corresponding movies.
	2. classic_movies_raw.csv whic shows movies and genres of each movie  is processed from classic_movies.csv. In classic_movies_clean.csv, we only show one genre for each movie.
	3.reviews_filmx_raw.csv is the html node of reviews scrapped from  rotten tomato website. After clean it by removing  stop word and film names, we get review_filmx_clean.txt.
	4.merge.csv merges classic_movies_clean.csv and reviews_filmx_clean.txt.
	5.workbook.xlsx shows all above data files. 

### Assumptions:
One big issue in real word situation is that movies can have the same name. 

To handle this, we simply use RottenTomato's own search and return the first hit. 

The reason why we do this is that Manor Theater doesn't provide the release year of any on-showing movie, and they identify movies by posters instead. In addition, we can not simply return the latest one because Manor sometimes play the former one. These all together makes it impossible for our programme to identify movies according to names. 
