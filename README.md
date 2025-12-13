# Wizard – Text-Based Card Game

## Group Members
- Ian Hashem  
- Ricardo Mejia  
- Daniel Osiyi  
- Sara Susa  
- Ryan Tran  

---

## About the Project
This is a text based version of the card game **Wizard**.  
The game runs in the terminal and allows players to:

- Get dealt cards  
- Predict how many tricks they expect to win  
- Play cards turn by turn  
- Follow suit and trump rules  
- Compete against computer players  
- Track scores across multiple rounds  


## How to Run the Game

 Run: 
 
- On Windows: python Wizard_Game_Completed.py
     
- On Mac: python3 Wizard_Game_Completed.py
     
The program will then ask you to:
- Enter your name
- Predict tricks
- Choose cards to play each turn
- Follow the suit rules during the trick takings

## Game Rules 

- The Wizard deck contains 60 cards: 52 normal cards + 4 Wizards + 4 Jesters.
- Game is played over multiple rounds; players receive a number of cards equal to the round number.
  Trump determination:
 - Normal card --> that suit becomes trump
 - Jester --> no trump
 - Wizard --> dealer chooses trump
 - Final round --> no trump
- Wizards always win a trick.
- Jesters always lose unless all cards are Jesters.
- You must follow suit if able.
  Scoring:
 - Exact prediction --> 20 + 10 × tricks won
 - Missed prediction --> –10 × difference

## The purpose of each file in the Repository 
- ComputerPlayer_Humanplayer_Class.py contains the Player class that is usedd for both human and computer players. In this section of the code, it includes methods for adding cards, choosing a card to play, printing the cards description and interacting with the games rules.
- Computer_Player.py contains the computer_choose_card() function and in this it determines how the computer selects the cards. It implements a strategy based on different attributes of the game like trump, lead suit, Wizards, and Jesters.
- Determining_Trick_Winners.py it contains determine_trick_winner() and carries the logic for assighning card strength and determines the winner of each truck.
- TrumpSuitSelection.py has two functions, determine_trump() being the first one which decides the trump suit for each round, the next function announce_trump_to_players() prints out the trump information to all the players and includes logic for a dealer choice when a wizard is flipped.
- Score_Predictions.py contains a calculate_score() and score_predictions(), which computes the score using predicted vs actual tricks and set operations to report correct predictors.
- MoveChecking.py is the original move checking logic that enforces the basic Wizard rules. It handles rules such as following a suit when possible as well as handling Wizards and Jesters during a trick.
- MoveCheckingUpdate.py is the updated version of the original movechecking.py. This version of it is the correct logic with refinements and particular handling.
- Wizard_Game_Completed.py is the final version of the code and is ready to play!

## Algorithm Components 
1. Trick Winner - Evaluates all the played cards where it assigns strength values and then selects a trick winner.
2. Scoring - Compares predicted and actual tricks to update all scores from each round.
3. Computer Player - Cards are choosen using the codes logic and the rules for which cards have priority.
4. Move Checking - Ensures legal moves: follows suit if possible, and handles Wizards/Jesters correctly.
5. Trump Selection - Determines trump each round which is based on flipped cards and the rules given for it.

## Attribution Table

| Method / Function | Primary Author | Techniques Demonstrated |
|-------------------|---------------|--------------------------|
| `human_choose_card` | Sara Susa | Composition (Player + Card interaction) |
| `computer_choose_card` | Sara Susa | List comprehension |
| `determine_trick_winner` | Daniel Osiyi | Conditional expressions |
| `card_strength` | Daniel Osiyi | Key function with max() |
| `calculate_score` | Ricardo Mejia | Optional parameters |
| `score_predictions` | Ricardo Mejia | Set operations (set difference) |
| `determine_trump` | Ian Hashem | Sequence unpacking |
| `announce_trump_to_players` | Ian Hashem | f-strings containing expressions |
| `CardChecker.__contains__` | Ryan Tran | Magic method ( __ contains __ ), generator expression |

# Annotated Bibliography 
1. Wizard Card Game Offical Rules - U.S. Games Systems, Inc.(n.d.). Wizard FAQ https://www.usgamesinc.com/Wizard-FAQ.html
   - We were all familar with the card game wizard prior to begining to code the game, but we actually had to sit down hop on a call and learn this all together. We used the rules as background information to understand the game, including trump determination, the mechanics of trick taking, and the role of Wizards and Jesters and how scoring works with those. It provided us with great knowledge of the game and how we wanted to implement the logic into our code.
2. Internet Searches
   - There was points when it came to implementing a technique that did stub us, espeically when we would try and implement something and python went from happy to angry in seconds. Just doing these quick searches helped us reinforce these concepts and how to implement it. We had several trial and errors with our game.
