def count_words(content):
    word_list = content.split()
    word_number = len(word_list)
    return word_number

def count_characters(content):
    character_list = (content).lower()
    character_set = set(character_list)
    dictionary = {}

    for i in character_set:
        count =  character_list.count(i)
        dictionary.update({i : count})
        
    return dictionary


def dictionary_presentation(dictionary):
    dict_list = list()

    for (key, value) in enumerate(dictionary.items()):
        dict_list.append(value)
    
    sorted_dict_list = sorted(dict_list, key=lambda x: (x[1]), reverse=True)

    return sorted_dict_list


