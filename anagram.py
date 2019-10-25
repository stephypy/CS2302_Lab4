# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 3- Option B Anagrams
# Instructor: Diego Aguirre
# TA: Gerardo Barraza
# Date of last modification: October 21, 2019
# Purpose: Given a file, generate an AVL or Red-Black tree and find the valid anagrams of a word


import avl
import red_black
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


def count_anagrams(english_words):
    print("Count anagrams of: ")
    word = input()
    word = word.replace("\n", "")
    print('Total anagrams of ', word, ': ', _count_anagrams(english_words, word, []))
    print_anagrams(english_words, word)


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


def get_avl_tree():
    english_words = avl.AVL()
    file = 'random.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def get_rb_tree():
    english_words = red_black.RBTree()
    file = 'random.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def main():
    print('1. AVL Tree')
    print('2. Red-Black Tree')
    type_tree = input()
    print('1. Count Anagrams')
    print('2. Greatest Num of Anagrams')
    response = input()
    if type_tree is '1':
        start = time.time()
        english_words = get_avl_tree()
        end = time.time()
        print('Getting AVL: ', end - start)
    elif type_tree is '2':
        start = time.time()
        english_words = get_rb_tree()
        end = time.time()
        print('getting red-black, ', end - start)
    else:
        print('Invalid option')
        return
    if response is '1':
        start = time.time()
        count_anagrams(english_words)
        end = time.time()
        print('Counting ', end - start)
    elif response is '2':
        start = time.time()
        greatest_anagrams(english_words)
        end = time.time()
        print('Greatest ,', end - start)
    else:
        print('Invalid option')


main()
