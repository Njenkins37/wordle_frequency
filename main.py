# This is a sample Python script.
import csv


def get_from_csv():
    list = []
    csv_path = '/Users/nickjenkins/PycharmProjects/wordle/wordle_list.csv'
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list.append(row)
    return list


def create_wordle_list(passed_list):
    shadow_list = []
    for word_func in passed_list:
        for char_func in word_func:
            shadow_list.append(char_func)
    return shadow_list


def create_freq(passed_list, letter):
    a = {}
    count = 0
    for item in freq_list:
        for key, value in item.items():
            if value == letter:
                a[key] = count + 1
                count += 1
    return a


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordle_list = get_from_csv()
    alphabet_dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [],
                     'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
                     'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    percent_dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [],
                    'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
                    'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    freq_list = []

    characters = create_wordle_list(wordle_list)
    wordle_list_copy = wordle_list.copy
    count = len(characters) * 5

    char_list = []
    for word in characters:
        for i in range(0, 5):
            char_list.append(word[i])

    for char in char_list:
        for key in alphabet_dict.keys():
            if str(char) == str(key):
                alphabet_dict[key].append(char)

    for index, char in enumerate(char_list):
        index = index % 5
        temp_dict = {}
        temp_dict[index] = char
        freq_list.append(temp_dict)

    test_list = []
    for letter in alphabet_list:
        return_list = create_freq(freq_list, letter)
        test_list.append(return_list)

    count = 0
    for item in test_list:
        print(alphabet_list[count], item)
        count += 1



