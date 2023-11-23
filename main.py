# Kibo FPWP Final Project
# This is our new TIC TAC TOE
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments

#Gomoku

import pyfiglet

welcome = pyfiglet.figlet_format("WELCOME    TO    GOMOKU!")
print(welcome)

#Initialising grid indices
p = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " "]]

welcome_message = """
Welcome players to New Gomoku (four in a row) on a 5x5 grid!
Here's how it works:
The program uses the first letter of each player's name to represent the player in the grid.
Enter positions as instructed by the program.
The winner must have their letter on four consecutive squares either horizontally, vertically, or diagonally.
Players kindly don't interfere with the code!
Good luck in the game and watch out!
"""
print(welcome_message)
print()
print(
  "************************************************************************")
print("This is the playing grid:")
grid = f"""
__|__A__|__B__|__C__|__D__|__E__|__
  |     |     |     |     |     |
 1|  {p[0][0]}  |  {p[0][1]}  |  {p[0][2]}  |  {p[0][3]}  |  {p[0][4]}  |1
  |_____|_____|_____|_____|_____|
  |     |     |     |     |     | 
 2|  {p[1][0]}  |  {p[1][1]}  |  {p[1][2]}  |  {p[1][3]}  |  {p[1][4]}  |2
  |_____|_____|_____|_____|_____|
  |     |     |     |     |     | 
 3|  {p[2][0]}  |  {p[2][1]}  |  {p[2][2]}  |  {p[2][3]}  |  {p[2][4]}  |3
  |_____|_____|_____|_____|_____|
  |     |     |     |     |     | 
 4|  {p[3][0]}  |  {p[3][1]}  |  {p[3][2]}  |  {p[3][3]}  |  {p[3][4]}  |4
  |_____|_____|_____|_____|_____|
  |     |     |     |     |     |
 5|  {p[4][0]}  |  {p[4][1]}  |  {p[4][2]}  |  {p[4][3]}  |  {p[4][4]}  |5
  |_____|_____|_____|_____|_____|
‾‾|  A  |  B  |  C  |  D  |  E  |‾‾     
  """
print(grid)

#Prompt the users for their names
player1 = input("Player 1: Enter your first name: ")
player2 = input("Player 2: Enter your first name: ")

while player1 == "" or player2 == "":
  print(
    "Either of the players has a blank entry! Kindly enter your names again!")
  player1 = input("Player 1: Enter your first name; ")
  player2 = input("Player 2: Enter your first name; ")

while player1[0].upper() == player2[0].upper():
  player2 = input("Player 2 kindly enter your second name: ")

fill1 = player1[0].upper()
fill2 = player2[0].upper()
player = player1
fill = fill1

