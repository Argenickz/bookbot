def get_num_words(text):
        num_words = len(text.split())
        return num_words

def count_characters(text):
        character_dicto = {}
        for character in text.lower():
            character_dicto[character] = character_dicto.get(character, 0) + 1
        return character_dicto



def sort_dict(dict):
        return dict['count']

def create_dictionaries(dictionary):
    # Create a list to append all the dictionaries
    dict_list = []
    # Create a new dictionary with a new key for the letters key, and a new value for the letters value
    for letter in dictionary:
        dict_list.append({'letter': letter, 'count': dictionary[letter]})
        dict_list.sort(reverse=True, key=sort_dict)
    return dict_list

def print_report(sorted_list, path, word_count):
      print('============ BOOKBOT ============')
      print(f'Analyzing book found at {path}...')
      print('----------- Word Count ----------')
      print(f'Found {word_count} total words')
      print('--------- Character Count -------')
      for char in sorted_list:
            if char['letter'].isalpha():
                  print(f'{char['letter']}: {char['count']}')
      print('============= END ===============')
        
          
        
        
              



