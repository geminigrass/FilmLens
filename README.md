# FilmLens
python for developers

To see the demo, run: python3 demo.py

### Assumptions:
One big issue in real word situation is that movies can have the same name. 

To handle this, we simply use RottenTomato's own search and return the first hit. 

The reson why we do this is that Manor Theater doesn't provide the release year of any on-showing movie, and they identify movies by poster instead. In addition, we can not simply return the latest one because Manor sometimes play the former one. These all together makes it impossible for our programe to identify movies according to names. 
