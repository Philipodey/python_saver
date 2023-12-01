def add_to_string_length_equal_to_three(sample_input: str):
    length_of_string = len(sample_input)
    if length_of_string >= 3:
        return sample_input + "ing"


def less_than_3_dont_add_anything(sample_input: str):
    length_of_string = len(sample_input)
    if length_of_string < 3:
        return sample_input


def add_ly_to_string_if_already_end_with_ing(sample_input):
    length_of_string = len(sample_input)
    if sample_input.endswith("ing"):
        return sample_input + "ly"


def add_ly_to_string_if_already_end_with_ing2(sample_input):
    length_of_string = len(sample_input)
    if length_of_string >= 3:
        if sample_input[-3::] == "ing":
            return sample_input + "ly"


print(add_ly_to_string_if_already_end_with_ing2("sting"))
