public class StringOperations {
	public static void main(String[] args) {

		// Create a new String object and assign it your name
		String myName = new String("JULIE");

		// Print it out
		System.out.println("My first name is: " + myName);

		// Pick the first letter in your name, and replace it with ‘A’
		myName = myName.replace('J', 'A');

		// Replace the last letter in your name with ‘Z’
		myName = myName.replace('E', 'Z');

		// Print out the result
		System.out.println("My name has been modified and is now: " + myName);

		// Declare a new String and give it the value of some web address
		String cowgirls = new String("www.cowgirls.com");

		// Print out the address
		System.out.println("My favorite website is the following: " + cowgirls);

		// Create a substring of the variable that’s just the “name” section, and concatenate the integer “1331” to the end
		int val = 1331;
		String websiteName = new String(cowgirls.substring(4, 12) + val);

		// Print out this final result
		System.out.println("The final result is: " + websiteName);
	}
}
