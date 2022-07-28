### Task
'''
WAP to replace all the multiples spaces into single space
'''
import re

def sub_s(text):
    quote = re.sub(" +"," ",text)
    return quote
if __name__ == "__main__":
    print(sub_s("Welcome     to                    India"))
