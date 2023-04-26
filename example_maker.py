import pytest
import hypothesis
import numpy as np
import pandas as pd
import random, string


def string_maker():
    s = ""
    for i in range(10):
        s += str(i)
    return s

class Appender():
    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix
        self.suffix = suffix

    def modify(self, s):
        return self.prefix + s + self.suffix


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class RandomAppender(Appender):
    def __init__(self):
        pre = randomword(4)
        suf = randomword(3)
        super(self).__init__(prefix = pre + "_",suffix = "-" + suf)

class IndexGenerator():
    def __init__(self):
        self.characters = "0123456789".split("")
        self.length = 10

    def generate(self):
        yield "".join(random.choice(self.characters) for i in range(self.length))



