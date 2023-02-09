import random
word_list = ["ardvrak","baboon","camel"]
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# chosing a random word from list
chosen_word = random.choice(word_list)
print(chosen_word)

# making an empty list for no of blanks
display = []
length = len(chosen_word)

# making no of blanks same as word
for _ in range(length):
    display += "_"

end_of_game = False

# taking input from user
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You loose")
            
    
    # replacing the blank with guessed word
    for position in range(length):
        letter = chosen_word[position] # first it will take first letter of chosen word and so on.
        
        if letter == guess:            
            display[position] = letter  # replace blank with the guessed word.
            
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")
    
