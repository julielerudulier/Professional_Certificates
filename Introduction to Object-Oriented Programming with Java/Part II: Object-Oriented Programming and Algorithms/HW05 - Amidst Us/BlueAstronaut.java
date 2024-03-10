public class BlueAstronaut extends Player implements Crewmate {
    private int numTasks;
    private int taskSpeed;
    private boolean tasksDone;

    public BlueAstronaut(String name, int susLevel, int numTasks, int taskSpeed) {
        super(name, susLevel);
        this.numTasks = numTasks;
        this.taskSpeed = taskSpeed;
    }

    public BlueAstronaut(String name) {
        super(name, 15);
        this.numTasks = 6;
        this.taskSpeed = 10;
    }

    public void emergencyMeeting() {
        boolean isFroze = this.isFrozen();
        if (!isFroze) {
            Player[] players = Player.getPlayers();
            int highestSus = 0;
            int highestSusIndex = 0;
            for (int i = 0; i < players.length; i++) {
                if (!players[i].isFrozen() && players[i].getSusLevel() > highestSus) {
                    highestSus = players[i].getSusLevel();
                    highestSusIndex = i;
                }
            }
            int count = 0;
            for (int i = 0; i < players.length; i++) {
                if (players[i].getSusLevel() == highestSus) {
                    count++;
                }
            }
            if (count == 1) {
                players[highestSusIndex].setFrozen(true);
            }
            this.gameOver();
        }
    }

    int count = 0;
	public void completeTask() {
		if (!super.isFrozen()) {
			if (taskSpeed > 20) {
				numTasks = numTasks - 2;
			} 
			else {
				numTasks = numTasks - 1;
			}
			if (numTasks <= 0) {
				numTasks = 0;
				taskSpeed = 0;
				count++;
			}
		}
	
		if (numTasks == 0 && count == 1) { 
			System.out.println("I have completed all my tasks");
			super.setSusLevel((int)(0.5 * getSusLevel()));
		}
	}
    
    public boolean equals(Object o) {
		if (o instanceof BlueAstronaut) {
			BlueAstronaut blue = (BlueAstronaut) o;
            return super.getName().equals(blue.getName()) && super.isFrozen() == blue.isFrozen() && super.getSusLevel() == blue.getSusLevel();
        }
        return false;
	}
    
    public String toString(){
        String newString = super.toString() + " I have " + this.numTasks + " left over.";
        if (this.getSusLevel() > 15){
            return newString.toUpperCase();
        }
        return newString;
    }
}
