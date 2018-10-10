Ashley Stuteville
Ashley and 17 others are consistently creating meaningful discussions with their posts.
For a bad reason...got into PhD program for biology, boss wants me to learn programming to create programs that analyze our genetic data. I haven't found a passion for it yet because so far it has just been 100% frustrating and is completely out of my comfort zone as I have no previous computer experience...is programming something that grows on you or if you don't love it or the process of learning it from the start then you'll never get into it?

Terrel Shumway That is a really good question.

For me, I was hooked from the very beginning. I read one book on BASIC programming and spent all summer writing programs in my notebook, not caring that none of them would ever actually run.

I can imagine it could be drudgery if what you care about is really the biology. What specific issues are you running into? What is causing most of your frustration?


Ashley Stuteville to Terrel Shumway 

It is very much so because all I know or have ever done work with is genetics. I am taking a "Programming for Biologists" course that gives very specific examples in lecture, then for the homework we are given things that we may not necessarily have ever mentioned in class (for these he tells us to "Google" the answer; which for a beginner does nothing other than gives us the solution without helping us understand WHY that is the solution). I just feel like when I look at the pieces of what I'm supposed to be learning I get it completely. Then once I'm asked to put it all together to create some larger functional code none of it makes sense anymore. For instance, I am learning about creating classes. We were given examples in class with things like Time or Rectangles such that the attributes given to the class were passed very SIMPLE arguments (i.e. just integers). The homework is to create a class that opens a separate file, has 4 attributes that are supposed to be 1. file name 2. file path 3. total word count 4. punctuation types. I also have to give 3 methods that 1. counts the words in the file 2. counts the punctuation in the file 3. displays both of these results. Then the program must print to the screen the top 20 words and their counts as well as top 10 punctuations with their counts.

So for me, I find it impossible to progress because I don't even know where to begin with the more complicated stuff. For this specific example, I tried to find so many things but all Google will give me is simple examples of how classes work like my professor did.


Ashley Stuteville This is the level of complexity of examples I can find/were given to me in class:

class Time:
    '''A class for time related data'''
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(time):
        print("{:0=2d}:{:0=2d}:{:0=2d}".format(
        time.hour,
        time.minute,
        time.second
        ))

def main():
    start = Time(9, 45)
    print(pretty_time(time))

if __name__ == '__main__':
    main()




Ashley Stuteville I also feel like at this very early stage of learning a programming language for the first time, all questions should be extremely encouraged so that we can get used to formatting, how the simple functions/methods work, etc., but people tend to me more like "I taught myself so you should have to, too" or "just Google it" none of which is helpful because you NEED to have an experienced programmer to refer to when weird errors pop up or your code doesn't work whatsoever and you have no idea how to even go about figuring out what the error is referring to or why your code isn't working

Terrel Shumway to Ashley Stuteville 

I'm not sure I would use a class for this problem. I would have all of the functions they suggest, but they really don't share enough data to justify being put together. (How do I know that? hmm... too many lame assignments like this where professors try to shove OOP into a problem that doesn't need it) I might use a data class to represent the tokens (two types: word, punctuation). Reading the file and displaying the results are fairly easy. The most interesting problem here is distinguishing words and punctuation.

As a general rule, try solving a smaller problem first. Try this: 
1) Write a function to split a string into words.
2) Modify the function to distinguish words from punctuation.
3) create a function that takes the output of this function and stores each unique token in a dict. The key is the token, the value is the number of times it has occurred.
4) from this dict, create list that is sorted in order of decreasing frequency.
5) print the top twenty pairs from this list.



## 1
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

# this is way overcomplicated for the problem. But it will make later code easier