__author__ = 'Dav-Z'

lyrics_file = open("JayZ/JayZ_American Gangster_American Dreamin.txt")
# print(lyrics_file.read())

# Process file and clean it up
for line in lyrics_file:
    line = line.rstrip()
    if line:
        print(line)