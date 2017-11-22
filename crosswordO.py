########################################
# AUTHORS: Nir Krieger & Oded Fogel
#
#
#
########################################

import os
import sys

# TODO main, input validation, load matrix

CORRECT_USAGE = '\nCorrect Usage: python3 crossword.py word_file matrix_file' \
                'output_file [udrlwxyz]'
ARGV_LEN_ERROR = 'ERROR: insufficient parameters!'
WORD_FILE_PATH_ERROR = 'ERROR: word_file does not exist!'
MATRIX_FILE_PATH_ERROR = 'ERROR: matrix_file does not exist!'
OUTPUT_FILE_PATH_ERROR = 'ERROR: output_file does not exist!'
INVALID_DIRECTIONS_ERROR = 'ERROR: invalid directions!'
SYS_ARGV_LEN = 5
WORD_FILE_IDX = 1
FIRST_IDX = 0
DELIMITER = ','
KNOWN_DIRECTIONS = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']


def extract_directions(directions):
    direction_set = set(list(directions.lower()))
    if not direction_set.issubset(KNOWN_DIRECTIONS):
        return False, None
    return True, list(direction_set)


def load_matrix(matrix_file, delimiter=DELIMITER):
    """
    Returns a matrix as a list of lists based on the matrix_file parameter.
    :param matrix_file:
    :param delimiter: DELIMITER (comma) by default, can be changed.
    :return: a matrix - list of lists of letters.
    """
    # Read matrix_file, location was validated in main func.
    matrix_file_handle = open(matrix_file, 'r')
    matrix = []
    # Iterate lines of matrix file content, get rid of \n
    for line in matrix_file_handle.read().splitlines():
        # Split line with known delimiter.
        matrix.append(line.split(delimiter))
    matrix_file_handle.close()  # close file handle.
    # Return the new matrix.
    return matrix


def load_words_file(words_file):
    """
    Returns a words dictionary based on words file parameter. Every item in
    the dictionary consists of a letter as the key and a list of words
    starting with that letter as the value.
    :param words_file: words_file location.
    :return: dictionary of letters and words starting with letter.
    """
    words_dict = {}  # Initialize words_dict
    # Read words from words_file location. location was validated in main func.
    words_file_handle = open(words_file, 'r')
    words_file_list = words_file_handle.read().splitlines()  # get rid of \n
    words_file_handle.close()
    # iterate words in words file list.
    for word in words_file_list:
        first_letter = word[FIRST_IDX]
        # if the first letter is not a key already:
        if first_letter not in words_dict:
            words_dict[first_letter] = [word]
        else:
            # append word to first letter key.
            words_dict[first_letter].append(word)
    return words_dict


def search_words(direction_list, words, word_count):
    """
    finds all the words that are in letters.
    :param direction_list: a list of the letters in a direction
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word appears
    :return:
    """
    for i, letter in enumerate(direction_list):
        if letter in words:
            for word in words[letter]:
                if len(word) <= len(direction_list) - i:
                    if word == ''.join(direction_list[i: i + len(word)]):
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1




def search_hori(matrix, words, word_count, is_reversed=False):
    """
    searches for the word for horizontal direction. If direction is r, searches
    the reversed line .
    :param matrix: the given matrix of letters.
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word appears
    :param is_reversed: bool arg. if the direction is l, will be true
    :return:
    """
    for line in matrix:
        if is_reversed:
            search_words(line[::-1], words, word_count)
        else:
            search_words(line, words, word_count)


def search_diag_wz(matrix, words, word_count, lines, columns,
                   is_reversed=False):
    """
    searches for the word for diagonal direction. If direction is x, searches
    the reversed line .
    :param matrix: the given matrix of letters.
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word appears
    :param lines: number of lines in matrix
    :param columns: number of columns in matrix.
    :param is_reversed: bool arg. if the direction is x, will be true
    :return:
    """
    direction_list = []
    starting line
    for current_line in range[0, ]:


def search_matrix(matrix, words, word_count, directions):
    """
    for each direction, searches the matrix for the words given.
    :param matrix: the given matrix of letters
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word appears
    :param directions: a list of the directions as given by the user
    :return:
    """
    columns = len(
        matrix[FIRST_IDX])  # FIRST_IDX=0 can be replaced with any number
    lines = len(matrix)
    for i in directions:
        if i == 'r':
            search_hori(matrix, words, word_count)
        elif i == 'l':
            search_hori(matrix, words, word_count, True)
        elif i == 'z':
            pass


def main():
    # Input validation:
    if len(sys.argv) != SYS_ARGV_LEN:
        print(ARGV_LEN_ERROR, CORRECT_USAGE)
        return
    word_file, matrix_file, output_file, directions = sys.argv[WORD_FILE_IDX:]
    # Validate input and output files.
    if not os.path.exists(word_file):
        print(WORD_FILE_PATH_ERROR, CORRECT_USAGE)
        return
    if not os.path.exists(matrix_file):
        print(MATRIX_FILE_PATH_ERROR, CORRECT_USAGE)
        return
    is_valid_directions, direction_list = extract_directions(directions)
    if not is_valid_directions:
        print(INVALID_DIRECTIONS_ERROR, CORRECT_USAGE)
        return
    # TODO load words
    words_dict = load_words_file(word_file)
    # TODO load matrix
    matrix = load_matrix(matrix_file)
    word_count = {}
    # TODO FIND WORDS IN MATRIX
    #

    search_matrix(matrix, words_dict, word_count, direction_list)
    print(word_count)


if __name__ == '__main__':
    main()
