def main():
    with open("books/frankenstein.txt") as f:
        count=0
        file_contents = f.read()
        words = file_contents.split( )
        for word in words:
            count += 1
        print(count)
main()