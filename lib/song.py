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

        # Add to song count
        Song.count += 1

        # Track unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Track unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

print(ninety_nine_problems.name) 
print(ninety_nine_problems.artist)     
print(ninety_nine_problems.genre)     

print(Song.count)                     
print(Song.genres)                     
print(Song.artists)                    
print(Song.genre_count)                
print(Song.artist_count)               