#ask for input, validate and reassign
while True:
  print(f"{player.capitalize()}, it is your turn.")
  choice = input("Kindly enter a cell reference e.g A5: ")
  if choice == "":
    print("Invalid cell reference")
    continue
  if not choice[0].isalpha():
    print("Invalid cell reference")
    continue
  column = choice[0].upper()
  row = int(choice[1])
  valid = column in ["A", "B", "C", "D", "E"
                     ] and (1 <= (row) <= 5) and len(choice) == 2
  if valid:
    if column == "A":
      column = 1
    elif column == "B":
      column = 2
    elif column == "C":
      column = 3
    elif column == "D":
      column = 4
    elif column == "E":
      column = 5
    if p[row - 1][column - 1] != " ":
      print("Cell already filled, try another one!")
      continue
    else:
      p[row - 1][column - 1] = fill
    print(f"""
  __|__A__|__B__|__C__|__D__|__E__|__
    |     |     |     |     |     |
   1|  {p[0][0]}  |  {p[0][1]}  |  {p[0][2]}  |  {p[0][3]}  |  {p[0][4]}  |1
    |_____|_____|_____|_____|_____|
    |     |     |     |     |     | 
   2|  {p[1][0]}  |  {p[1][1]}  |  {p[1][2]}  |  {p[1][3]}  |  {p[1][4]}  |2
    |_____|_____|_____|_____|_____|
    |     |     |     |     |     | 
   3|  {p[2][0]}  |  {p[2][1]}  |  {p[2][2]}  |  {p[2][3]}  |  {p[2][4]}  |3
    |_____|_____|_____|_____|_____|
    |     |     |     |     |     | 
   4|  {p[3][0]}  |  {p[3][1]}  |  {p[3][2]}  |  {p[3][3]}  |  {p[3][4]}  |4
    |_____|_____|_____|_____|_____|
    |     |     |     |     |     |
   5|  {p[4][0]}  |  {p[4][1]}  |  {p[4][2]}  |  {p[4][3]}  |  {p[4][4]}  |5
    |_____|_____|_____|_____|_____|
  ‾‾|  A  |  B  |  C  |  D  |  E  |‾‾     
    """)
  else:
    print("Invalid position")
    continue

  #win rows
  for hor in p:
    if hor[0] == fill and hor[1] == fill and hor[2] == fill and hor[3] == fill:
      print(player, "has four in a row! Hence the winner is", player)
      play_again = input("Do you want to play again? (Choose yes or no)")
      if play_again.upper() == "YES":
        for m in range(0, 5):
          for n in range(0, 5):
            p[m][n] = " "
            continue
      else:
        print("Thanks for playing! Goodbye:)")
        exit()
    elif hor[1] == fill and hor[2] == fill and hor[3] == fill and hor[
        4] == fill:
      print(player, "has four in a row! Hence the winner is", player)
      play_again = input("Do you want to play again? (Choose yes or no)")
      if play_again.upper() == "YES":
        for m in range(0, 5):
          for n in range(0, 5):
            p[m][n] = " "
            continue
      else:
        print("Thanks for playing! Goodbye:)")
        exit()
#win columns
  for t in range(0, 4):
    if p[0][t] == fill and p[1][t] == fill and p[2][t] == fill and p[3][
        t] == fill:
      print(player, "has four in a row! Hence the winner is", player)
      play_again = input("Do you want to play again? (Choose yes or no)")
      if play_again.upper() == "YES":
        for m in range(0, 5):
          for n in range(0, 5):
            p[m][n] = " "
            continue
      else:
        print("Thanks for playing! Goodbye:)")
        exit()
  for q in range(0, 4):
    if p[1][q] == fill and p[2][q] == fill and p[3][q] == fill and p[4][
        q] == fill:
      print(player, "has four in a row! Hence the winner is", player)
      play_again = input("Do you want to play again? (Choose yes or no)")
      if play_again.upper() == "YES":
        for m in range(0, 5):
          for n in range(0, 5):
            p[m][n] = " "
            continue
      else:
        print("Thanks for playing! Goodbye:)")
        exit()
  #win diagonals
  #left-right diagonals
  if p[1][0] == fill and p[2][1] == fill and p[3][2] == fill and p[4][
      3] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  elif p[0][1] == fill and p[1][2] == fill and p[2][3] == fill and p[3][
      4] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  #right-left diagonals
  elif p[1][4] == fill and p[2][3] == fill and p[3][2] == fill and p[4][
      1] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  elif p[0][3] == fill and p[1][2] == fill and p[2][1] == fill and p[3][
      0] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
#main diagonals
#left-right diagonal
  elif p[0][0] == fill and p[1][1] == fill and p[2][2] == fill and p[3][
      3] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  elif p[1][1] == fill and p[2][2] == fill and p[3][3] == fill and p[4][
      4] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  #right-left diagonal
  elif p[0][4] == fill and p[1][3] == fill and p[2][2] == fill and p[3][
      1] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  elif p[1][3] == fill and p[2][2] == fill and p[3][1] == fill and p[4][
      0] == fill:
    print(player, "has four in a row! Hence the winner is", player)
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
#draw
  count = 0
  for k in range(0, 5):
    for j in range(0, 5):
      if p[k][j] != " ":
        count += 1
  if count == 25:
    print("Grid is full, there is no winner. It is a draw!")
    play_again = input("Do you want to play again? (Choose yes or no)")
    if play_again.upper() == "YES":
      for m in range(0, 5):
        for n in range(0, 5):
          p[m][n] = " "
          continue
    else:
      print("Thanks for playing! Goodbye:)")
      exit()
  if fill == fill1:
    fill = fill2
    player = player2.capitalize()
  else:
    fill = fill1
    player = player1.capitalize()
