#!/usr/bin/env python3

class Token:
    def __init__(self,text):
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return "<Token text='{}'>".format(self.text)
        
def tokenize(text):
    for t in text.split():
        yield Token(t)

def main():
    for t in tokenize("foo bar baz beep"):
        print(t)

if __name__=="__main__":
    main()

# this is way overcomplicated for the problem. But it will make later code easier