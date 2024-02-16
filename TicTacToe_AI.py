# Tic Tac Toe Game in Python using Simple AI

"""
To do this in python we will create a list called board that will start off with 10 empty values. The reason we have 10 empty values rather than 9 is because when we get input from the user they can type numbers 1-9 NOT 0-8. So to make our lives easier we are going make the first value of our list an empty string. This way when we index elements in our list we can use 1-9 not 0-8.
"""
board = [' ' for x in range(10)] # board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



def insertLetter(letter, pos):
    """
    This function is going to take two parameters: letter & pos. It is simply going to insert the given letter at the given position.
    """
    board[pos] = letter



def spaceIsFree(pos):
    """
    This function will simply tell us if the given space is free. Meaning it does not already contain a letter. It has one parameter, pos, which will be an integer from 1-9.
    """
    return board[pos] == ' '



def printBoard(board):
    """
    This function takes the board as a parameter and will display it to the console.
    """
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')



def isWinner(board, letter):
    """
    This function will tell us if the given letter has won based on the current board. It has two parameters: bo(board) & le(letter). The letter must be a “X” or an “O”. We will simply check each possible winning line on the board and see if it is populated by the given letter.
    """
    return (board[7]==letter and board[8]==letter and board[9]==letter) or (board[4]==letter and board[5]==letter and board[6]==letter) or (board[1]==letter and board[2]==letter and board[3]==letter) or (board[1]==letter and board[4]==letter and board[7]==letter) or (board[2]==letter and board[5]==letter and board[8]==letter) or (board[3]==letter and board[6]==letter and board[9]==letter) or (board[1]==letter and board[5]==letter and board[9]==letter) or (board[3]==letter and board[5]==letter and board[7]==letter)



def isBoardFull(board):
    """
    This function takes board as parameter and will simply return True if the board is full and False if it is not.
    """
    return not board.count(' ') > 1



#Function for player move on the basis of position, Player => 'X'
def playerMove():
    """
    In this function we will be asking the user to input a move and validating it. If the move is valid we will add that letter to the board. Otherwise we will continue to ask the user for input.
    """
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if 1 <= move <= 9:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')



def computerMove():
    """
    Now time for the AI! This function will be responsible for making the computers move. It will examine the board and determine which move is the best to make. The algorithm we will follow to do this is listed below.

    If the current step cannot be completed proceed to the next.

    step 1: If there is a winning move take it.
    step 2: If the player has a possible winning move on their next turn move into that position.
    step 3: Take any one of the corners. If more than one is available randomly decide.
    step 4: Take the center position.
    step 5: Take one of the edges. If more than one is available randomly decide.
    step 6: If no move is possible the game is a tie.
    """
    possibleMoves = [x for x, Letter in enumerate(board) if x!=0 and Letter==' ']
    move = 0

    #step 1 + step 2
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    #step 3
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #step 4
    if 5 in possibleMoves:
        move = 5
        return move
    
    #step 5
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    #step 6
    return move



def selectRandom(sequence):
    """
    This function will randomly decide on a move to take given a list of possible positions.
    """
    from random import choice

    return choice(sequence)



#Function to clear the terminal after playing each game 
def clearScreen():
    from os import system, name

    system('cls' if name=='nt' else 'clear' )



#Main Function
def main():
    print('Welcome to Tic Tac Toe!')
    global board
    board = [' ' for x in range(10)]
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print("Sorry O's won this time!")
            break

        if not isWinner(board, 'X'):
            move = computerMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print(f"Computer placed an 'O' in position {move}:")
                printBoard(board)
        else:
            print("X's won this time! Good Job!")
            break

    if isBoardFull(board):
        print('Tie Game!')



#Game Starts from here
play = True
while play:
    clearScreen()
    main()
    play = input('Play again Y/N? ').lower()
    if play == 'y':
        play = True
    else:
        print('Good Bye!')
        play = False