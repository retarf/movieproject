# movieproject

Application get movies from http://www.omdbapi.com/ and save it in local database.

POST /movies   -- add movie to local database </br>
&Tab;                    Parameters: title </br>
                    Example: curl localhost/movies/ -H 'Content-Type: application/json' -d '{"title": "Batman"}'</br>                
GET /movies     -- display movies list from local database</br>
POST /comments -- add comment to movie</br>
                    Parameters: movie_id, content</br>
                    Example: curl localhost/comments/ -H 'Content-Type: application/json' -d '{"movie_id": 1, "content": "my comment"}'</br>
GET /comments  -- display comments list</br>
GET /top       -- display top list of movies base on comments number. </br>
                    Parameters: start_date, end_date (format: YYYY-MM-DD)</br>
                    Example: curl localhost/comments/?start_date=2019-10-31&end_date=2019-11-1</br>

Requirements:
* django==2,<3.0
* psycopg2>=2.7,<3.0
* django-rest-framework

Apikey:
It is required to get apikey from http://www.omdbapi.com/ and save it in /movies/key.py

Example:
    class Apikey(object):
        APIKEY = '0000ffff'
