def replace_string(word: str, old_string: str, new_string: str):
    first_letter = word[0]
    word = word.replace(old_string, new_string)
    return first_letter + word[1:]


def replace_string2(word: str,old_string: str, new_string: str):
    for count in word:
        first_char = count[0]
        word = count.replace(old_string, new_string)
        new_word = word[1:len(word):]
        return first_char + word


print(replace_string2('restart', 'r', '$'))
