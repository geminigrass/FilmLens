# FilmLens

Course: python for developers

Users can interact with program by enter valid keyboard input (case sensitive).



Please always enter the valid input.

For video demo, please refer to https://youtu.be/QgzSPVFGpNA 

Users can interact with program by enter valid keyboard input (case sensitive).

Steps:
1. Run python3 demo.py command on your terminal  and you can see a list of films on showing in Manor theater.

```
python3 demo.py
```

2. Then it notices you the programme is scrapping reviews from rotten tomato

3. For about ten seconds, it notices you scrapping is done.

4. Please enter the index of movie you have interest in and it shows you showing schedule of the movie.

5. Enter 'y' to continue have a view at word cloud image of the movie, close the figure window and enter 'y' in terminal to go back to list of all movie

Below is the demo in terminal.

```
desdeMacBook-Pro:FilmLens des$ python3 demo.py
----------Main Menu--------------------
Welcone to FilmLens!
^_^
Enter E to exit from FilmLens.

These movies are showing at Manor Cinema recently:
0 Avengers: Infinity War
1 Isle of Dogs
2 Tully
3 RBG
4 Deadpool
5 Deadpool 2
6 Solo: A Star Wars Story

Please wait. Programe is scraping reviews from these movies.....
scraping for  avengers_infinity_war ...
scraping for  isle_of_dogs ...
scraping for  tully ...
scraping for  rbg ...
scraping for  deadpool ...
scraping for  deadpool_2 ...
scraping for  solo_a_star_wars_story ...
Please enter a number to select a movie:3
--------------Showtime----------------
Showtime of the movie:  RBG  is
days:  Fri, Mon - Thu
date:  5/11, 5/14 - 5/17
time:  3:10 PM, 5:20, 7:30, 9:40 PM

continue?y/n :y
-------------Review & Recommendation-----------------
Genre of the movie:  RBG  is
Documentary
 
You may also like movies with similar genre:
'Life Is Sacred (2014)'
'My Friend Rockefeller (2015)'
'Author: The JT LeRoy Story (2016)'
'The Beatles: Eight Days a Week - The Touring Years (2016)'
"Women of '69
Unboxed"
Press y to go back:y
----------Main Menu--------------------
Welcone to FilmLens!
^_^
Enter E to exit from FilmLens.

These movies are showing at Manor Cinema recently:
0 Avengers: Infinity War
1 Isle of Dogs
2 Tully
3 RBG
4 Deadpool
5 Deadpool 2
6 Solo: A Star Wars Story

Please enter a number to select a movie:E
desdeMacBook-Pro:FilmLens des$ 
```
### Word Cloud:
Below is the word cloud of movie RGB.

![](rgb_word_cloud.png)

### Data Source:
Our data comes from

1.Manor Cinema(movies and showing schedule)

2.Rotten Tommato(reviews)

3.A file downloaded from the Internet.(genres and classic movies)

Data files: 

All data files are put in DataFile folder including:
	
1. classic_movies.csv is a file we download form internet whose content is genres and corresponding movies.
	
2. classic_movies_raw.csv whic shows movies and genres of each movie  is processed from classic_movies.csv. In classic_movies_clean.csv, we only show one genre for each movie.
	
3.reviews_filmx_raw.csv is the html node of reviews scrapped from  rotten tomato website. After clean it by removing  stop word and film names, we get review_filmx_clean.txt.
	
4.merge.csv merges classic_movies_clean.csv and reviews_filmx_clean.txt.
	
5.workbook.xlsx shows all above data files.

For detailed description, please refer to workbook under DataFile folder.

### Assumptions:
One big issue in real word situation is that movies can have the same name. 

To handle this, we simply use RottenTomato's own search and return the first hit irrespective of the release year. 

The reason why we do this is that Manor Theater doesn't provide the release year of any on-showing movie, and they identify movies by posters instead. In addition, we can not simply return the latest one because Manor sometimes play the former one. These all together makes it impossible for our programme to identify movies according to names. 
