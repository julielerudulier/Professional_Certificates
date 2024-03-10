public abstract class Pet {

	// Variables 
	private String name;
	private double health; //A percentage value ranging from 0.0 to 1.0
	private int painLevel; //Ranges from 1 to 10

	// Constructor
	public Pet(String name, double health, int painLevel) {
		this.name = name;
		if (health >= 1.0) {
			this.health = 1.0;
		} else if (health <= 0.0) {
			this.health = 0.0;
		} else {
			this.health = health;
		}
		if (painLevel >= 10) {
			this.painLevel = 10;
		} else if (painLevel <= 1) {
			this.painLevel = 1;
		} else {
			this.painLevel = painLevel;
		}
	}

	// Methods
	public String getName() {
		return name;
	}

	public double getHealth() {
		return health;
	}

	public int getPainLevel() {
		return painLevel;
	}

	public abstract int treat();

	public void speak() {
		String output = String.format("Hello! My name is %s", name);
		output = (painLevel > 5) ? output.toUpperCase() : output;
		System.out.println(output);	
	}

	public boolean equals(Object o) {
		if (o instanceof Pet) {
            		Pet pet = (Pet) o;
            		return pet.name.equals(name);
        	}
        	return false;
    	}	
	
	protected void heal() {
		health = 1.0;
		painLevel = 1;
	}
}
