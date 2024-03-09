import java.util.*;
import java.io.*;

public class Battleship {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
		String InvalidCoordinates = "Invalid coordinates. Choose different coordinates.";
		String DifferentCoordinates = "You already have a ship there. Choose different coordinates.";
		char[][] battlefield1 = {{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'}};
		char[][] battlefield2 = {{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'}};
		char[][] targetHistoryBoard1 = {{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'}};
		char[][] targetHistoryBoard2 = {{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'},
					{'-', '-', '-', '-', '-'}};
		
		int[] P1Coordinates = new int[2];
		int[] P2Coordinates = new int[2];

		System.out.println("Welcome to Battleship!" + "\n");
		
		// Player 1's board
		System.out.println("PLAYER 1, ENTER YOUR SHIPS’ COORDINATES.");
		
		for (int i = 1; i < 6; i++) {
			do {
				do {
					System.out.println("Enter ship " + i + " location:");
					P1Coordinates[0] = input.nextInt();
					P1Coordinates[1] = input.nextInt();
		
					for (int j = 0; j < 2; j++) {
						if ((P1Coordinates[j] < 0) || (P1Coordinates[j] > 4)) {
							System.out.println(InvalidCoordinates);
							break;
						}
					}

				} while ((P1Coordinates[0] < 0) || (P1Coordinates[0] > 4) || (P1Coordinates[1] < 0) || (P1Coordinates[1] > 4));

				
				if (battlefield1[P1Coordinates[0]][P1Coordinates[1]] == '@') {
					System.out.println("You already have a ship there. Choose different coordinates.");
				}

				else {
					battlefield1[P1Coordinates[0]][P1Coordinates[1]] = 'T';	
				}

			} while (battlefield1[P1Coordinates[0]][P1Coordinates[1]] != 'T');	
			
			battlefield1[P1Coordinates[0]][P1Coordinates[1]] = '@';	
		}

		printBattleShip(battlefield1);
		
		for (int i = 0; i < 100; i++) {
			System.out.println(" ");
		} 

		// Player 2's board
		System.out.println("PLAYER 2, ENTER YOUR SHIPS’ COORDINATES.");
		
		for (int i = 1; i < 6; i++) {
			do {
				do {
					System.out.println("Enter ship " + i + " location:");
					P2Coordinates[0] = input.nextInt();
					P2Coordinates[1] = input.nextInt();
		
					for (int j = 0; j < 2; j++) {
						if ((P2Coordinates[j] < 0) || (P2Coordinates[j] > 4)) {
							System.out.println(InvalidCoordinates);
							break;
						}
					}

				} while ((P2Coordinates[0] < 0) || (P2Coordinates[0] > 4) || (P2Coordinates[1] < 0) || (P2Coordinates[1] > 4));

				
				if (battlefield2[P2Coordinates[0]][P2Coordinates[1]] == '@') {
					System.out.println("You already have a ship there. Choose different coordinates.");
				}

				else {
					battlefield2[P2Coordinates[0]][P2Coordinates[1]] = 'T';	
				}

			} while (battlefield2[P2Coordinates[0]][P2Coordinates[1]] != 'T');	
			
			battlefield2[P2Coordinates[0]][P2Coordinates[1]] = '@';	
		}

		printBattleShip(battlefield2);
		System.out.println(" ");
		int p = 1;
		int countP1 = 0;
		int countP2 = 0;
		boolean GameOver = false;
		
		// Game
		do {
			if (p == 1) {		
				do {
					do {
						System.out.println("Player " + p + ", enter hit row/column:");
						P1Coordinates[0] = input.nextInt();
						P1Coordinates[1] = input.nextInt();
		
						for (int j = 0; j < 2; j++) {
							if ((P1Coordinates[j] < 0) || (P1Coordinates[j] > 4)) {
								System.out.println(InvalidCoordinates);
								break;
							}
						}

					} while ((P1Coordinates[0] < 0) || (P1Coordinates[0] > 4) || (P1Coordinates[1] < 0) || (P1Coordinates[1] > 4));

					if ((targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] == 'O') || (targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] == 'X')) {
						System.out.println("You already fired on this spot. Choose different coordinates.");
					}
				
					else {
						targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] = 'T';
					}

				} while (targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] != 'T');	
			
				if (battlefield2[P1Coordinates[0]][P1Coordinates[1]] == '-') {
					targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] = 'O';
					battlefield2[P1Coordinates[0]][P1Coordinates[1]] = 'O';
					System.out.println("PLAYER " + p + " MISSED!");
					printBattleShip(targetHistoryBoard1);
					p = 2;
				}	

				else if (battlefield2[P1Coordinates[0]][P1Coordinates[1]] == '@') {
					targetHistoryBoard1[P1Coordinates[0]][P1Coordinates[1]] = 'X';
					battlefield2[P1Coordinates[0]][P1Coordinates[1]] = 'X';
					System.out.println("PLAYER " + p + " HIT PLAYER "+ (p+1) + "'s SHIP!");	
					printBattleShip(targetHistoryBoard1);			
					p = 2;	
					countP1 += 1;
					if (countP1 == 5) {
						System.out.println("PLAYER 1 WINS! YOU SUNK ALL OF YOUR OPPONENT’S SHIPS!" + "\n");
						System.out.println("Final boards:" + "\n");
						printBattleShip(battlefield1);
						System.out.println(" ");
						printBattleShip(battlefield2);
						GameOver = true;
					}
				}
			}

			else if (p == 2) {		
				do {
					do {
						System.out.println("Player " + p + ", enter hit row/column:");
						P2Coordinates[0] = input.nextInt();
						P2Coordinates[1] = input.nextInt();
		
						for (int j = 0; j < 2; j++) {
							if ((P2Coordinates[j] < 0) || (P2Coordinates[j] > 4)) {
								System.out.println(InvalidCoordinates);
								break;
							}
						}

					} while ((P2Coordinates[0] < 0) || (P2Coordinates[0] > 4) || (P2Coordinates[1] < 0) || (P2Coordinates[1] > 4));

					if ((targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] == 'O') || (targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] == 'X')) {
						System.out.println("You already fired on this spot. Choose different coordinates.");
					}
				
					else {
						targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] = 'T';
					}

				} while (targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] != 'T');	
			
