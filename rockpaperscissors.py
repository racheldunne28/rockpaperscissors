# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:24:30 2020

@author: rachel.dunne
"""

import random
import pandas as pd

def create_winner_matrix():
    """ Create matrix showing who wins in each pair of selections:
        0 = draw
        -1 = computer wins
        1 = user wins"""
    matrix = pd.DataFrame(list(zip([0,-1,1], [-1,0,1], [1,-1,0])), 
                          columns = ["rock", "paper", "scissors"],
                          index = ["rock", "paper", "scissors"])
    return(matrix)



def determine_winner(user_selection, computer_selection, winner_matrix):
    """Takes user and computer selections and returns corresponding matrix element
    from winner matrix"""
    result= winner_matrix.loc[user_selection, computer_selection]
    return(result)
    
def check_input(user_selection):
    """Checks user selection is a valid input"""
    while user_selection not in ["rock", "paper", "scissors"]:
        print("Invalid selection")
        user_selection = input("Type rock, paper or scissors: ")
    return(user_selection)
    


def rockpaperscissors(rounds):
    """ Play as many rounds of rock, paper, scissors as rounds entered"""
    options = ["rock", "paper", "scissors"]
    print("New game started: ")
    matrix = create_winner_matrix()
    rounds_played = 0
    overall_score = 0
    while rounds_played < rounds:
        user_selection = input("Type rock, paper or scissors: ")
        user_selection = check_input(user_selection)
        computer_selection = options[random.randint(0,2)]
        rounds_played = rounds_played + 1
        result = determine_winner(user_selection, computer_selection, matrix)
        overall_score = overall_score + result
        if result == 0:
            print(computer_selection)
            print("It's a draw")
        elif result == -1:
            print(computer_selection)
            print("The computer wins")
        elif result == 1:
            print(computer_selection)
            print("You win")         
    if overall_score > 0:
        print("End of game: You win overall")
    elif overall_score == 0:
        print("End of game: It's a draw")
    elif overall_score < 0:
        print("End of game: Computer wins overall")
        

rockpaperscissors(3)
 
    
