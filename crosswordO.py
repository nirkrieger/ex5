########################################
# AUTHORS: Nir Krieger & Oded Fogel
#
#
#
########################################

import os
import sys

ARGV_LEN_ERROR = 'ERROR: invalid number of parameters. Please enter ' \
                 'word_file matrix_file output_file directions.'
WORD_FILE_PATH_ERROR = 'ERROR: Word file word_list.txt does not exist'
MATRIX_FILE_PATH_ERROR = 'ERROR: Matrix file mat.txt does not exist.'
INVALID_DIRECTIONS_ERROR = 'ERROR: invalid directions.'
OUTPUT_LINE_FORMAT = "%s%s%s\n"
SYS_ARGV_LEN = 5
WORD_FILE_IDX = 1
FIRST_IDX = 0
FIRST_COLUMN = 0
FIRST_ROW = 0
EMPTY_DICT = {}
EMPTY_LIST = []
DELIMITER = ','
DIRECTION_U = 0
DIRECTION_D = 1
DIRECTION_R = 2
DIRECTION_L = 3
DIRECTION_W = 4
DIRECTION_X = 5
DIRECTION_Y = 6
DIRECTION_Z = 7
KNOWN_DIRECTIONS = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']


def search_words(search_list, words_dict, word_count):
    """
    finds all the words that are in letters.
    :param direction_list: a list of the letters in a direction
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word apprears
    :return:
    """

    for i, letter in enumerate(search_list):
        if letter not in words_dict:
            continue
        for word in words_dict[letter]:
            if len(word) <= len(search_list) - i:
                if word == ''.join(search_list[i: i + len(word)]):
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1


def search_single_right_diagonal(matrix, height, width, words_dict, word_count,
                                 row_index=0, column_index=0,
                                 is_reversed=False):
    """

    :param matrix:
    :param height:
    :param width:
    :param words_dict:
    :param word_count:
    :param is_reversed:
    :return:
    """
    i = row_index
    j = column_index
    search_list = []
    while i <= height - 1 and j <= width - 1:
        search_list.append(matrix[i][j])
        i += 1
        j += 1
    if is_reversed:
        search_words(search_list[::-1], words_dict, word_count)
    else:
        search_words(search_list, words_dict, word_count)


def search_diagonal_right(matrix, height, width, words_dict, word_count,
                          is_reversed=False):
    """

    :param matrix:
    :param height:
    :param width:
    :param words_dict:
    :param word_count:
    :param is_reversed:
    :return:
    """
    if height == 1 or width == 1:
        return
    for row_index in range(height):
        search_single_right_diagonal(matrix, height, width, words_dict,
                                     word_count, row_index, FIRST_COLUMN,
                                     is_reversed)
    for column_index in range(1, width):
        search_single_right_diagonal(matrix, height, width, words_dict,
                                     word_count, FIRST_ROW, column_index,
                                     is_reversed)


def search_single_left_diagonal(matrix, height, width, words_dict, word_count,
                                row_index, column_index,
                                is_reversed=False):
    """

    :param matrix:
    :param height:
    :param width:
    :param words_dict:
    :param word_count:
    :param row_index:
    :param column_index:
    :param is_reversed:
    :return:
    """
    i = row_index
    j = column_index
    search_list = []
    while i <= height - 1 and j >= 0:
        search_list.append(matrix[i][j])
        i += 1
        j -= 1
    if is_reversed:
        search_words(search_list[::-1], words_dict, word_count)
    else:
        search_words(search_list, words_dict, word_count)


def search_diagonal_left(matrix, height, width, words_dict, word_count,
                         is_reversed=False):
    """

    :param matrix:
    :param height:
    :param width:
    :param words_dict:
    :param word_count:
    :param is_reversed:
    :return:
    """
    if height == 1 or width == 1:
        return
    for column_index in range(1, width):
        search_single_left_diagonal(matrix, height, width, words_dict,
                                    word_count, FIRST_ROW, column_index,
                                    is_reversed)
    for row_index in range(1, height - 1):
        search_single_left_diagonal(matrix, height, width, words_dict,
                                    word_count, row_index, width - 1,
                                    is_reversed)


