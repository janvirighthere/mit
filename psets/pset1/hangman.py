import random
def load_file(path):
    with open(path, 'r') as file:
        print("Loading  word list from file ...")
        words = file.read().split()
                    
    print(f"{len(words)} words loaded")
    return words

def computer_guess(words):
    random_number = random.randint(0, len(words) - 1)
    #print(f"random number is : {random_number}")
    return words[random_number]

def hangman():
    print("Welcome to hangman game")
    words = load_file('words.txt')
    random_word = computer_guess(words)
    #random_guess = words[computer_guess(words)]
    print(f"I am thinking of a word that is {len(random_word)} long.")
    print("-------------------")
    
    #print(f"the random word is {random_word}")
    num_guesses = 8
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_list = list(available_letters)
    word  = ['_'] * len(random_word) 
    while num_guesses > 0 and ''.join(word) != random_word:
        print(f"You have {num_guesses} left.")
        print(f"Available letters: {''.join(letters_list)}.")
        
        guess = input("Please enter a guess: ")
        found = False

        for letter in range(len(random_word)):
            if guess.lower() == random_word[letter]:
                found = True
                word[letter] = guess.lower()
                if letter in letters_list:
                    letters_list.remove(random_word[letter])
       
        if found:
            print(f"Good guess: {''.join(word)}")
        else:
            print(f"Oops! That letter is not in my word: {''.join(word)}")
            num_guesses -= 1
    print("----------Game Over!-----------")
    if num_guesses > 0:
        print("Congratulations you won!")
    
if __name__ == '__main__':
    hangman()

