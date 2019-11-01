DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movies',
        'USER': 'admin',
        'PASSWORD': 'mypass',
        'HOST': 'db',
        'PORT': '5432',
    }
}

class data:
    Database = DATABASES
