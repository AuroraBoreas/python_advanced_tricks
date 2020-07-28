import unicodedata
import string

def shave_mark(s):
    """remove all accents
    """
    norm_txt = unicodedata.normalize('NFD', s)
    shaved   = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)