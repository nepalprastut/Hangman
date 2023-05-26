"""
    IMPLEMENTATION OF OOP TO CREATE HANGMAN GAME
"""
import random

class HangMan:

    def __init__(self):
        self.stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        
        self.words = [
                        "algorithm", "analytics", "API", "artificial intelligence", "augmented reality",
                        "big data", "blockchain", "cloud computing", "coding", "cybersecurity",
                        "data science", "database", "deep learning", "digital", "encryption",
                        "frontend", "gaming", "hacking", "internet of things", "machine learning",
                        "mobile app", "networking", "open source", "programming", "responsive design",
                        "robotics", "server", "smartphone", "software", "virtual reality",
                        "web development", "wireless", "3D printing", "agile methodology", "API integration",
                        "biometrics", "cloud storage", "computer vision", "data mining", "e-commerce",
                        "fintech", "genetic algorithms", "Internet", "IoT devices", "nanotechnology",
                        "predictive analytics", "quantum computing", "self-driving cars", "wearable technology",
                        "UX/UI design", "video streaming"
]

        self.rand_word = random.choice(self.words)
        self.dummy = self.rand_word


    def display_stages(self, c):

        print(self.stages[c])


    def game(self):
        print(self.dummy)
        spaces = []
        c = 0
        incorrect_letters = []
        letters = []
        for o in self.rand_word:
            letters.append(o)
        correct_letters = []
        for j in self.rand_word:
                spaces.append("_ ")
        self.display_stages(0)
        print(" ".join(map(str, spaces)))

        while c<=5:

            found = 0
            while True:
                guess = input("\n\n Guess a letter -->  ").lower()

                if guess in incorrect_letters or guess in correct_letters:
                    print("Please enter a new letter.")
                else:   
                    for k in range(len(self.rand_word)):
                        if guess == self.rand_word[k]:
                            spaces[k] = guess
                            self.rand_word.replace(guess, "")
                            correct_letters.append(guess)
                            found = 1
                    if found == 0:
                        self.display_stages(c+1)
                        c += 1
                        incorrect_letters.append(guess)
                        
                    print(f"Incorrect Letters:  {incorrect_letters}\n")        
                    
                    print(" ".join(map(str, spaces)))
                    if sorted(correct_letters) == sorted(letters):
                        print(f"\n\n'{self.dummy.lower()}' is the word. You guessed it right!!!")
                        break
                    if c == 6:
                        print(f"\n\n Game over! You lose! The word was '{self.dummy.lower()}' ")
                break




while True:

    print("Welcome to Hangman! Guess the word before the Hangman completes itself to win.\n")
    play = HangMan()
    play.game()
    ask = input("Wanna play again? (y/n):  ").lower()
    if ask == 'n':
        break



