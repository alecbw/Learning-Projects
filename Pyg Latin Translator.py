pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha() == True:
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
    
    #takes a word and translates it into pyg Latin
