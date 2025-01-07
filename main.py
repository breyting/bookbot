def main ():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        print(count_words(text))


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    number_of_each_character = {}

    for character in lower_text:
        if character in number_of_each_character:
            number_of_each_character[character] += 1
        else:
            number_of_each_character[character] = 1
    
    return number_of_each_character

main()