
# Relative path to the file you  want to analyze.
filename = './books/frankenstein.txt'

with open(filename) as f:
    book = f.read()
    print()

    # print(book) 


def count_words(words):
    """Counts the amount of words in any given book"""
    num_of_words = words.split()
    return f'{len(num_of_words)} words found in the document \n'
    

def character_count(books):
    """Takes the text from a book as a string, and returns the number of times
    each character appears in the string."""
    character_list = []
    for character in books.lower():
        character_list.append(character)
    character_dict = {}
    for character in character_list:
        if character.isalpha():
            # Todo This function (.isalpha())is new to me, it checks if a character is part of the alphabet.
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    # print(character_dict)
    return character_dict

def sort(dict):
    """Takes a dictionary and sort it smallest to largest by value"""
    sorted_dict = {}
    for key in sorted(dict, key=dict.get, reverse=True):
        sorted_dict[key] = dict[key]
    for key in sorted_dict:
        print(f'The {key} character was found {sorted_dict[key]} times')
    print('--End report--')

def report():
    """Builds a report analysis of a given text"""
    print(f'--Begin report of {filename.strip('.')}')
    print(f'{count_words(book)}\n')
    sort(character_count(book))


def test():
    report()

def main():
    test()    
        

main()










# ----------------------------------------------------------------------------------------------------------------------------------------------
"""
! Practice examples below this line:"""

example_sentence = "thE year was 1979 and the three musketeers where in the middle of the civil war 'fighting' a 'losing battle."
# 'e' appears 14 times in this sentence. We're going to start small and build up,
# let's build a function that counts how many times the letter e appears in this sentence.
# The function should return a dictionary with the letter and the count in the following format:
"""
{word: 'number_of_times' (integer)}"""

def num_of_letters(sentence):
    character_list = []
    for word in sentence.lower():
        character_list.append(word)
    # print(character_list)
    # Up to this point, the output of 'character_list' is a list of characters, I can iterate over this list
    character_dict = {}
    for character in character_list:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    for letter in character_dict:
        if letter.isalpha():
            print(f'{letter}: {character_dict[letter]}')
    return character_dict

# dictionary_report = num_of_letters(example_sentence)


