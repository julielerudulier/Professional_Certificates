public class Pond {
    
    public static void main(String[] args) {
        // Create frogs
		Frog frog1 = new Frog("Peepo");
		Frog frog2 = new Frog("Pepe", 10, 15);
		Frog frog3 = new Frog("Peepaw", 4.6, 5);
		Frog frog4 = new Frog("Frenchie", 3, 25);

		// Create flies
		Fly fly1 = new Fly(1, 3);
		Fly fly2 = new Fly(6);
		Fly fly3 = new Fly(1, 6);

		// set species to "1331 Frogs"
		frog1.setSpecies("1331 Frogs");
		frog2.setSpecies("1331 Frogs");
		frog2.setSpecies("1331 Frogs");
		frog4.setSpecies("1331 Frogs");

		// print out Peepo's description
		System.out.println(frog1.toString());

		// Have Peepo attempt to eat Fly with mass 6
		frog1.eat(fly2);

		// Print out Fly with mass 6's description
		System.out.println(fly2.toString());

		// Have Peepo grow by 8 months
		frog1.grow(8);

		// Have Peepo attempt to eat fly with mass 6
		frog1.eat(fly2);

		// Print out fly with mass 6's description
		System.out.println(fly2.toString());

		// Print out Peepo's description
		System.out.println(frog1.toString());

		// Print out own frog's description
		System.out.println(frog4.toString());

		// Have Peepaw grow by 4 months
		frog3.grow(4);

		// Print out Peepaw's description
		System.out.println(frog3.toString());

		// Print out Pepe's description
		System.out.println(frog2.toString());  
    }
}
