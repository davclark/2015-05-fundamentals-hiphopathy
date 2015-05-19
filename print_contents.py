__author__ = 'Dav-Z'

lyrics_file = open("JayZ/JayZ_American Gangster_American Dreamin.txt")
# print(lyrics_file.read())

# Process file and clean it up
for line in lyrics_file:
    line = line.casefold()
    # Extra Extra credit: get rid of punctuation
    # Another way to get rid of the chorus junk
    # line = line.rstrip("[chorus]")
    line = line.rstrip()
    for junk_character in [",", "'", "?", "!", "."]:
        line = line.replace(junk_character, "")

    found_junk_line = False
    for junk_line in ["[chorus]", "[chorus:]"]:
        if junk_line in line:
            found_junk_line = True

    # if "[chorus" not in line:
    if not found_junk_line:
        if line:
            print(line)

# TODO Replace [Chorus] with actual chorus text