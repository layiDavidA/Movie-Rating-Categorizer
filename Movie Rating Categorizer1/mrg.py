# #Project: Movie Rating Categorizer App

from enum import Enum
import sys
import math

header = "Rate My Flicks App".upper()
headerTwo = "Movie rating".upper()

print("")
print(header.center(50, "="))
movieName = input("What is the name of this movie \t")
print("")
movieRating = input("What is this movie rated\n ex. G, PG, PG-13, R\t ")
print("")
movieScale = input(
    "Rate this move 1-10 \n Ps. 10 being the great! and 1 being horrible. \t")
print("")
movieRec = input("Would you recomend this movie to a frined?\t")

movieR = movieRating
movieS = int(movieScale)

if movieR == "G" or movieR == "g":
    movieR = 1
elif movieR == "PG" or movieR == "pg":
    movieR = 2
elif movieR == 'PG-13' or movieR == "pg-13":
    movieR = 3
elif movieR == 'R' or movieR == 'r':
    movieR = 4
else:
    print("")
    sys.exit("Invalid Movie Rating. Try Again")

if movieS >= 7 and movieS <= 10:
    movieS = 1
elif movieS <= 3 and movieS >= 0:
    movieS = 2
else:
    print("")
    sys.exit("Invalid Movie Rating. Try Again")


class movieAdj(Enum):
    Amazing = 1
    Horrible = 2


class fullRating(Enum):
    GeneralAudience = 1
    ParentalGuidance = 2
    ParentsStronglyCautioned = 3
    Restricted = 4


print("")
print(headerTwo.center(50, "="))
print("You watched " + movieName.title() + ".")
print("This movie is rated " +
      str(fullRating(movieR)).replace('fullRating.', "") + ".")
if movieS <= 3 or movieS >= 7:
    print("You rated this movie a " + movieScale + " and you thought the movie was " +
          str(movieAdj(movieS)).replace("movieAdj.", "") + ".")
else:
    print("You rated this movie a " + movieScale + ".")
print("You would definitly recommend this movie to friends.") if movieRec == "Yes" or movieRec == "yes" else print(
    "You would not recommend this movie to friends.")
print("")
