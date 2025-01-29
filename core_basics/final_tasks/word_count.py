# Write a function that takes a sentence as input 
# and returns the number of words in it. Ignore extra spaces between words.

def count_words(sentence):
    if not sentence:
        print('Input is enpty. Reenter.')
    
    return sentence.split()
        
our_string = 'Hi there. My name is Lincoln.' # 6 words
print(len(count_words(our_string)))