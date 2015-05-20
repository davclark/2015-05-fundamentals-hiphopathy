__author__ = 'Dav-Z'

import glob

# print(lyrics_file.read())
def clean_lyrics_file(lyrics_file, clean_file):
    clean_lines = []

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
                clean_file.write(line + '\n')
                clean_lines.append(line)

    return clean_lines


for infile in glob.glob("JayZ/*.txt"):
    # stuff below goes here!
    lyricsf = open(infile)
    cleanf = open(infile + '.clean', 'w')

    curr_clean_lines = clean_lyrics_file(lyricsf, cleanf)

    # Want to do...
    # Change to add lines from each file to a list
    print("We got", len(curr_clean_lines), "lines")

    lyricsf.close()
    cleanf.close()

# After we get all of our lines, with counts - make a plot
print("We're done!")

# At the end - example of accumulator