import java.util.Scanner;

public class Calculator {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);	
		String add = "add";
		String sub = "subtract";
		String mult = "multiply";
		String div = "divide";
		String alph = "alphabetize";	

		System.out.println("List of operations: " + add + " " + sub + " " + mult + " " + div + " " + alph + " ");
		System.out.println("Enter an operation: ");

		String typedIn = input.next();
		String operation = typedIn.toLowerCase();
		
		if (!operation.equals(add) && !operation.equals(sub) && !operation.equals(mult) && !operation.equals(div) && !operation.equals(alph)) {
			System.out.println("Invalid input entered. Terminating...");
		}

		else if (operation.equals(add) || operation.equals(sub)) {
			System.out.println("Enter two integers: ");
			if (input.hasNextInt()) {
				int digit1 = input.nextInt();

				if (input.hasNextInt()) {
					int digit2 = input.nextInt();

					if (operation.equals(add)) {
						int result = digit1 + digit2;
						System.out.print("Answer: " + result);
					}

					else if (operation.equals(sub)) {
						int result = digit1 - digit2;
						System.out.print("Answer: " + result);
					}
				}
							
				else {
					System.out.println("Invalid input entered. Terminating..." + "\n");
				}
			}			
			else {
				System.out.println("Invalid input entered. Terminating..." + "\n");
			}
		}

		else if (operation.equals(mult) || operation.equals(div)) {
		
			System.out.println("Enter two doubles: ");

			if (input.hasNextDouble()) {
				double double1 = input.nextDouble();
				
				if (input.hasNextDouble()) {
					double double2 = input.nextDouble();
					double result;

					switch (operation) {
					case "multiply":
						result = double1 * double2;
						System.out.printf("Answer: %.2f \n", result);
						break;
					case "divide":
						if (double2 == 0) { 
							System.out.println("Invalid input entered. Terminating...");
							break;
						}
						else {
							result = double1 / double2;
							System.out.printf("Answer: %.2f \n", result);
							break;
						}
					default:
						System.out.println("Invalid input entered. Terminating..." + "\n");
					}
				}

				else {
					System.out.println("Invalid input entered. Terminating..." + "\n");			
				}
			}
			
			else {
				System.out.println("Invalid input entered. Terminating..." + "\n");			
			}
		}
		
		else if (operation.equals(alph)) {

			System.out.println("Enter two words: ");

			String word1 = input.next();
			String word2 = input.next();
			String word1LC = word1.toLowerCase();
			String word2LC = word2.toLowerCase();
		
			int rank1 = word1LC.compareTo(word2LC);
			
			if (rank1 == 0) {
				System.out.println("Answer: Chicken or Egg.");
			}

			else if (rank1 < 0) {
				System.out.println("Answer: " + word1 + " comes before " + word2 + " alphabetically.");
			}
			
			else if (rank1 > 0) {
				System.out.println("Answer: " + word2 + " comes before " + word1 + " alphabetically.");				
			}
		}
	}
}
