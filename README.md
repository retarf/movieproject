# movieproject

Application get movies from http://www.omdbapi.com/ and save it in local database.

POST /movies   -- add movie to local database
                    Parameters: title
                    Example: curl localhost/movies/ -H 'Content-Type: application/json' -d '{"title": "Batman"}'
GET /movies     -- display movies list from local database
POST /comments -- add comment to movie
                    Parameters: movie_id, content
                    Example: curl localhost/comments/ -H 'Content-Type: application/json' -d '{"movie_id": 1, "content": "my comment"}'
GET /comments  -- display comments list
GET /top       -- display top list of movies base on comments number. 
                    Parameters: start_date, end_date (format: YYYY-MM-DD)
                    Example: curl localhost/comments/?start_date=2019-10-31&end_date=2019-11-1

Requirements:
- django==2,<3.0
- psycopg2>=2.7,<3.0
- django-rest-framework

Apikey:
It is required to get apikey from http://www.omdbapi.com/ and save it in /movies/key.py

Example:
    class Apikey(object):
        APIKEY = '0000ffff'
