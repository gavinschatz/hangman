import random

class randomWord:
    global wordlist
    wordlist = ["hello", "goodbye", "random", "love"]
    
    def __init__(self):
        self.word = random.choice(wordlist)
        self.len = len(self.word)
        
    def __getitem__(self, index):
        return self.word[index]
        
    def __repr__(self):
        return self.word
        

def blankList():
    answer = randomWord()
    
    list = []
    
    for letter in range(answer.len):
        list += ["_"]
    return list, answer, answer.len

class Play():

    def __init__(self):
        self.key = blankList()
        self.list = self.key[0]
        self.answer = self.key[1]
        self.len = self.key[2]
        self.guesses = 0
        self.lettersleft = self.key[2]
        


def interface():
    print("Welcome to Hangman. Below is the amount of letters in the word:")
    
    solved = False
    answer = Play()
    
    while solved == False:
        print(answer.list)
        guess = input("Enter guess:")
        
        correct = False
        for index in range(answer.len):
            if guess == answer.answer[index]:
                print("Answer Correct!")
                answer.lettersleft -= 1
                answer.list[index] = guess
                correct = True
        
        if correct == False:
            print("Answer Incorect... keep guessing!")
            answer.guesses += 1
    
        
        print("Incorrect guesses made: " + str(answer.guesses)) 
        
        if answer.lettersleft == 0:
            solved = True
        
    print("Answer - " + str(answer.answer))
    print("Thanks for playing, bye!!!")
        
            
                
interface()
        

    
    