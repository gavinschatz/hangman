import random

#Creating a random word from word list, with attributes for the word and length of word
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
        
#Method for creating the initial blank list with the correct amount of letters
def blankList():
    answer = randomWord()
    
    list = []
    
    for letter in range(answer.len):
        list += ["_"]
    return list, answer, answer.len

#class for all the attributes of the word
class Play():
    def __init__(self):
        self.key = blankList()
        self.list = self.key[0]
        self.answer = self.key[1]
        self.len = self.key[2]
        self.guesses = 0
        self.lettersleft = self.key[2]
        
#Section for making guesses, showing the board
def interface():
    print("Welcome to Hangman. Below is the amount of letters in the word:")
    
    solved = False
    answer = Play()
    
    #To print out the interface
    def visual(answer):
        incorrectparts = ["O", " \\", "|", "/", "|", "/", "\\"]
        blanklist = [" " for letter in range(len(incorrectparts))]
        for ind in range(answer.guesses):
            blanklist[ind] = incorrectparts[ind]

        print(" _____ ")
        print("|     |  ")
        print("|     " + str(blanklist[0]) + "  ")
        print("|   " + str(blanklist[1]) + str(blanklist[2]) + str(blanklist[3]) + " ")
        print("|     " + str(blanklist[4]))
        print("|    " + str(blanklist[5]) + " " + str(blanklist[6]) + " ")
        print("---     ")
        
        templist = ""
        for letter in answer.list:
            templist += " " + str(letter)
        print(templist)
        

    
    while solved == False:
        guess = input("Enter guess (type quit to end): ")
        if guess == "quit":
            break
        
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
        
        visual(answer)
        
    print("Answer - " + str(answer.answer))
    print("Thanks for playing, bye!!!")
        
            
                
interface()
        

    
    