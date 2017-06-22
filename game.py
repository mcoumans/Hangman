board = []
board.append([" ", "_", "_", "_", "_", " ", " "])
for x in range(6):
    board.append([" ", "|", " ", " ", " ", " ", " "])
board.append(["X"] * 7)
board.append([" "] * 7)

# instellen
secret_word = "boeken"
secret_word_l = list(secret_word)
turn = 1
error = 0
guessed_letters = []
guessed_word = ["_"] * len(secret_word)
board.append(guessed_word)


def print_board(board):
 #   print("\n"*30)
    for row in board:
        print(" ".join(row))


def hang_it(x):
    if x == 1:
        board[1] = [" ", "|", " ", " ", "|", " ", " "]
    if x == 2:
        board[2] = [" ", "|", " ", " ", "O", " ", " "]
    if x == 3:
        board[3] = [" ", "|", " ", " ", "|", " ", " "]
    if x == 4:
        board[3] = [" ", "|", " ", "\\", "|", " ", " "]
    if x == 5:
        board[3] = [" ", "|", " ", "\\", "|", "/", " "]
    if x == 6:
        board[4] = [" ", "|", " ", " ", "|", " ", " "]
    if x == 7:
        board[5] = [" ", "|", " ", "/", " ", " ", " "]
    if x == 8:
        board[5] = [" ", "|", " ", "/", " ", "\\", " "]

def game_over():
    print_board(board)
    print("Game over!")
    exit()

def inputting():
    global turn
    guess = input("Which letter? ")
    if guess == "quit": exit()
    turn += 1
    if guess.isalpha() & len(guess) == 1:
        if guess in guessed_letters:
            print("You guessed {} already! Try again.".format(guess))
            print("Try again")
            if turn > 26: game_over()
            return False
            #inputting()
        else:
            guessed_letters.append(guess)
        return guess
    else: return False


# find indeces for guessed letter in secret word
# indices = [i for i, x in enumerate(secret_word_l) if x == guess]

print("Let's play HangMan!")
print_board(board)
print("")

# control flow
while True:
    print("Turn %s: " % turn)
    guess = inputting()
    if guess not in secret_word_l and guess != False:
        error += 1
        hang_it(error)
        if error == 8: game_over()

    indices = [i for i, x in enumerate(secret_word_l) if x == guess]
    for i in indices:
        board[9][i] = guess
    print_board(board)
    if guessed_word == secret_word_l:
        print("You win!")
        exit()



