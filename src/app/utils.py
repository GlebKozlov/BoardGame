import functools
import string
import time

import numpy


def timer(func):
    @functools.wraps(func)
    def calculate(*args, **kwargs):
        start_time = time.time()
        exec_result = func(*args, **kwargs)
        print("Time spent for '{}' : {} ms".format(func.__name__, (time.time() - start_time) * 1000))
        return exec_result

    return calculate


def generate_board(size):
    return _get_random_matrix(size, list(string.ascii_lowercase))


def generate_used_pattern(size):
    return _get_random_matrix(size, [False])


def _get_random_matrix(size, data):
    return numpy.random.choice(data, size=(size, size))


def load_words(path):
    words = []
    with open(path) as file:
        for line in file:
            word = line.rstrip().lower()
            words.append(word)
    return words
