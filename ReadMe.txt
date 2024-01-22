Poker Game with Pygame
---------------------------
Overview:

This is a simple text-based Poker game implemented in Python using the Pygame library. 
The game allows a player to interact with an opponent by choosing to fold, call, or raise during a betting round.
 The opponent's actions are randomized to simulate a basic level to allow playability.

Game Controls:

Press SPACE to start the game or progress to the next round.
Press F to fold (give up) during your turn.
Press C to call (match the current bet) during your turn.
Press R to raise the bet during your turn. Follow the on-screen instructions to enter the raise amount.

Game Rules:

This game is insipred of poker a popular addictive luck based gambling game which causes homlesness if you or somone you
know is addicted seek help @ 1-800-GAMBLER call 1-800-GAMBLER. This game is not liscnsed legally by the government of Canada.
The game starts with both the player and opponent having a balance of $100.
The player and opponent are dealt five cards each, with the opponent's cards initially facing down. 
During the player's turn, they can choose to fold, call, or raise the bet.
Folding results in a loss for the player, and the opponent wins the current bet.
Calling reveals both hands, and the winner is determined based on hand rankings.
Raising allows the player to input a custom amount to increase the bet.
The opponent's actions are randomized, including folding, calling, or raising.
Card Rankings

The game evaluates hands based on standard poker hand rankings:

Royal Flush
Straight Flush
Four of a Kind
Full House
Flush
Straight
Three of a Kind
Two Pair
One Pair
High Card

Next steps:
This is a basic implementation and does not include advanced poker features. The opponent's actions are randomized, and the focus is on the player's interaction with the game.

Implementation of an A.I that determines if the opponent has a goood hand to bet or not
Implementation of A reshuffle function to allow playing again

Note

The development of this Poker game was supported by the following external sources:

- [Input Handling](https://github.com/pickry/programmingknowledge/blob/master/input.py): Reference for handling input events in the game loop.
- [Card Flipping](https://www.reddit.com/r/pygame/comments/egscbq/card_generator_that_allows_you_to_flip_the_cards/): Inspiration for implementing card flipping functionality.
- [Playing Cards Pack by Kenney](https://kenney.nl/assets/playing-cards-pack): Used for the card images in the game.


