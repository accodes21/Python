import random

words=["word","python","language","spyder","mountain","camera","diamond","pencil",
       "zoo","dream","crayon","zebra","star","bee","octopus","alligator","computer","juice",
       "motorcycle"]

word = random.choice(words)

spaces = ["_"]*len(word)

def getwordlen(guess,word,spaces):
    index = -2
    while index!=-1:
        if guess in word:
            index = word.find(guess)
            remove_char = "*"
            word = word[:index]+remove_char+word[index+1:]
            spaces[index] = guess
        else:
            index = -1
            
        return (word,spaces)

def check_win():
    for i in range(0,len(spaces)):
        if spaces[i] == "_":
            return -1
        
    return 1

num_turns = len(word)
for i in range(-1,num_turns):
    guess = input("Guess a letter:")
    
    if guess in word:
        word,spaces = getwordlen(guess, word, spaces)
        print(spaces)
        
    else:
        print("Wrong Guess!")
        
    if check_win() == 1:
        print("Congrats You WIN")
        break
    
    print("You have "+str(num_turns - i -1)+" turns left")
    print()