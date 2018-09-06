'''
3. Most of the puzzles produced by the previous program are much too hard. Modify
the program so that it gives the user a threeletter
puzzle to start and then adjusts the
number of letters up by one every time a correct answer is given and down by one for
every wrong answer. In this way, the program will generally produce puzzles that are
at the user’s level.

Rather than keeping all possible words in a single list, you should use a dictionary. If
the dictionary is called wordlists , then wordlists[7] should be a list of all words in
Pride and Prejudice that are seven letters long.
'''

import random
import functions as f

list_words = f.word_arr()

