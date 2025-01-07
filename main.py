def main ():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        print(count_words(text))


def count_words(text):
    words = text.split()
    return len(words)

main()