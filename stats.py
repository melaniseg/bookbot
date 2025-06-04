def num_of_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

char_list = {}

def char_count(text):
    lctext = text.lower()
    for char in lctext:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list

sorted_list = []
new_list = []

def sort_on(dict):
    return dict["num"]

def sort_report(raw_dict):
    for letter, count in raw_dict.items():
        if letter.isalpha():
            list_entry = dict([("char",letter), ("num", count)])
            new_list.append(list_entry)

    new_list.sort(reverse=True, key=sort_on)

    return new_list

