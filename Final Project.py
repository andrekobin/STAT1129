#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Initialize variables
options = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

#Ask player if they are ready to play before starting
def start():
    ready = input('Ready to play? (yes / no); ').lower()
    if ready == 'yes':
        random_move(player_score, computer_score)
    elif ready == 'no':
        print(':(')
    else:
        print('Invalid selection. Please try again!')
        start()

#Generate random move for the computer
def random_move(player_score, computer_score):
    computer_move = random.choice(options)
    valid(computer_move, player_score, computer_score)
    
#Check if player's move is valid choice r, p, or s
def valid(computer_move, player_score, computer_score):
    player_move = input('Make a move (rock / paper / scissors):').lower()
#If the player's move is valid, reveal the move of the computer
    if player_move in options:
        if computer_move == 'rock':
            print ('Computer chose ROCK!')
        elif computer_move == 'paper':
            print ('Computer chose PAPER!')
        elif computer_move == 'scissors':
            print ('Computer chose SCISSORS!')
        result(player_move, computer_move, player_score, computer_score)
    else:
        print("Invalid Selection. Please Try again.")
        valid(computer_move, player_score, computer_score)

#Recall function until move is valid

#Determine winner of round and adjust the scores
def result(player_move, computer_move, player_score, computer_score):
    if player_move == computer_move:      #Tie
        print('Tie!')
    elif player_move == 'rock':           #Player Rock
        if computer_move == 'paper':
            print('Haha you lose!')
            computer_score += 1
        else:
            print('You won!')
            player_score += 1
    elif player_move == 'paper':          #Player paper
        if computer_move == 'rock':
            print('You won!')
            player_score += 1
        else:
            print('Haha you lose!')
            computer_score += 1
    elif player_move == 'scissors':        #Player scissors
        if computer_move == 'rock':
            print('Haha you lose!')
            computer_score += 1
        else:
            print('You won!')
            player_score += 1
    score(player_score, computer_score)   #Return scores to score function
    
#Print scores after each round
def score(player_score, computer_score):
    print("Player:", player_score, '| Computer:', computer_score)
    play_again(player_score, computer_score)
    
#Ask player to play again or end the game
def play_again(player_score, computer_score):
    again = input('Do you want to Play Again? (yes / no): ').lower()
    if again == 'yes':
        random_move(player_score, computer_score) #Send scores back to random function and repeat for next round
    elif again == 'no':
        print('Thanks for Playing! \nFinal Score: \nPlayer:', player_score, '| Computer:', computer_score)
    else:
        print('Invalid selection. Please try again.')
        play_again(player_score, computer_score) #Recall function until valid selection is made

def main():
    print('Welcome to Rock, Paper, Scissors!')
    start()
    
#Start the game
if __name__ == "__main__":
    main()
    

