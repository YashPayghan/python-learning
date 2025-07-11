import random
#define list of wordd from which word is choose
word_list=["apple","banana","pineapple","mango","dragonfruit","chiku","orange","grapes"]
print("Guess The Name Of Fruits")
stages=[
   '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========b
    
    ''',
     '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]
# defining lives how many time you get chanse to get word
lives=6
print("***************************YOU HAVE 6 LIVES************************")
chosen_word=random.choice(word_list)
#chossing random word from list
#define plaseholder to store"_"
placeholder=""
for char in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
#defining correct_word--
correct_word=[]
game_over=False

while not game_over:
    guess=input("enter the word you want to choose\n").lower()
    display=""
    for char in chosen_word:
        if guess==char:
            display+=char
            correct_word.append(guess)
        elif char in correct_word:
            display+=char
        else:
            display+="_"
    print("word to guess is \n",display)
    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        print("YOU HAVE",lives," LIVES LEFT")
        if lives==0:
            game_over=True
            print("*************************YOU LOST***********************")
    if "_"not in display:
        game_over=True
        print("*****************************YOU WIN************************")
  
        