def search_horizontal(matrix, height, width, words_dict, word_count,
                      is_reversed=False):
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
            search_words(line[::-1], words_dict, word_count)
        else:
            search_words(line, words_dict, word_count)


def search_vertical(matrix, height, width, words_dict, word_count,
                    is_reversed=False):
    """

    :param matrix:
    :param words_dict:
    :param word_count:
    :param is_reversed:
    :return:
    """
    for column_index in range(width):
        search_list = []
        for row_index in range(height):
            search_list.append(matrix[row_index][column_index])
        if is_reversed:
            search_words(search_list[::-1], words_dict, word_count)
        else:
            search_words(search_list, words_dict, word_count)


def search_matrix(matrix, words_dict, word_count, directions):
    """

    :param matrix:
    :param words_dict:
    :param word_count:
    :param directions:
    :return:
    """
    height = len(matrix)
    width = len(matrix[FIRST_ROW])
    for direction in directions:
        if direction == KNOWN_DIRECTIONS[DIRECTION_U]:
            search_vertical(matrix, height, width, words_dict, word_count,
                            is_reversed=True)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_D]:
            search_vertical(matrix, height, width, words_dict, word_count)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_L]:
            search_horizontal(matrix, height, width, words_dict, word_count,
                              is_reversed=True)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_R]:
            search_horizontal(matrix, height, width, words_dict, word_count)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_X]:
            search_diagonal_right(matrix, height, width, words_dict,
                                  word_count, is_reversed=True)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_Y]:
            search_diagonal_right(matrix, height, width, words_dict,
                                  word_count)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_W]:
            search_diagonal_left(matrix, height, width, words_dict,
                                 word_count, is_reversed=True)
        elif direction == KNOWN_DIRECTIONS[DIRECTION_Z]:
            search_diagonal_left(matrix, height, width, words_dict,
                                 word_count)
        else:
            pass  # WTF.


def extract_directions(directions):
    """

    :param directions:
    :return:
    """
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
        matrix.append([item.lower() for item in line.split(delimiter)])
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
        word = word.lower()
        first_letter = word[FIRST_IDX]
        # if the first letter is not a key already:
        if first_letter not in words_dict:
            words_dict[first_letter] = [word]
        else:
            # append word to first letter key.
            words_dict[first_letter].append(word)
    return words_dict


def write_output_file(output_path, word_count, delimiter=','):
    """

    :param output_path:
    :param word_count:
    :return:
    """
    word_count_keys = sorted(word_count)
    with open(output_path, 'w') as output_file_h:
        for key in word_count_keys:
            output_file_h.write(OUTPUT_LINE_FORMAT % (key, delimiter,
                                                      str(word_count[key])))


def main():
    # Input validation:
    if len(sys.argv) != SYS_ARGV_LEN:
        print(ARGV_LEN_ERROR)
        return
    word_file, matrix_file, output_file, directions = sys.argv[WORD_FILE_IDX:]
    # Validate input and output files.
    if not os.path.exists(word_file):
        print(WORD_FILE_PATH_ERROR)
        return
    if not os.path.exists(matrix_file):
        print(MATRIX_FILE_PATH_ERROR)
        return
    is_valid_directions, direction_list = extract_directions(directions)
    if not is_valid_directions:
        print(INVALID_DIRECTIONS_ERROR)
        return
    # LOAD WORDS
    words_dict = load_words_file(word_file)
    # LOAD MATRIX
    matrix = load_matrix(matrix_file)
    word_count = {}

    if words_dict != EMPTY_DICT and matrix != EMPTY_LIST:
        # RUN SEARCH MATRIX
        search_matrix(matrix, wordds_ict, word_count, directions)

    write_output_file(output_file, word_count)


if __name__ == '__main__':
    main()
