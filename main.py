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


def return_empty_alph_dict():
    this_dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [],
                 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
                 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    return this_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordle_list = get_from_csv()

    alphabet_dict = return_empty_alph_dict()
    percent_dict = return_empty_alph_dict()
    in_dictionary = return_empty_alph_dict()
    wrong_place_dictionary = return_empty_alph_dict()

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

    for key, value in alphabet_dict.items():
        count = len(value)
        percentage = (count / len(char_list)) * 100
        percent_dict[key] = percentage

    flipped_dict = {value: key for key, value in percent_dict.items()}

    dict_list = []
    for letter in alphabet_list:
        return_list = create_freq(freq_list, letter)
        dict_list.append(return_list)

    test_dict = {}
    test_list = []
    not_in_list = []
    not_dict = {}
    is_solved = False
    possible_list = characters.copy()
    guess_dict = {}

    while not is_solved:
        remaining_words = []
        prob_dict = {}

        guess = input("What was your guess? ")

        for i in range(0, 5):
            if i not in test_dict:
                bool_val = input(f"Was {guess[i]} in the word? ")
                if bool_val.lower() == 'yes':
                    bool_val2 = input(f"Was {guess[i]} in the correct spot? ")
                    if bool_val2.lower() == 'yes':
                        test_dict[i] = guess[i]
                    else:
                        if guess[i] not in test_list:
                            wrong_place_dictionary[guess[i]].append(i)
                            test_list.append(guess[i])
                else:
                    not_in_list.append(guess[i])
        print(wrong_place_dictionary)
        possible_list = [word for word in possible_list if all(char not in not_in_list for char in word)]
        possible_list = [word for word in possible_list if all(item in word for item in test_list)]

        temp_list = []
        for word in possible_list:
            for char in word:
                if word.count(char) > 2:
                    temp_list.append(word)

        for item in temp_list:
            if item in possible_list:
                possible_list.remove(item)

        # Adding words to remaining_words if they match certain conditions with test_dict
        for word in possible_list:
            matches = True
            for index, char in enumerate(word):
                if index in test_dict and test_dict[index] != char:
                    matches = False
                    break
            if matches:
                remaining_words.append(word.lower())

        to_be_removed = []
        for word in remaining_words:
            for index, char in enumerate(word):
                if index in not_dict.keys() and not_dict[index] == char:
                    to_be_removed.append(word)

        for item in to_be_removed:
            if item in remaining_words:
                remaining_words.remove(item)

        double_letters = []
        for word in remaining_words:
            for char in word:
                if word.count(char) > 1:
                    double_letters.append(word)

        for item in double_letters:
            if item in remaining_words:
                remaining_words.remove(item)

        print(len(remaining_words))
        print(remaining_words)

        for word in remaining_words:
            prob = 0
            for index, char in enumerate(word):
                if index in wrong_place_dictionary[char]:
                    prob = 0
                elif word.count(char) > 1 and len(remaining_words) > 0:
                    prob = 0
                else:
                    prob = prob + percent_dict[char]

            prob_dict[word] = prob

        new_list = []
        search = max(prob_dict.values())
        for key, value in prob_dict.items():
            if value == search:
                new_list.append(key)

        possible_list = remaining_words

        print(new_list)
        if len(test_dict) == 5:
            is_solved = True
