""" Check All Relative Orderings that exist in subtrees of final configurations of 4 with 7 chips
# Relative orderings are written as tuples of 7 terms
# In each tuple:
- First term stands for rank of the chip on the leftmost vertex in the 3rd layer of the subtree
- Second term stands for rank of the chip on the leftmost vertex in the 2rd layer of the subtree
- Third term stands for rank of the chip on the second leftmost vertex in the 3rd layer of the subtree
- Fourth term stands for rank of the chip on the vertex at the first layer of the subtree, i.e. on the root of the subtree
- Fifth term stands for rank of the chip on the third leftmost vertex in the 3rd layer of the subtree
- Sixth term stands for rank of the chip on the second leftmost vertex in the 2nd lyaer of the subtree
- Seventh term stands for rank of the chip on the rightmost vertex in the 3rd layer of the subtree.

For instance relative ordering (1, 2, 3, 4, 5, 6, 7) stands for


              4
      2               6
  1       3      5         7
In the subtree.
"""
import ast, time
file1 = open('LiscioResult.txt', 'r')
Lines = file1.readlines()
# Finds Relative Orders of subtrees of Length 3 in Liscio's Data Set
# Relative Orders are read in the smallest to largest 
for line in Lines:
    count += 1
    textedlist = line.strip().split("], ")[0] +"]"
    li = ast.literal_eval(textedlist)
    # Chips that are in the tree of the left child of the root.
    left= li[:len(li)//2]
    # Chips that are in the tree of the right child of the root. 
    right = li[len(li)//2+1:]
    leftsorted = sorted(left)
    relativeOrder = []
    for i in left:
        relativeOrder.append(leftsorted.index(i)+1)
    set_of_orderings.add(tuple(relativeOrder))
    rightsorted = sorted(right)
    relativeOrder = []
    for i in right:
        relativeOrder.append(rightsorted.index(i)+1)
    set_of_orderings.add(tuple(relativeOrder))
    
end =  time.time()
print(set_of_orderings)