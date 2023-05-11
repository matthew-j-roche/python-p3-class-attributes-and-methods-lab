class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    @classmethod
    def add_song_to_count(cls, song):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if song.genre not in Song.genres:
            Song.genres.append(song.genre)
        if song.genre not in Song.genre_count:
            Song.genre_count[song.genre] = 1
        else:
            Song.genre_count[song.genre] += 1
   
    @classmethod    
    def add_to_artists(cls, song):
        if song.artist not in Song.artists:
            Song.artists.append(song.artist)
        if song.artist not in Song.artist_count:
            Song.artist_count[song.artist] = 1
        else:
            Song.artist_count[song.artist] += 1
