public class Frog extends Pond {

	// variables
	private String name;
	private int age;
	private double tongueSpeed;
	private boolean isFroglet;
	private static String species = "Rare Pepe";
	public static final int defaultAge = 5;
	public static final double defaultSpeed = 5;

	// constructors
	public Frog(String name, int age, double tongueSpeed) {
		this.name = name;
		this.age = age;
		this.tongueSpeed = tongueSpeed;
	}

	public Frog(String name, double ageInYears, double tongueSpeed) {
		this(name, (int)(ageInYears * 12), tongueSpeed);
		this.isFroglet(age);
	}

	public Frog(String name) {
		this(name, defaultAge, defaultSpeed);
		this.isFroglet(age);
	}

	// methods
	private void isFroglet(int age) {
		if (age > 1 && age < 7) {
			isFroglet = true;
		}
		else {
			isFroglet = false;
		}
	}

	public void grow (int months) {
		int oldAge = age;
		age = age + months;
		if (oldAge < 12) {
			for (int i = 0; i < months; i++) {
				tongueSpeed = tongueSpeed + 1;
				if (tongueSpeed == 12) {
					break;
				}
			}
		} 
		else if (age >= 30) {
			if ((age - months) > 30) {
				if (tongueSpeed > 5) {	
					for (int i = 0; i < months; i++) {					
						tongueSpeed = tongueSpeed - 1;
						if (tongueSpeed == 5) {
							break;
						}
					}
				}
			}
			else {
				if (tongueSpeed > 5) {
					for (int i = 0; i < (age - 30); i++) {
						tongueSpeed = tongueSpeed - 1;
						if (tongueSpeed == 5) {
							break;
						}
					}
				}	
			}
		}
		this.isFroglet(age);
	}
	
	public void grow () {
		age = age + 1;
		if (age < 12) {
			tongueSpeed = tongueSpeed + 1;
		} 
		else if (age >= 30) {
			if ((age - 1) >= 30) {
				if (tongueSpeed > 5) {	
					tongueSpeed = tongueSpeed - 1;
				}
			}
			else {
				if (tongueSpeed > 5) {
					tongueSpeed = tongueSpeed - 1;
				}	
			}
		}
		this.isFroglet(age);
	}

	public void eat(Fly fly) {
		if (fly.isDead()) {
			return;
		}
		if (tongueSpeed > fly.getSpeed()) {
			if (fly.getMass() >= (0.5 * age)) {
				this.grow();
			}
			fly.setMass(0);
		}
		else {
			fly.grow(1);
		}
	}

	public String toString() {
		if (isFroglet == true) {
			return "My name is " + name + " and I'm a rare froglet! I'm " + age + " months old and my tongue has a speed of " + (Math.round(tongueSpeed * 100.0) / 100.0) + ".";
		} 
		else {
			return "My name is " + name + " and I'm a rare frog. I'm " + age + " months old and my tongue has a speed of " + (Math.round(tongueSpeed * 100.0) / 100.0) + ".";
		}
	}

	public String getSpecies() {
		return species;
	}

	public void setSpecies (String species) {
		this.species = species;
	}

}
