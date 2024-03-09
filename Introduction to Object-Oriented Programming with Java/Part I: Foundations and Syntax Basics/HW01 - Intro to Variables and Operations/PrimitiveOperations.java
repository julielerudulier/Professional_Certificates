public class PrimitiveOperations {
	public static void main(String[] args) {
		// Declarae and initialize two variables
		int days = 28;
		double dailyXmasSpendings = 398.87;

		// Print each of these values out on their own line
		System.out.println("The first variable is the following integer: " + days);
		System.out.println("The second variable is the following double: " + dailyXmasSpendings);

		// Multiply these variables together, and assign the outcome to a new variable
		double totalXmasSpendings = days * dailyXmasSpendings;

		// Print out this new value
		System.out.println("28 * 398.87 is equal to: " + totalXmasSpendings);	

		// Use casting to convert the integer from the first step to a floating point value 
		float days2 = (float) days;	

		// Print out the value
		System.out.println("The converted version of the int variable 'days' is: " + days2);

		// Use casting to convert the floating point value from the first step to an integer type
		int dailyXmasSpendings2 = (int) 398.87;

		// Print out the value
		System.out.println("The converted version of the double variable 'dailyXmasSpendings' is: " + dailyXmasSpendings2);

		// Declare a char variable, and assign an uppercase letter to it
		char santa = 'S';

		// Print out this value
		System.out.println("The uppercase letter is: " + santa);

		// Using a numerical operation, change the letter to the same letter, but in lowercase and print out the new char value
		System.out.println((char) (santa + 32));
	}
}
