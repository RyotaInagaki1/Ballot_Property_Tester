import ast, time
# In this file we confirm that all chip configurations in LiscioResult.txt satisfy the Ballot Property, which was defined in Sec.3.3 of our paper.
file1 = open('LiscioResult.txt', 'r')
Lines = file1.readlines()
begin = time.time()
count = 0
satisfy = True
for line in Lines:
    count += 1
    textedlist = line.strip().split("], ")[0] +"]"
    li = ast.literal_eval(textedlist)
    left= li[:len(li)//2] # List of chips that are in the tree of the left child of the root. 
    right = li[len(li)//2+1:]  # List of Chips that are in the tree of the right child of the root.
    # Does the tree at large satisfy the Ballot Property?
    not_at_root = left + right # list of chips that are not at the root.
    not_at_root = sorted(not_at_root) # Chips in notatroot written in increasing numerical order
    leftcount = 0 # Variable for number of chips that are less than i in  and at the tree rooted at the LEFT child
    rightcount = 0 # Variable for number of chips that are less than i and at the tree rooted at the RIGHT child
    for i in not_at_root:
        if i in left:
            leftcount += 1
        elif i in right:
            rightcount += 1
        if rightcount > leftcount:
            print("Tree Doesn't exhibit the Ballot Property.")
            satisfy = False
            break
end =  time.time()

if satisfy:
    print("The final configuration of chips in the tree satisfies the ballot property.")
print("It took ", end-begin, "seconds.")