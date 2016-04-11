import test

number_of_words = {}
count = 0
text = open('test.txt')

for line in text:
    line = line.rstrip()
    words = line.split(" ")
    # print line
    # print words
    for word in words:
        words = number_of_words.get(word, 0) 
        count = words + 1
        print "{} {}".format(word, count)
        # number_of_words[word] = 0 + 1
        # print number_of_words
