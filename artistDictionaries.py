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

def printDictionary(d):
    for keys in d:
        print(keys, ": ", d[keys])

def printKeys(d):
    for keys in d:
        print(keys)

def guessKeyValues (d):
    guess = input("What would you like to guess for?\n\n")
    if guess in d:
        print("Ok, well what do you think the ", guess, " is?")
        userGuess = input("\n")
        if userGuess == str(d[guess]):
            print('Thats right! The ', guess, ' was', userGuess, "!\n")
            print("Here's some more info about the song\n")
            printDictionary(d)
            return True
        else:
            print("\nNo, I'm sorry that'n not right.\n\nThe ", guess, "is: ", d[guess])
            print("Here's some more info about the song.\n")
            printDictionary(d)
    else:
        print("We didn't find that information, here are some things you can guess.\n")
        printKeys(d)
    return False

guessKeyValues(myFavoriteSong)
