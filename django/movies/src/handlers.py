def keys_to_lower(base_dict):
    '''
    change dictionary keys to lowercase
    '''

    return dict((key.lower(), value) for key, value in base_dict.items())

def title_url(title):
    '''
    change spaces to %20
    '''

    return title.replace(' ', '%20')
