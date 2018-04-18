For submission on 4/18/2018, we analyze 2 data sources:
(1)The website of a cinema in Pittsburgh with url http://www.manorpgh.com
(2)

The files are:
(1)cinema_raw.csv:
  This file contains the raw data crawled from the Manor cinema website. 
  It crawled the showtimes for all movies that Manor cinema is playing recently.
  The Manor website HTML has the DOM hierarchy in a way that the names and showtimes are aggregated in 2 different nodes.
  In this way, for each movie, we have 2 nodes of interest: the name of the movie & the showtimes of the movie.
  Notice that, the only way to retrive the showtimes of a movie is by movie ID given by the HTML.
  This is why we need to retain information up to the movie ID in each nodes.
  
(2)cinema_clean.csv
  This file contains the cleaned data from cinema_raw.csv.
  It only retain the names and showtimes of movies.
  The movie ID is on longer incluede in this file.
  The showtimes are saved in Python dictionary format.
(3)_raw
(4)_clean
(5)merged
