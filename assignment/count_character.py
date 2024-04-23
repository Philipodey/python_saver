def count_character_in_list(word: str):
    new_word = {}
    for index in word:
        if index not in new_word:
            new_word[index] = 1
        else:
            new_word[index] += 1
    return new_word


# print(count_character_in_list("semicolon.africa"))
