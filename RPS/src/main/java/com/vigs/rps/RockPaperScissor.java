package com.vigs.rps;

import java.util.ArrayList;
import java.util.Random;

public class RockPaperScissor {
	
	private static final int NUM_CHOICES = 3;
	
	public enum Choice{
		/**
		 *  ordering is important here, because thats what we are going to use to determine seniority(rank)
		 */
		ROCK(1),
		PAPER(2),
		SCISSOR(3);
		
		int intVal;
		
		Choice(int intVal){
			this.intVal = intVal;
		}
		
		public static Choice forValue(int intVal) {
			for(Choice c: Choice.values()) {
				if(c.intVal==intVal) return c;
			}
			return null;
		}
		
		public int getIntValue() {
			return intVal;
		}
	}
	
	public enum Winner{
		USER,
		COMPUTER,
		DRAW
	}
	
	public class Round{
		final int roundNum;
		final Choice userChoice;
		final Choice computerChoice;
		final Winner winner;
		
		Round(int roundNum, Choice userChoice, Choice computerChoice, Winner winner){
			this.roundNum = roundNum;
			this.userChoice = userChoice;
			this.computerChoice = computerChoice;
			this.winner = winner;
		}
		
		public String toString() {
			StringBuffer buff = new StringBuffer("Round: " + this.roundNum)
								.append(", User: ").append(userChoice)
								.append(", Computer: ").append(computerChoice)
								.append(", Winner: ").append(this.winner);
			return buff.toString();
		}
	}
	
	private Random randomNum = new Random();
	
	public RockPaperScissor() {
	}

	public Round playRound(int roundNum) throws Exception{
		System.out.format("Enter your choice (number 1, 2 or 3)\n %s\n %s \n %s", "1. Rock", "2. Paper", "3. Scissor");
		
		int userInput = readUserInput("");
		int computerSelection = randomNum.nextInt(NUM_CHOICES) + 1;
		
		Choice userChoice = Choice.forValue(userInput);
		Choice computerChoice = Choice.forValue(computerSelection);
		
		int choiceDiff = Math.abs(userChoice.getIntValue()-computerChoice.getIntValue());
		Winner winner = null;
		switch (choiceDiff) {
		case 0:
			winner = Winner.DRAW;
			break;
		case 1:
			winner = userChoice.getIntValue()>computerChoice.getIntValue()?Winner.USER:Winner.COMPUTER;
			break;
		case 2:
			//cyclic seniority comes into play
			winner = userChoice.getIntValue()>computerChoice.getIntValue()?Winner.COMPUTER:Winner.USER;
			break;
		}
		
		return new Round(roundNum, userChoice, computerChoice, winner);
	}
	
	public void playGame(int numRounds) throws Exception{
		ArrayList<Round> rounds = new ArrayList<Round>();
		
		int userScore = 0;
		int computerScore = 0;
		int draws = 0;
		for(int i=1;i<=numRounds;i++) {
			Round round = playRound(i);
			rounds.add(round);
			if(round.winner==Winner.USER) {
				userScore++;
			}else if(round.winner==Winner.COMPUTER) {
				computerScore++;
			}else {
				draws++;
			}
		}
		
		
		System.out.println("\n\nRESULTS");
		for(Round round: rounds) {
			System.out.println(round);	
		}

		System.out.format("FINAL SCORE \nUser: %s\nComputer: %s\nDraws: %s", userScore, computerScore, draws);
		
	}
	
	private static int readUserInput(String message) throws Exception{
		String input = null;
		while(input==null) {
			System.out.println(message);
			byte[] b = new byte[10];
			System.in.read(b);
			
			input = new String(b).trim();
			if(!input.matches("\\d")) {
				input = null;
			}
		}
		
		return Integer.parseInt(input);		
	}
	
	public static void main(String args[]) throws Exception{

		int numRounds = readUserInput("How many rounds? ");
		
		new RockPaperScissor().playGame(numRounds);
	}
	
}
