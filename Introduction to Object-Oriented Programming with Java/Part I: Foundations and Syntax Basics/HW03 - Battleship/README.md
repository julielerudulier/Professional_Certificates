### HW03 - Battleship

#### **Problem Description**

For homework 03, you will be creating a recreation of the game Battleship, where two players will choose the locations of ships on a board and attempt to sink the other player’s ships by choosing coordinates to fire at.


**Solution Description**

Your program must be named Battleship.java. Please read all the steps and look at the Example Output carefully before you begin. It must work as follows:

1. Print out the message Welcome to Battleship!
2. Prompt each user to enter coordinates for five ships of length one. There must be five separate prompts for each ship (use the example below as a guide). You can expect the user input will be two ints separated by a space. The first int represents the row number and the second int represents the column number.
    * If the user enters invalid integers, print
    Invalid coordinates. Choose different coordinates.
    * If the user enters a coordinate that they had already entered, print
    You already have a ship there. Choose different coordinates.
    * After each player enters their fifth coordinate, a board representing the player’s ship locations must be printed to the console using the provided method. See step three on how to construct these Locations Boards.
    100 new lines must follow the printed board so that the other player will not see the entered coordinates and board of their opponent.
3. Create two 5x5 grids in the form of 2D arrays using the coordinates entered by the players. These Location Boards store each player's ship locations and will be used to keep track of the damage states of each player’s ships, as well as any misses. The corresponding Location Board must be printed to the console right after a player enters the coordinates of their ships.
    * A ‘–’ character must represent an empty space.
    * An ‘@’ character must represent a ship that is not hit. When the game begins, all ships will start fresh with no hits.
    * An ‘X’ character will represent a space with a ship that has been hit.
    * An ‘O’ character will represent a space that was fired upon, but since there is not ship at that location, the shot was a miss.
    * Each player’s board must have five ships of length one. Five of the 25 grid spaces will start with ships on them.
4. Additionally, you must generate two more 5x5 grids in the form of 2D arrays. These Target History Boards will allow each player to visually track their hits and misses. After each hit or miss by the player, their Target History Board must be printed to the console using the provided method.
    * On this board, an ‘X’ character must represent a hit by the player, an ‘O’ character must represent a miss by the player, and a ‘-’ character must represent a space that has not been attacked.
5. Prompt Player 1 to enter a coordinate to fire upon. You can expect the user input will be two ints separated by a space.
    * If the user enters invalid integers, print
    Invalid coordinates. Choose different coordinates.
    * If the user enters a coordinate that they had already entered, print out the following
    You already fired on this spot. Choose different coordinates.
    * If the user enters a coordinate with no ship on it, print out the following and print the updated Target History Board, where [NUM] is replaced with the attacked player’s ID.
    PLAYER [NUM] MISSED!
    * If the user enters a coordinate with a ship on it, print out the following and print the updated Target History Board, where [NUM A] is replaced with the attacking player’s ID and [NUM B] is replaced with the attacked player’s ID.
    PLAYER [NUM A] HIT PLAYER [NUM B]’s SHIP!
6. Player 2 will get a turn after each turn that Player 1 takes, which will function in the same way as Player 1’s turns.
7. When a ship is hit by a player, the Location board (which tracks the damage states) of the corresponding player’s ships must be updated. Misses should be updated on the Location board as well.
8. The program must terminate gracefully after a player wins. This will occur when all of the ‘@’ signs on their opponent’s board have been replaced with ‘X’ symbols.
    * Immediately following the move which sinks the final ship location, print the following message, where [NUM] is replaced by the winning player’s ID.:
    PLAYER [NUM] WINS! YOU SUNK ALL OF YOUR OPPONENT’S SHIPS!
    * Using the provided method, print both players’ Location Boards in order to verify the results of the game to the players. Player 1’s Location Board should be printed first.
In your solution, you must use each of the following Java features at least once:

1. A for loop (not including those used in provided code)
2. A do-while loop.
**Note:** A premade Battleship.java file will be provided for this HW. Your code MUST be written in this file. The file simply includes a method, printBattleShip(…), that MUST be used for printing 2D arrays to the console. Make sure not to alter the printBattleShip(…) method.

**HINT:** The method is used by passing in the 2D array you wish to print. For example:
printBattleShip(playerOneShotsBoard);

**Allowed Imports**

To prevent trivialization of the assignment, you may only import java.util.Scanner.


**Feature Restrictions**

There are a few features and methods in Java that overly simplify the concepts we are trying to teach or break our auto grader. For that reason, do not use any of the following in your final submission:

* var (the reserved keyword)
* System.exit
