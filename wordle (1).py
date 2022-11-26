import random
import sys

class bcolors:
    HEADER = '\033[95m'  # mov
    OKBLUE = '\033[94m'  # blue
    OKCYAN = '\033[96m'  # cyan
    OKGREEN = '\033[92m'  # green
    WARNING = '\033[93m'  # yellow
    FAIL = '\033[91m'  # red
    BOLD = '\033[1m'  # white
    ENDC = '\033[0m'

def print_menu():
    print("Let's play wordle: ")
    print("Type a 5 letter word and hit enter!\n")


def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words).lower()

# nltk.data.path.append('/work/words')
# word_list = words.words()
# words_five = [word for word in word_list if len(word) == 5]

print_menu()
play_again = ""
while play_again != "q":
    word = read_random_word()
    # word = random.choice(words_five)
    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                # print(bcolors.OKGREEN + (guess[i]), end=""+ bcolors.ENDC)#green
                print(f"{bcolors.OKGREEN}{guess[i]}{bcolors.ENDC}", end="")
            elif guess[i] in word:
                #print((guess[i]), end="")  # yellow
                print(f"{bcolors.WARNING}{guess[i]}{bcolors.ENDC}", end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(bcolors.FAIL + f"Congratulations! You got the wordle in {attempt}" + bcolors.ENDC)  # red
            break
        elif attempt == 6:
            print(bcolors.FAIL + f"Sorry the wordle was... {word}" + bcolors.ENDC)
    play_again = input("Want to play again? Type q to exit.")