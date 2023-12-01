

sample_input = ['apple', 'banana', 'coconut', 'cucumber']
sample_input4 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]


sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]


# sample_input_1 = ['apple', 'banana', 'coconut', 'corn']


def dictionary_get(sample_1, sample_2):
    diction = {key: value for key, value in zip(sample_1, sample_2)}
    return diction


def difference(sample: list):
    differ = 0
    large = sample_list[0]
    small = sample_list[0]
    for count in sample:
        if count > large:
            large = count
        if count < small:
            small = count
        differ = large - small
    return differ

# from collections import counts
# def frequency_greater_than_value(sample):


def split_list(sample: list):
    another_list = len(sample) // 2
    return sample[:another_list]


def list_to_dictionary(sample):
    return {str(sample[0]): sample for index, sample in enumerate(sample) }


def list_to_dictionary2(input1):
    diction = {}
    for count in input1:
        index = count[0]
        diction[index] = count
        if index in diction:
            index = count[0].upper()
            diction[index] = count
    return diction


print(list_to_dictionary2(sample_input))
print(split_list(sample_input4))
# print(frequency_greater_than_value(sample_input4))
# print(difference(sample_list))
# print(list_to_function(sample_input))
