import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)

#Python provides a module named copy that provides both the copy()
#and deepcopy() functions. The first of these, copy.copy(), can be
#used to make a duplicate copy of a mutable value like a list or
#dictionary, not just a copy of a reference
