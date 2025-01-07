def main ():
    with open("books/frankenstein.txt") as file:
        text = file.read()
    print(text)


main()