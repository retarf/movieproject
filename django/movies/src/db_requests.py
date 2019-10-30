from movies.models import Movie
from .handlers import keys_to_lower

def save_movie(data):
    '''
    save movie if is not in database
    '''
    title = data['Title']
    if not is_movie_in_db(title):
        data = keys_to_lower(data)
        data['movie_type'] = data.pop('type', None)
        movie = Movie(**data)
        movie.save()
    else:
        movie = Movie.objects.get(title__iexact=title)

    return movie

def is_movie_in_db(title):
    exists = False
    if Movie.objects.filter(title__iexact=title).count():
        exists = True

    return exists



