def main ():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        words = count_words(text)
        characters = count_characters(text)
        print_report(words, characters)


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    number_of_each_character = {}
    set_of_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for character in lower_text:
        if character in number_of_each_character:
            number_of_each_character[character] += 1
        elif character in set_of_characters:
            number_of_each_character[character] = 1
    
    return number_of_each_character

def print_report(words, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")

    charachter_sorted = {}
    for i in range(0, len(characters)):
        max = float("-inf")
        max_character = ""

        for charachter in characters:
            if characters[charachter] > max:
                max = characters[charachter]
                max_character = charachter

        print(f"The \'{max_character}\' charachter was found {max} times")

main()