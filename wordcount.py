#!/usr/bin/env python3

from collections import namedtuple
from enum import Enum

class TokenT(Enum):
    WORD = 1
    PUNCTUATION = 2

Token = namedtuple("Token",['text','type'])
        
def tokenize(text):
    for t in text.split():
        yield Token(t,TokenT.WORD)

def main():
    for t in tokenize("foo bar baz beep"):
        print(t)

if __name__=="__main__":
    main()

# this is way overcomplicated for the problem. But it will make later code easier