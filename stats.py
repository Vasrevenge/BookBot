def count_words(content):
    word_list = content.split()
    word_number = len(word_list)
    return word_number

def count_characters(content):
    character_list = (content).lower()
    character_set = set(character_list)
    dictionary = dict()

    for i in character_set:
        count =  character_list.count(i)
        dictionary.update({i : count})        

    return dictionary

