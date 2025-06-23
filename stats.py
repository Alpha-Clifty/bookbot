def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dict = {}
    checked = ""
    lowercase = text.lower()
    for letter in lowercase:
        if letter.isalpha():
            checked += letter
    for c in checked:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def dict_sort(char_count):
    return dict(sorted(char_count.items(), key=lambda x: -x[1]))