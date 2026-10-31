# Assignment 1 - Codility Lessons
# Five selected problems: CyclicRotation, OddOccurrencesInArray, FrogJmp,
# PermMissingElem, TapeEquilibrium.
# On Codility, paste ONE function per problem (each must be named `solution`).
# Here they are given distinct names so they can live in one file.
#
# Citation: Solutions assisted by Claude (Anthropic), October 31st 2026, [chat link].


# ---------------------------------------------------------------
# 1. CyclicRotation
# Rotate array A to the right K times.
# ---------------------------------------------------------------
def cyclic_rotation(A, K):
    # Nothing to rotate in an empty array
    if len(A) == 0:
        return A
    # Do one rotation at a time, K times
    for i in range(K):
        last = A.pop()        # take the last item off the end
        A.insert(0, last)     # put it at the front
    return A
