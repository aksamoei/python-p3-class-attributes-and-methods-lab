class Song:
    '''blueprints song'''
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        '''initialize attributes'''
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        '''update song count'''
        cls.count += increment

    @classmethod
    def add_to_genres(cls, gen):
        '''updates genres'''
        if gen not in cls.genres:
            cls.genres.append(gen)

    @classmethod
    def add_to_artists(cls, art):
        '''update artists'''
        if art not in cls.artists:
            cls.artists.append(art)

    @classmethod
    def add_to_genre_count(cls, gen):
        '''adds genre count'''
        if gen not in cls.genre_count:
            cls.genre_count[gen] = 1
        else:
            cls.genre_count[gen] += 1

    @classmethod
    def add_to_artist_count(cls, art):
        '''adds artist count'''
        if art not in cls.artist_count:
            cls.artist_count[art] = 1
        else:
            cls.artist_count[art] += 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")



