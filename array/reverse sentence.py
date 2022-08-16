def sentence_reverse(sentence):
    word = sentence.split()
    word.reverse()
    return ' '.join(word)


user = input('Enter a sentence: ')
txt = sentence_reverse(user)
print('Reversed sentence: ', txt)
