# Quantum Master Mind

#### America University of Armenia
#### College of Science and Engineering
#### CS339 Quantum Computing - Final Project
#### Instructor: Dr. Suren Khachatryan (skhachat@aua.am)

---

## Project Description
This project is a quantum version of the classic game Master Mind played by two players. Given _n_ different colors, the first player – the keeper, secretly forms a sequence of _n_ colored pins, where several pins may share the same color, or all of them may be of different colors. The task of the second player – the guesser, to disclose the hidden sequence with minimal guesses.

This project works with the following version (__version 2__): each guess is graded by the keeper with a single digit – the number of correct
pins in their correct positions. The game stops when the grade of the most recent guess is
_n_.

## Progress Steps
1. Estimate the complexity of the move search in different stages of the game.
2. Suggest a system of qubits that describes the game, and define the game states and state
vectors.
3. Design quantum gates that implement the operations of the sequential classical algorithm.
4. Apply the designed gates to superposition states aiming at parallelization of the move
search.