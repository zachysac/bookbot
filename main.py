def word_count():
    with open("books/frankenstein.txt") as f:
        count=0
        file_contents = f.read()
        words = file_contents.split( )
        for word in words:
            count += 1
        print(f"There are {count} words in the text.")
word_count()

##this is not working
##looking for solution to increase count of letter in the dictionary
def letter_count():
     with open("books/frankenstein.txt") as f:
        lettercount = {}
        file_contents = f.read()
        lowered_string = file_contents.lower()
        for letter in lowered_string:
            if letter.isalpha():
                if letter in lettercount:
                    lettercount[letter] += 1
                else:
                    lettercount[letter] = 1
        print(lettercount)
letter_count()