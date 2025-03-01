"""
Welcome to two player tic tac toe. Something fun to play and do during quarentine. 
You can ether play tic tac toe which family or get a laugh from the Pig Latin translator. 
I have sumbitted both codes
Think of it as a quarentine boardgame bundle. 
"""
# Using numbers to create the board and key areas that will help create inputs
game_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in game_board:
    board_keys.append(key)


# GAME NOTES. ISSUE AND PROBLEMS THAT CAME UP.
# Attempt 1- ok the board is not updating and now all i see is an X on my screen.
# Attempt 2-Need to create a updated board function, in order to have the board update each round
# Something along the lines of "printBoard" might work.O
# - Ok I think it is working will see. 
# New issue. cant figure out how to get an end of game message to display after player presses (n) to not continue game. 
#New Issue. Also need to fix if player presses random key I need my code to say please
# try another key between 1-9. Every code i have tried has not works. 


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
    
print('Welcome to tic tac toe may the best human win. ')
print('The board lay out uses numbers 1-9')
print('Each number has a corresponding square to it')
print('Starting from the bottom left is 1')
print('Seond row far left is 4')
print('The Top left starts with 7 ')
print('The numbers go from left to right')
print('Hopefully that helps each player understand the lay out of the board. ')
print('Thank You and enjoy the game')

# Main function for all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(game_board)
        print("Its your turn what will you do," + turn + ".Move to which place?")

        move = input()        

        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nChoose another place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ': # across the top
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Congrats")                
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ': # across the middle
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Congrats")
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ': # across the bottom
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Good Job")
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ': # down the left side
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. YAY!!")
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ': # down the middle
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. WOOT")
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ': # down the right side
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Go You")
                break 
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ': # diagonal
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Amazing")
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ': # diagonal
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" Player " +turn + " won. Amamzing Play.")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        #  change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #  player wants to restart the game or not.
    restart = input("Would you like to play again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            game_board[key] = " "

        game()

if __name__ == "__main__":
    game()

