from pathlib import Path
import index_search


def unique_words_from_list_of_strings(list_of_strings):
    unique_words = set({})
    for string in list_of_strings:
        string_set = index_search.prepare_string(string)
        unique_words.update(string_set)
    return unique_words


def find_unique_words_in_file(file):
    file = open(file, "r" )
    list_of_lines = file.read().splitlines()
    unique_words = unique_words_from_list_of_strings(list_of_lines)
    file.close()
    return unique_words


def add_file_to_index(index, file):
    file = Path(file)
    unique_words = find_unique_words_in_file(file)
    for word in unique_words:
        if word in index:
            index[word].add(file.name)
        else:
            index[word] = set({file.name})
    return index


def index_files(folder):
    index = {}
    folder = Path(folder)
    for file in folder.glob("*.bok"):
        index = add_file_to_index(index, file)
    return index


if __name__ == "__main__":
    index = index_files('books')
    print(index_search.search_index_using_string(index, 'hound, sherlock'))
