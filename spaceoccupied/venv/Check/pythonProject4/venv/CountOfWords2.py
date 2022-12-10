#Imported string to use "string.punctuation" in the future

import string

#I have chosen the Bee Movie script as my text to make the exercise more entertaining for me (This is a second check of the programm, to see if it works correctly).

read_file = 'bee_movie_script.txt'

#We open the file in read more - value 'f'

f = open(read_file , 'r')

#Create dictionary

d = dict()

#Create a loop to clean each line and word

for line in f:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")

#Loop, to count each word and retain the value in the form of the key

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

#We print each key with a counted value

for key in list(d.keys()):
    print(key, ":", d[key])
