# Subtrees_and_Ballot_Property

Supplements "On Chip Firing on Undirected Trees"

We verify that each of the chip configurations listed by Patrick Liscio's data satisfies the ballot property, i.e. the ith smallest chip in the left subtree is less than the ith smallest chip in the right subtree.

LiscioResult.txt is the list of all possible final chip configurations when there are 2^{\ell}-1 labeled chips $1, 2, \dots, 2^{\ell}-2, 2^{\ell}-1$ starting at the root of the undirected infinite binary tree. This file is the same as the one at https://drive.google.com/file/d/1b_QkfDahUJuDoF7YhMf_oCU6qNcSY_Sj/view, but with the preamble deleted. Please see https://drive.google.com/file/d/1b_QkfDahUJuDoF7YhMf_oCU6qNcSY_Sj/view for a detailed description on how to read each list in the file as a configuration.

How to run the code:
Open your terminal. Once your point working directory is this repository run ```Python TestingBallotProperty.py``` in the terminal.
