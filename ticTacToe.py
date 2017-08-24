theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' ',
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    print(printBoard(theBoard))
    print('Turn for ' + turn + '. Move on which space?')
    move = raw_input()
    theBoard[move] = turn
    if turn == 'X':
        turn='O'
    else:
        turn = 'X'

print(printBoard(theBoard))


###This isn’t a complete tic-tac-toe game—for
#instance, it doesn’t ever check whether a player
#has won—but it’s enough to see how data structures can be used in programs.###
