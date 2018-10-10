#!/usr/bin/env python3
from shlex import shlex
from collections import namedtuple,defaultdict
from enum import Enum

class TokenT(Enum):
    WORD = 1
    PUNCTUATION = 2

Token = namedtuple("Token",['text','type'])
        
def tokenize(text):
    # this is NOT what I would really use: it is designed for unix shell parsing
    s = shlex(text,punctuation_chars=True)
    s.quotes=''
    s.escape = ''
    s.escapedquotes = ''

    while True:
        t = s.get_token()
        if not t:
            break
        # TODO: figure out whether it is a word or punctuation
        # TODO: deal with apostrophe and abbreviations: 'twasn't a wee bairn in sight o' Dr. O'Reilly's flat.
        yield Token(t,TokenT.WORD)

class Frequency(defaultdict):
    # using defaultdict in this way allows you to replace
    #  if foo in bar:
    #     bar[foo]+=1
    #  else:
    #     bar[foo]=1
    # with the much simpler
    #  bar[foo]+=1
    def __missing__(self,key):
        return 0
    
def report(freq,count):
    ll = [(v,k) for (k,v) in freq.items()]
    ll.sort(reverse=True)
    for v,k in ll[:count]:
        print("{}\t{}".format(v,k.text))


# if you aren't familiar with click, I strongly encourage you to learn it.
import click
@click.command()
@click.argument("files",nargs=-1,type=click.File('rUt'))
def main(files):
    words = Frequency()
    for fname in files:
        for t in tokenize(fname):
            # TODO: distinguish between punctuation and words
            words[t]+=1
    report(words,200)


if __name__=="__main__":
    main()

