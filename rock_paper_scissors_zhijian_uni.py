import time
import random

def human_win(human_choice, bot_choice):
    """
    checks if the player won the round
    in order to adapt next round bot's choice
    it takes in argument the input from the player (rock, paper or scissors)
    as well as the bot choice. Returns True if the player wins False otherwise
    because for this strategy ties are treated the same way as if the player
    lost the game.
    """
    if ((human_choice == 'paper' and bot_choice == 'rock') or
        (human_choice == 'rock' and bot_choice == 'scissors') or
        (human_choice == 'scissors' and bot_choice == 'paper')) :
        return True
    return False

def best_choice(human_choice, bot_choice):
    """
    return, as a string, the best choice according to zhuijian university study
    """
    if human_win(human_choice, bot_choice):
        if human_choice == 'rock':
            return 'paper'
            #because the player will tend to play rock again
        elif human_choice == 'paper':
            return 'scissors'
            #because the player will tend to play paper again
        else :
            return 'rock'
            #because the player will tend to play scissors again
    else :
        if human_choice == 'rock':
            return random.choice(['rock', 'scissors'])
            #because the player will tend to not play rock again,
            #he or she might play scissors or paper,
            #thus the bot should not choose paper
        elif human_choice == 'paper':
            return random.choice(['rock', 'paper'])
            #because the player will tend to not play paper again
        else :
            return random.choice(['rock', 'scissors'])
            #because the player will tend to not play scissors again



def tie(human_choice, bot_choice):
    """
    checks it there is a tie, for score purposes
    return True if there is a tie otherwise returns False
    """
    if ((human_choice == 'paper' and bot_choice == 'paper') or
        (human_choice == 'rock' and bot_choice == 'rock') or
        (human_choice == 'scissors' and bot_choice == 'scissors')) :
        return True
    return False

human_score = 0
bot_score = 0
#initializing scores

bot_choice = random.choice(['rock', 'paper', 'scissors'])
#for the first round the bot choice will be random then it will adapt to
#the players choice (it could also juste be paper because people tend to
#start with rock, but it's not in the zhijian university study, so its random)


while human_score < 3 and bot_score < 3 :

    print ('Rock')
    time.sleep(0.5)
    print ('Paper')
    time.sleep(0.5)
    print('Scissors', end=' ')
    time.sleep(0.3)
    human_choice = input('Choose your weapon (rock, paper or scissors)').strip().lower()
    while (human_choice != 'rock' and
           human_choice != 'paper' and
           human_choice != 'scissors') :
           print("I don't understand")
           human_choice = input('Choose your weapon (rock, paper or scissors)').strip().lower()

    if human_win(human_choice, bot_choice) :
        human_score += 1
        print('I chose ' + bot_choice.capitalize())
        print ('Congratulation you won this round !')
    else :
        if tie(human_choice, bot_choice) :
            print('I chose ' + bot_choice.capitalize())
            print('Tie')
        else :
            bot_score += 1
            print('I chose ' + bot_choice.capitalize())
            print('AHAHA I WON this round ! ')

    time.sleep(0.3)
    print('My score: ', bot_score)
    print('Your score: ', human_score, '\n')
    bot_choice = best_choice(human_choice, bot_choice)
    time.sleep(0.5)


if human_score == 3 :
    print ('You won You are superior to me ! ')
    print("""
But it might just be luck so why don't you try to win twice juste to
be sure""")
else :
    print('You lost You are so weak')
    print("""
Actully I won because I used the stategy base on the Zhijian University
experimental study of rock, paper, scissors game, if you want to learn more
about this study here is the link to the paper :
https://www.researchgate.net/publication/261761603_Social_cycling_and_conditional_responses_in_the_Rock-Paper-Scissors_game
and here is the vice article on the paper : https://www.vice.com/en/article/gvym4x/game-theory-rock-paper-scissors
I wish you interesting reading :)
    """)
