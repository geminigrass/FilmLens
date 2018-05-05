# FilmLens

python for developers

To see the demo, run:

```
python3 demo.py
```

Users can interact with program by enter valid keyboard input (case sensitive).

Please always enter the valid input.

For video demo, please refer to https://youtu.be/QgzSPVFGpNA

### Command Line Interface:

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

1.Manor Cinema

2.Rotten Tommato 

3.A file downloaded from the Internet.

For detailed description, please refer to workbook.xlsx under DataFile folder.


### Assumptions:
One big issue in real word situation is that movies can have the same name. 

To handle this, we simply use RottenTomato's own search and return the first hit irrespective of the release year. 

The reson why we do this is that Manor Theater doesn't provide the release year of any on-showing movie, and they identify movies by poster instead. In addition, we can not simply return the latest one because Manor sometimes play the former one. These all together makes it impossible for our programe to identify movies according to names. 
