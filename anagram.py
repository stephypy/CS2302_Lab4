# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 4- Option B Anagrams
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: October 21, 2019
# Purpose: Compare the perfomance between AVL, Red-black, and B-trees

import avl
import red_black
import BTrees
import time


def print_anagrams(english_words, word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(english_words, before + after, prefix + cur)


def greatest_anagrams(english_words):
    greatest = []
    for word in english_words:
        if not greatest:
            greatest.append(word)
            greatest.append(_count_anagrams(english_words, word, []))
        else:
            count = _count_anagrams(english_words, word, [])
            if count > greatest[1]:
                greatest[0] = word
                greatest[1] = count
    print(greatest[0], 'has the greatest number of anagrams with a total of', greatest[1])


def count_anagrams(english_words, word):
    word = word.replace("\n", "")
    print('Total anagrams of ', word, ': ', _count_anagrams(english_words, word, []))
    # print_anagrams(english_words, word)


def _count_anagrams(english_words, word, li, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        if english_words.contains(str):
            li.append(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                _count_anagrams(english_words, before + after, li, prefix + cur)
    return len(li)


def get_avl_tree(file):
    english_words = avl.AVL()
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def get_rb_tree(file):
    english_words = red_black.RBTree()
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def get_btree(file, max_num_of_keys=5):
    english_words = BTrees.BTree(max_num_of_keys)
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


# Use this method to compare how different number of keys affect the perfomance of B-trees
def degrees(file, max_num_of_keys, word):
    start = time.time()
    btree_words = get_btree(file, max_num_of_keys)
    end = time.time()
    print('Getting B Tree ', end - start, 's', '\n')

    start = time.time()
    count_anagrams(btree_words, word)
    end = time.time()
    print('Counting with B Tree of ', max_num_of_keys, 'keys: ', end - start, 's')


# Compare performance amongst AVL, red-black, and B tree
def compare(file, word):
    print('AVL')
    start = time.time()
    avl_words = get_avl_tree(file)
    end = time.time()
    print('Getting AVL ', end - start, 's')

    start = time.time()
    count_anagrams(avl_words, word)
    end = time.time()
    print('Counting with AVL ', end - start, 's', '\n')

    print('Red Black')
    start = time.time()
    red_black_words = get_rb_tree(file)
    end = time.time()
    print('Getting Red-Black ', end - start, 's')

    start = time.time()
    count_anagrams(red_black_words, word)
    end = time.time()
    print('Counting with Red-Black ', end - start, 's', '\n')

    print('Default B Tree')
    start = time.time()
    default_btree_words = get_btree(file)
    end = time.time()
    print('Getting default B-tree ', end - start, 's')

    start = time.time()
    count_anagrams(default_btree_words, word)
    end = time.time()
    print('Counting with default B-tree', end - start, 's', '\n')


def main():
    print('Testing')
    print('Name of file:')
    file = input() + '.txt'
    print("Count anagrams of: ")
    word = input()

    print('Select one of the following:', '\n', '1. Compare', '\n', '2. Degrees')
    selection = input()

    if selection is '1':
        compare(file, word)
    elif selection is '2':
        print('Number of max keys')
        num_key = input()
        degrees(file, int(num_key), word)
    else:
        print('Invalid Option >:[')


if __name__ == "__main__":

    main()
