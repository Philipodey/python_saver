sample_string = 'google.com'


# def count_character(word: str)
def characters(word: str):
    result = {}
    for character in word:
        result[character] = word.count(character)
    return result


print(characters(sample_string))


def count_occurrence_in_a_string(word: str):
    result = {}
    for character in word:
        if character in result.keys():
            result[character] += 1
        else:
            result[character] = 1
    return result


print(count_occurrence_in_a_string(sample_string))


def character_frequency(words: str):
    return {word: words.count(word) for word in words}


print(character_frequency(sample_string))
