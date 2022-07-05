# Count frequency of words in given text
# Hash Table used to record frequency of each word.


def word_count(text):
    words=text.split(' ')
    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    print(word_counter)        


sample_text= 'apple banana orange apple kiwi apple grapes orange'
word_count(sample_text)