# Tic Tac Toe 
This is a fun coding project to make the game tic-tac-toe (https://en.wikipedia.org/wiki/Tic-tac-toe). The English game 
also know as noughts and crosses. The goal of the game is for the player to place three of their marks (Xs or Os) horizontally, vertically
or diagonally. If the board is full and no player has three marks in a row, the game is a tie, also known as a cat's game. 
 
# Installation
The testing class requires the installation of parameterized to run the test cases.
 ```bash
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```
 
 # Computer Player
This version of tic-tac-toe has two computer players. 

## Random Computer Player
This is a very native implementation of a computer, where random spaces are selected by the computer to place their mark. 
The source code for the Random Computer Player can be found at https://github.com/robot255/tic_tac_toe/blob/master/players/random_computer.py
  
## MiniMax Computer Player
Currently the game implements a recursive algorithm that looks at all possible combinations, scores them accordingly, and chooses the path with the highest score. 
  
 
 # Testing 
Testing is critical for correctness and future refactoring. To achieve proper testing, both integration and unit tests 
were created. Below command will run the tests.

 ```bash
python test_tic_tac_toe.py
```

 # Future enhancements 
 - Allow for multiple players in boards that are larger then 3 
 - Test the Minimax algorithm in larger boards
 - Add argument testing to the game runner
 
