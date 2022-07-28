#Punctuation removal functions
from cProfile import label
from string import punctuation

def remove_punc(text):
    ''' 
    Remove Punctuation from a text and return cleaned text
    -> clean_text = remove_punc(text)
    '''
    for punc in punctuation:
        text = text.replace(punc,'')
    return text

def word_count(text):
    wordlist = text.lower().split()
    wc = {}
    for word in wordlist:
        if word in wc:
            wc[word]+=1
        else:
            wc[word] =1
    return wc
def sort(word_dict):
    ans = sorted(word_dict.items(),key=lambda val:val[1],reverse=True)
    return dict(ans)
if __name__ == '__main__':
    long_text ='''
    The Moon is a barren, rocky world without air and water.
    It has dark lava plain on its surface. 
    The Moon is filled wit craters. 
    It has no light of its own. 
    It gets its light from the Sun. 
    The Moon keeps changing its shape as it moves round the Earth.
    It spins on its axis in 27.3 days stars were named after the Edwin Aldrin were the first ones to set their foot on the Moon on 21 July 1969 They reached the Moon in their space craft named Apollo II.
    '''
    cl_text = remove_punc(long_text)
    counted_word = word_count(cl_text)
    sorted_word = sort(counted_word)
    print(sorted_word)


