# Assignment 1 - Codility Lessons
# Five selected problems: CyclicRotation, OddOccurrencesInArray, FrogJmp,
# PermMissingElem, TapeEquilibrium.
# On Codility, paste ONE function per problem (each must be named `solution`).
# Here they are given distinct names so they can live in one file.
#
# Citation: Solutions assisted by Claude (Anthropic), October 30th 2026, https://claude.ai/share/d252a8f0-20a8-4863-aee9-aee525230663


# ---------------------------------------------------------------
# 5.Tape Equilibrium
# Looks for the best splitting point 
# ---------------------------------------------------------------
def tape_equilibrium(A):
    best = None
    #Splitting point P from 1 to N-1
    for p in range(1,len(A)):
        left = sum(A[:p]) #Sum of left
        right = sum(A[p:]) #Sum of right
        difference = abs(right-left)
        #To only keep the "best" if its less than or the first iteration
        if best is None or difference < best:
            best = difference
    return best
