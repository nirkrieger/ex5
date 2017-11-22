########################################
# AUTHORS: Nir Krieger & Oded Fogel
#
#
#
########################################

import os
import sys

import crossword

KNOWN_3D_DIRECTIONS = ['a', 'b', 'c']
SEPARATOR = '***'
DIRECTION_A = 0
DIRECTION_B = 1
DIRECTION_C = 2
FIRST_MAT = 0
FIRST_ROW = 0
FIRST_COLUMN = 0


def extract_3d_directions(directions):
    """

    :param directions:
    :return:
    """
    direction_set = set(list(directions.lower()))
    if not direction_set.issubset(KNOWN_3D_DIRECTIONS):
        return False, None
    return True, list(direction_set)


def load_3d_matrix(matrix_file, delimiter=crossword.DELIMITER):
    """
    Returns a matrix as a list of lists based on the matrix_file parameter.
    :param matrix_file:
    :param delimiter: DELIMITER (comma) by default, can be changed.
    :return: a 3d matrix - list of matrix that are list of lists of letters.
    """
    # Read matrix_file, location was validated in main func.
    matrix_file_handle = open(matrix_file, 'r')
    matrix_3d = []
    matrix = []
    # Iterate lines of matrix file content, get rid of \n
    for line in matrix_file_handle.read().splitlines():
        if line != SEPARATOR:
            # Split line with known delimiter.
            matrix.append([item.lower() for item in line.split(delimiter)])
        else:
            matrix_3d.append(matrix)
            matrix = []
    matrix_3d.append(matrix)
    matrix_file_handle.close()  # close file handle.
    # Return the new 3d matrix.
    return matrix_3d


def search_depth(matrix_3d, words_dict, word_count):
    """
    
    :param matrix_3d: 
    :param words_dict: 
    :param word_count: 
    :return: 
    """""
    for matrix in matrix_3d:
        crossword.search_matrix(matrix, words_dict, word_count,
                                crossword.KNOWN_DIRECTIONS)


def search_length(matrix_3d, height, words_dict, word_count):
    """

    :param matrix_3d:
    :param height:
    :param words_dict:
    :param word_count:
    :return:
    """
    for row_index in range(
            height):  # will run on the same row in every 2d matrix.
        len_matrix = []
        for mat in matrix_3d:  # will run  over all 2d matrix
            len_matrix.append(mat[row_index])
        crossword.search_matrix(len_matrix, words_dict, word_count,
                                crossword.KNOWN_DIRECTIONS)


def search_width(matrix_3d, number_of_2d_matrix, height, width, words_dict,
                 word_count):
    """

    :param matrix_3d:
    :param number_of_2d_matrix:
    :param height:
    :param width:
    :param words_dict:
    :param word_count:
    :return:
    """
    for column_index in range(
            width):  # will run over the same column in every 2d matrix
        width_matrix = []
        for mat in range(
                number_of_2d_matrix):  # will run  over every 2d matrix
            width_matrix.append([])
            for row_index in range(height):
                width_matrix[mat].append(
                    matrix_3d[mat][row_index][column_index])

        crossword.search_matrix(width_matrix, words_dict, word_count,
                                crossword.KNOWN_DIRECTIONS)


def search_3d_matrix(matrix_3d, words_dict, word_count, directions):
    """

    :param matrix_3d:
    :param words_dict:
    :param word_count:
    :param directions:
    :return:
    """
    num_of_2d_matrix = len(matrix_3d)
    height = len(matrix_3d[FIRST_MAT])
    width = len(matrix_3d[FIRST_MAT][FIRST_ROW])
    for i in directions:
        if i == KNOWN_3D_DIRECTIONS[DIRECTION_A]:
            search_depth(matrix_3d, words_dict, word_count)
        elif i == KNOWN_3D_DIRECTIONS[DIRECTION_B]:
            search_length(matrix_3d, height, words_dict, word_count)
        elif i == KNOWN_3D_DIRECTIONS[DIRECTION_C]:
            search_width(matrix_3d, num_of_2d_matrix, height, width,
                         words_dict, word_count)


def main():
    # Input validation:
    if len(sys.argv) != crossword.SYS_ARGV_LEN:
        print(crossword.ARGV_LEN_ERROR)
        return
    word_file, matrix_file, output_file, directions = sys.argv[
                                                      crossword.WORD_FILE_IDX:]
    # Validate input and output files.
    if not os.path.exists(word_file):
        print(crossword.WORD_FILE_PATH_ERROR)
        return
    if not os.path.exists(matrix_file):
        print(crossword.MATRIX_FILE_PATH_ERROR)
        return
    is_valid_directions, direction_list = extract_3d_directions(directions)
    if not is_valid_directions:
        print(crossword.INVALID_DIRECTIONS_ERROR)
        return
    # LOAD WORDS
    words_dict = crossword.load_words_file(word_file)
    # LOAD MATRIX
    matrix_3d = load_3d_matrix(matrix_file)
    word_count = {}
    if words_dict != crossword.EMPTY_DICT and matrix_3d != crossword.EMPTY_LIST:
        # RUN SEARCH 3D MATRIX
        search_3d_matrix(matrix_3d, words_dict, word_count, directions)

    crossword.write_output_file(output_file, word_count)


if __name__ == '__main__':
    main()
