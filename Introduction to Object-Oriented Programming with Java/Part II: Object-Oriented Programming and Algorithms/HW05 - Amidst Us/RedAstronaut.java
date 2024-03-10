public class RedAstronaut extends Player implements Impostor {
    private String skill;

    public RedAstronaut(String name, int susLevel, String skill){
        super(name, susLevel);
        this.skill = skill;
    }

    public RedAstronaut(String name){
        super(name, 15);
        this.skill = "experienced";
    }

    public RedAstronaut(String name, int susLevel){
        super(name, susLevel);
        this.skill = "experienced";
    }

    public void emergencyMeeting(){
        boolean isFroze = this.isFrozen();
        if (!isFroze) {
            Player[] players = Player.getPlayers();
            int highestSus = 0;
            int highestSusIndex = 0;
            for (int i = 0; i < players.length; i++) {
                if (!players[i].isFrozen() && players[i].getSusLevel() > highestSus && (players[i].getName() != this.getName())) {
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

    public String testInst(Player player){
        if (super.compareTo(player) > 0){
            return "Greater";
        } else if (super.compareTo(player) < 0){
            return "Less";
        } else {
            return "Equal";
        }
    }

    public void freeze(Player player){
        if (!(player instanceof Impostor) && !this.isFrozen() && !player.isFrozen()){
            if (this.compareTo(player) < 0){
                player.setFrozen(true);
            } else {
                int susLevel = this.getSusLevel();
                susLevel = susLevel * 2;
                this.setSusLevel(susLevel);
            }
            this.gameOver();
        }
    }
    
    public void sabotage(Player player){
        if (!this.isFrozen() && !player.isFrozen() && !(player instanceof RedAstronaut)){
            int playerSusLevel = player.getSusLevel();
            double newSusLevel;
            if (this.getSusLevel() < 20){
                newSusLevel = playerSusLevel * (1 + 0.5);
            } else {
                newSusLevel = playerSusLevel * (1 + 0.25);
            }
            player.setSusLevel((int) newSusLevel);
        }
    }
    
    public boolean equals(Object o) {
		if (o instanceof RedAstronaut) {
			RedAstronaut red = (RedAstronaut) o;
      		return super.getName().equals(red.getName()) && super.isFrozen() == red.isFrozen() && super.getSusLevel() == red.getSusLevel();
       	}
       	return false;
    }
    
    public String toString(){
        String newString = super.toString() + " I am a " + this.skill + " player !";
        if (this.getSusLevel() > 15){
            return newString.toUpperCase();
        }
        return newString;
    }
}
