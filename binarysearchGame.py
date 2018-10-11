# A game to assitant parents playing the game with their children
# Developed by JuliaLi Oct. 11, 2018

welcome = '\nLet\'s play a game: \n\nYou choose an interger no less than 1 & no more than 1000 as your \'secrete number\', and keep it as only you know. \n\nI will make a guess and give your a number in each round. \nYou need to tell me which case is right as follow: i) It is less than the secrete number; ii) It is more than the secrete number; iii) It is the secrete number! \n\n If I can get the secrete number in 10 rounds, I win. Otherwise, you win. \n\nWill you play the game with me? \n\n Tell me by input the option charactor as follows:\n (A) Yes, Let\'s play it; (B) No, thanks.\n'

startword = '\nChoose your number and press A when you are ready. You can quit the game at any time by inputting \'quit\' \n(A) Begin (B) Exit\n'

guessword = "\n[Round {0}] I guess your secrete number is {1}.\nDid I make the guess? Which one as follos is correct?\n    (A) It is less than the secrete number; \n    (B) It is more than the secrete number; \n    (C) It is the secrete number! \n"

hintword = '\nYou can only input \'a\' or \'b\' or \'c\'. \nPlease tell me which one is correct for {0}:\n    (A) It is less than the secrete number; \n    (B) It is more than the secrete number; \n    (C) It is the secrete number! \n'

winword = '\nHaha, I got it by {0} guess! I win :D \n'
loseword = '\nWhat a pity! I lose :( \n'

def play_game(round, start, end, lastguess):
    guessnumber = int((start + end)/2)
    if (guessnumber == lastguess):
        guessnumber += 1

    print(guessword.format(round, guessnumber))

    repeat = 0
    user_input = input("Your option: ")

    while(repeat < 2):
        answer = user_input.lower().strip()
        if (answer == 'a'):
            if (guessnumber < 1000):
                start = guessnumber + 1
            else:
                start = guessnumber
            break
        elif (answer == 'b'):
            if (guessnumber > 1):
                end = guessnumber - 1
            else:
                end = guessnumber
            break
        elif (answer == 'c'):
            start = -1
            end = -1
            break
        elif (answer == 'quit'):
            start = -2
            end = -2
            break
        else:
            print(hintword.format(guessnumber))
            user_input = input("")
            repeat += 1

    if (repeat == 2):
        print ("You input wrong answer for 3 times. Game over.")
        start = -2
        end = -2

    return start, end, guessnumber


print(welcome)

start = 1
end = 1000

user_input = input("Your option: ")
round = 1
guess = -1
if ((user_input.lower().strip()) == 'a'):
    print(startword)
    user_input = input("Your option: ")

    if ((user_input.lower().strip()) == 'a'):
        for round in range(1,11):
            start, end, guess = play_game(round, start, end, guess)
            if (start == -2 and end == -2):
                print("Byebye")
                break
            elif (start == -1 and end == -1):
                print(winword.format(round))
                break
            elif(round == 10):
                print(loseword)
    else:
        print("Byebye")
else:
    print("Byebye")


