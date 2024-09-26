# Subtrees_and_Ballot_Property

Supplements "On Chip Firing on Undirected Trees" by Ryota Inagaki, Tanya Khovanova, and Austin Luo.


LiscioResult.txt is the list of all possible final chip configurations when there are 2^{4}-1 labeled chips $1, 2, \dots, 2^{4}-2, 2^{4}-1$ starting at the root of the undirected infinite binary tree. This file is the same as the one at Liscio's Result.txt (can be found at https://drive.google.com/file/d/1b_QkfDahUJuDoF7YhMf_oCU6qNcSY_Sj/view and is referenced in Musiker \& Nguyen's paper), but with only the contents after "FULL RESULT: (Format: [Tree], [#Inversions]". The file still contains all configurations listed in Liscio's Result.txt. Please see https://drive.google.com/file/d/1b_QkfDahUJuDoF7YhMf_oCU6qNcSY_Sj/view for a detailed description on how to read each list in the file as a configuration.

TestingBallotProperty.py verifies that each of the chip configurations listed by Patrick Liscio's data satisfies the ballot property, i.e. the ith smallest chip in the left subtree is less than the ith smallest chip in the right subtree.

CheckRelativeOrderings.py finds all relative orderings of chips in the subtrees of 7 chips that show up in Liscio's stable configurations. Please see the Python file for how to read the output.

To run thesee scripts, open your terminal, make your point working directory this repository, and then type ```Python [insert-filename]``` and hit enter.


