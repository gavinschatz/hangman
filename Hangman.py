import random

class randomWord:
    global wordlist
    wordlist = ["hello", "goodbye", "random", "love"]
    
    def __init__(self):
        self.word = random.choice(wordlist)
        self.len = len(self.word)
        
        
word = randomWord()
print(word.word)
print(word.len)