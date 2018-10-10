#!/usr/bin/env python3

from collections import namedtuple,defaultdict
from enum import Enum

class TokenT(Enum):
    WORD = 1
    PUNCTUATION = 2

Token = namedtuple("Token",['text','type'])
        
def tokenize(text):
    for t in text.split():
        yield Token(t,TokenT.WORD)

class Frequency(defaultdict):
    def __missing__(self,key):
        return 0
    
def main():
    words = Frequency()

    for t in tokenize("foo bar foo beep baz beep"):
        words[t]+=1
    print(words)


if __name__=="__main__":
    main()

# this is way overcomplicated for the problem. But it will make later code easier