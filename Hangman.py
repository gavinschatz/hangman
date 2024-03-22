import random
# import nltk
# nltk.download('words')
# from nltk.corpus import words
# word_list = words.words()


#Creating a random word from word list, with attributes for the word and length of word
class randomWord:
    global wordlist
    wordlist = [
    'zeppelin', 'pyramid', 'mystery', 'knight', 'hurricane', 'mountain',
    'penguin', 'wizard', 'vortex', 'quicksand', 'volcano', 'eclipse',
    'treasure', 'flamingo', 'dolphin', 'chocolate', 'sphinx', 'galaxy',
    'ghost', 'keyboard', 'diamond', 'robot', 'bicycle', 'lighthouse',
    'jungle', 'rainbow', 'unicorn', 'river', 'astronaut', 'skyscraper'
]
    
    def __init__(self):
        self.word = random.choice(wordlist)
        self.len = len(self.word)
        
    def __getitem__(self, index):
        return self.word[index]
        
    def __repr__(self):
        return self.word
        

#class for all the attributes of the word
class Play():
    def blankList():
        answer = randomWord()
    
        list = []
    
        for letter in range(answer.len):
            list += ["_"]
        return list, answer, answer.len

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
        incorrectparts = ["O", "|", " \\", "/", "|", "/", "\\"]
        blanklist = [" " for letter in range(len(incorrectparts))]
        for ind in range(answer.guesses):
            blanklist[ind] = incorrectparts[ind]

        print(" _____ ")
        print("|     |  ")
        print("|     " + str(blanklist[0]) + "  ")
        print("|   " + str(blanklist[2]) + str(blanklist[1]) + str(blanklist[3]) + " ")
        print("|     " + str(blanklist[4]))
        print("|    " + str(blanklist[5]) + " " + str(blanklist[6]) + " ")
        print("---     ")
        
        templist = ""
        for letter in answer.list:
            templist += " " + str(letter)
        print(templist)   
    
    visual(answer)
    
    guessedletters = []
    while solved == False:
        guess = input("Enter guess (type quit to end): ")
        if guess == "quit":
            break
            
        if guess in guessedletters:
            print("Guess already made. Try again")
        else:
            guessedletters += guess
        
            print(guessedletters)
            correct = False
            for index in range(answer.len):
                if guess == answer.answer[index]:
                    print("Answer Correct!")
                    answer.lettersleft -= 1
                    answer.list[index] = guess
                    correct = True
        
            if correct == False:
                answer.guesses += 1
                if answer.guesses > 6:
                    visual(answer)
                    print("Game over. Try again next time.")
                    break
                print("Answer Incorect... keep guessing!")
        
            if answer.lettersleft == 0:
                solved = True
                print("Great job!")
        
        visual(answer)
        
    print("Answer - " + str(answer.answer))
    print("Thanks for playing, bye")
        
            
                
interface()
        

    
    