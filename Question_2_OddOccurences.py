# Assignment 1 - Codility Lessons
# Five selected problems: CyclicRotation, OddOccurrencesInArray, FrogJmp,
# PermMissingElem, TapeEquilibrium.
# On Codility, paste ONE function per problem (each must be named `solution`).
# Here they are given distinct names so they can live in one file.
#

# ---------------------------------------------------------------
# 2. OddOccurences
# Looks for the number that only appears once/unpaired
# ---------------------------------------------------------------

def Odd_Occurences(A):
    #Counts how man times each number appears
    counts = {}
    for value in A:
        if value in counts:
            counts[value]+=1
        else:
            counts[value] = 1
    #The unpaired number appears an odd number of times
    for value in counts:
        if counts[value]%2 == 1:
            return value
    pass
