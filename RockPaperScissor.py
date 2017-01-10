def game():
 while True:
  player1 = raw_input("please give input for 1st user:")
  player2 = raw_input("please give input for 2nd user:")
  if player1 == player2:
   print "Game Tie!!congratulation to both of u."
  elif (player1 == "rock" and player2 ==" scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
   print "player1 won!congratulation player 1!"
  else:
   print "player 2 won!congratulation player 2!" 
   break

agreement = raw_input("do u want to play rock paper scissors game?type y or n:")
if agreement == "y":
 game()
else:
 print "awww!no problem at all."
 exit()
again_agreement = raw_input("do u want to play again?type y or n:")
if again_agreement == "y":
 game()
else:
 print "ewww!we thought u like the game!"
