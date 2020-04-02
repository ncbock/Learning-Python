"""
Creating data types which give information about the song
Mr. Carter by Lil'wayne
"""


# Object with general information
myFavoriteSong = {
  "artist" : "Lil' Wayne",
  "album" : "Tha Carter III",
  "title" : "Mr. Carter",
  "length" : "5:16",
  "genre" : "Hip-Hop",
  "releaseDate" : "July 1, 2008",
  "featuredArtist": "Jay-Z",
  "songWritters" : ["Dwayne Carter", "Andrews Correa", "Sha Prescott", "Shawn Carter", "Marco Rodriguez"],
  "songProducers" : ["Infamous", "Drew Correa"],
  "topChartRanking" : 62,
  "wasNumberOne" : False,

}

for keys in myFavoriteSong:

    print(keys, " = ", myFavoriteSong[keys])
