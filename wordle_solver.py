guess = ""
feedback = ""
guess_list = []

with open('words.txt') as f:
    for line in f:
        guess_list.append(line.strip())

print("Cel mai bun cuvant de inceput: TAIOU")

for guesses in range(6):
    guess = input("word:").lower()
    print("v - verde, g - galben, a - alb")
    feedback = input("Feedback").lower()
    if feedback == "vvvvv":
        print("Well Done! Guess",guesses+1)
        break

    temp_tuple = tuple(guess_list)
    for word in temp_tuple:
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break

    counter = 0
    for word in guess_list:
        print(word,end=", ")
        counter+=1
        if counter == 7:
            print("")
            counter = 0