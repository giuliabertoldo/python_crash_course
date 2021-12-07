# 8.3 RETURN VALUES
## EXERCISE 8-7

def make_album(artist, album_title, songs = None):
    album_info = {
        'Artist' : artist.title(),
        'Album Title' : album_title.title(),
        }

    if songs:
        album_info['Number Songs'] = songs

    return(album_info)

info1 = make_album('purple disco machine', 'exotica', songs = 10)
print(info1)

info2 = make_album('purple disco machine', 'Soulmatic')
print(info2)

info3 = make_album('dua lipa', 'dua lipa')
print(info3)
