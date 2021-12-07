# 8.3 RETURN VALUES
## EXERCISE 8-8

def make_album(artist, album_title, songs = None):
    album_info = {
        'Artist' : artist.title(),
        'Album Title' : album_title.title(),
        }

    if songs:
        album_info['Number Songs'] = songs

    return(album_info)

while True:
    print("\nYou can enter music information")
    print("Type 'q' to quit at any time. ")

    artist = input("\nArtist name: ")
    if artist == 'q':
        break

    album = input ("\nAlbum title: ")
    if album == 'q':
        break

    n_songs = input("\nNumber of songs in the album: ")
    if n_songs == 'q':
        break

    entry = make_album(artist, album, n_songs)
    print(entry)
