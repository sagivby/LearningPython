def findWinner(player1Ans, player2Ans):
    if player1Ans == player2Ans:
        print "Its a tie"
        print ""


    winner = -1
    if player1Ans == "rock":
        if player2Ans == "scissors":
            winner = 1
        if player2Ans == "paper":
            winner = 2

    if player1Ans == "scissors":
        if player2Ans == "rock":
            winner = 2
        if player2Ans == "paper":
            winner = 1

    if player1Ans == "paper":
        if player2Ans == "scissors":
            winner = 2
        if player2Ans == "rock":
            winner = 1
    if winner > -1:
        print "The Winner is Player " + str(winner)
        print ""


while(True):
    user1 = raw_input("Hi player 1 are you ready to play Rock Paper Scissors (Yes/No)")
    user2 = raw_input("Hi player 2 are you ready to play Rock Paper Scissors (Yes/No)")

    if user1.lower() == "no" or user2.lower() == "no":
        print "Needs two for tango - see you soon"
        break

    ply1Ans = raw_input("Player 1 - Choose one your instrument: (rock/scissors/paper)")
    ply1Ans.lower()
    ply2Ans = raw_input("Player 2 - Choose one your instrument: (rock/scissors/paper)")
    ply2Ans.lower()

    findWinner(ply1Ans, ply2Ans)






