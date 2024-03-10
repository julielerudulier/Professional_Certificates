public class Fly extends Pond {

	// variables
	private double mass;
	private double speed;

	public static final double defaultMass = 5;
	public static final double defaultSpeed = 10;

	// constructors
	public Fly(double mass, double speed) {
		this.mass = mass;
		this.speed = speed;
	}

	public Fly(double mass) {
		this(mass, defaultSpeed);
	}

	public Fly() {
		this(defaultMass, defaultSpeed);
	}

	// getters
	public double getMass() {
		return mass;
	}

	public double getSpeed() {
		return speed;
	}

	// setters
	public void setMass(double mass) {
		this.mass = mass;
	}

	public void setSpeed(double speed) {
		this.speed = speed;
	}

	// toString
	public String toString() {
		if (mass == 0) {
			return "I'm dead, but I used to be a fly with a speed of " + (Math.round(speed * 100.0) / 100.0) + ".";
		}
		else {
			return "I'm a speedy fly with " + (Math.round(speed * 100.0) / 100.0) + " speed and " + (Math.round(mass * 100.0) / 100.0) + " mass.";
		}
	}

	// methods
	public void grow(int addedMass) {
		int i = 0;
		while (i != addedMass) {
			mass++;
			if (mass <= 20) {
				speed++;
			}
			else {
				speed = speed - 0.5;
			}
			i++;
		}
	}

	public boolean isDead() {
		if (mass == 0) {
			return true;
		}
		else {
			return false;
		}
	}
}
