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
    
def report(freq,count):
    ll = [(v,k) for (k,v) in freq.items()]
    ll.sort(reverse=True)
    for v,k in ll[:count]:
        print("{}\t{}".format(v,k.text))


def main():
    words = Frequency()
    with open(__file__,'rt') as fi:
        text = fi.read()

    for t in tokenize(text):
        words[t]+=1
    report(words,20)


if __name__=="__main__":
    main()

# this is way overcomplicated for the problem. But it will make later code easier