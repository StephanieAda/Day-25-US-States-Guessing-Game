# Day-25-US-States-Guessing-Game
Objective: To guess as many U.S states as you can, you'll receive a CSV file labeling all the states you missed so you can learn and try again

I made use of the turtle and Panda Modules to create this game.

I used the Turtle module to create the background

I made use of the Panda module to read a csv file containing all 50 US States and turned it to a list.

Asked for the user guess using the turtle screen prompt and converted it to title case to match the states in the list.

Checked if the user guess was within the "states" column of the states list.

If correct, added the user's guess to a new list called "guessed_states"

The game doesn't end until you correctly guess all 50 states or type 'exit'

After which it creates a new csv file cotaining all the states you missed.
