import re
import string

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

def is_palindrome_mine(str):
    newStr = str.lower().replace(" ","").translate(str.maketrans("", "", string.punctuation))
    result = newStr == newStr[::-1]
    return result

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome_mine("Abc C b a"))
    print(is_palindrome_mine("Go hang a salami, I'm a lasagna hog."))  # true

