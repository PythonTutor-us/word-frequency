class WordCounter():
    def __init__(self, filename):
        self.fname = "test.txt"
        self.content = open(self.fname, 'r').read()
        my_dict = {}

        a = self.content.replace('.', ' ').replace(',', ' ').replace('!', '')

        # print(a)
        b = a.split()
        # where word represents each iterable in 'b'
        for word in b:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1

        my_list = []

        for k, v in my_dict.items():
            a_list = my_list.append((v, k))
            # you cannot return anything from a constructor (__init__ method)
            #return a_list

        b_list = sorted(a_list, reverse=True)
        tops = b_list[:20]


    def word_count_method(self):
        len(content.split())
        self.word_count = len(content.split())


    def punct_count_method(self):
        punct = ".',"

        d = {}

        for item in content:
            if item in punct:
                if item not in d:
                    d[item] = 0
                d[item] += 1
            # self.punct_count =


    def pretty_print_method(self):
        # i need this to take the value from "tops" line 81
        for element in tops:
            print(element[1], element[0])


# close file somewhere


def main():

    # to work on file in the class must input "string-indicating-file-name"
    test_file = WordCounter("test.txt")

    pretty_print_method(test_file)


if __name__ == '__main__':

    main()
