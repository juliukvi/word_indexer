from complete_index import load_index  # Here we load the complete index


def remove_chars(string):
    remove_list = [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!',
                   '\n']
    for char in remove_list:
        string = string.replace(char, "")
    return string


def find_unique_words(string):
    string = string.strip().lower()
    word_list = string.split(" ")
    word_set = set(word_list)
    return word_set


def set_intersection(setlist):
    u = set.intersection(*setlist)
    return u


def search_index_using_set(index, search_set):
    result_list = []
    for word in search_set:
        if word in index:
            result_list.append(index[word])
    result_set = set_intersection(result_list)
    return result_set


def prepare_string(search_string):
    search_string = remove_chars(search_string)
    search_set = find_unique_words(search_string)

    return search_set


def search_index_using_string(index, search_string):
    search_set = prepare_string(search_string)
    books = search_index_using_set(index, search_set)
    return books


if __name__ == "__main__":
    search_string = "Sherlock Holmes, scarlet"
    index = load_index()
    print(search_index_using_string(index, search_string))
    # {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}