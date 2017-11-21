########################################
# AUTHORS: Nir Krieger & Oded Fogel
#
#
#
########################################


def search_words(direction_list, words, word_count):
    """
    finds all the words that are in letters.
    :param direction_list: a list of the letters in a direction
    :param words: a dictionary with all the words that begin with a letter
    :param word_count: a dictionary that counts how many times a word apprears
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


def main():
    pass


if __name__ == '__main__':
    main()
