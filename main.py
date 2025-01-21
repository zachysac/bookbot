print("--- Begin report of books/frankenstein.txt ---")

def word_count():
    with open("books/frankenstein.txt") as f:
        count=0
        file_contents = f.read()
        words = file_contents.split( )
        for word in words:
            count += 1
        print(f"There are {count} words in the text.")
word_count()

def sort_on(dict):
    return dict["num"]

def letter_count():
     with open("books/frankenstein.txt") as f:
        lettercount = {}
        letter_list = []
        file_contents = f.read()
        lowered_string = file_contents.lower()

        #counts letters only
        for letter in lowered_string:
            if letter.isalpha():
                if letter in lettercount:
                    lettercount[letter] += 1
                else:
                    lettercount[letter] = 1
        #create list of dictionaries
        for letter, count in lettercount.items():
            letter_list.append({"char": letter,"num": count})
        #sorts letter list from most to least using sort_on function
        letter_list.sort(reverse=True, key=sort_on)
        #prints list of items in letter list
        for letter in letter_list:
            print(f"The '{letter['char']}' character was found {letter['num']} times")

letter_count()
print("--- End report ---")