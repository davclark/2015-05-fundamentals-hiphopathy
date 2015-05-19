__author__ = 'Dav-Z'

lyrics_file = open("JayZ/JayZ_American Gangster_American Dreamin.txt")
# print(lyrics_file.read())

for line in lyrics_file:
    line = line.rstrip()
    print(line)