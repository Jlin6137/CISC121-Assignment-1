# Assignment 1 - Codility Lessons
# Five selected problems: CyclicRotation, OddOccurrencesInArray, FrogJmp,
# PermMissingElem, TapeEquilibrium.
# On Codility, paste ONE function per problem (each must be named `solution`).
# Here they are given distinct names so they can live in one file.
#


# ---------------------------------------------------------------
# 3. FrogJmp
# Looks for the most optimal amount of jumps the frog can do to reach the end
# ---------------------------------------------------------------
def frog_jmp(X, Y, D):
    distance = Y - X
    # Number of full jumps that fit in the distance
    jumps = distance // D
    # If some distance is left over, one more jump is needed
    if distance % D != 0:
        jumps += 1
    return jumps
