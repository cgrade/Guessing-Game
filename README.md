# Guessing-Game
This is a solution to a problem/challeng..(Guessing a Number until you get it correct)

## The Question/Challenge
In a file called game.py, implement a program that:

* Prompts the user for a level `n`  if the user does not input a positive `integer`  the program should prompt again.

* Randomly generates an integer between 1 and `n` , inclusive, using the `random` module.

* Prompts the user to guess that `integer` . If the guess is not positive `integer` the program should prompt the user again.

  * If the guess is smaller than the `integer` , the program should output `Too small!` and prompt the user again.
  * If the Guess is larger than that `integer` , the program should output ` Too Large!` and prompt the user again.
  * If the guess is the same as that `integer` , the program should output `Just Right!` and exit.