				if (battlefield1[P2Coordinates[0]][P2Coordinates[1]] == '-') {
					targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] = 'O';
					battlefield1[P2Coordinates[0]][P2Coordinates[1]] = 'O';
					System.out.println("PLAYER " + p + " MISSED!");
					printBattleShip(targetHistoryBoard2);
					p = 1;
				}	

				else if (battlefield1[P2Coordinates[0]][P2Coordinates[1]] == '@') {
					targetHistoryBoard2[P2Coordinates[0]][P2Coordinates[1]] = 'X';
					battlefield1[P2Coordinates[0]][P2Coordinates[1]] = 'X';
					System.out.println("PLAYER " + p + " HIT PLAYER "+ (p-1) + "'s SHIP!");	
					printBattleShip(targetHistoryBoard2);			
					p = 1;	
					countP2 += 1;
					if (countP2 == 5) {
						System.out.println("PLAYER 2 WINS! YOU SUNK ALL OF YOUR OPPONENT’S SHIPS!" + "\n");
						System.out.println("Final boards:" + "\n");
						printBattleShip(battlefield2);
						System.out.println(" ");
						printBattleShip(battlefield1);
						GameOver = true;
					}
				}
			}

		} while (GameOver == false);
    }
    
    // Use this method to print game boards to the console.
	private static void printBattleShip(char[][] player) {
		System.out.print("  ");
		for (int row = -1; row < 5; row++) {
			if (row > -1) {
				System.out.print(row + " ");
			}
			for (int column = 0; column < 5; column++) {
				if (row == -1) {
					System.out.print(column + " ");
				} else {
					System.out.print(player[row][column] + " ");
				}
			}
			System.out.println("");
		}
	}

}
