# Assignment 1 - Codility Lessons
# Five selected problems: CyclicRotation, OddOccurrencesInArray, FrogJmp,
# PermMissingElem, TapeEquilibrium.
# On Codility, paste ONE function per problem (each must be named `solution`).
# Here they are given distinct names so they can live in one file.
#
# Citation: Solutions assisted by Claude (Anthropic), October 30th 2026, https://claude.ai/share/d252a8f0-20a8-4863-aee9-aee525230663
# AI assistance: Claude (Anthropic), Oct 30 2026 – hints and debugging

# ---------------------------------------------------------------
# 4. PermMissingElem
# Looks for the element that is missing
# ---------------------------------------------------------------
def Perm_missing_elem(A):
    #Puts the elements into a set so it can check them quickly
    seen = set(A)
    #Checks every number from 1 to N+1;return the one not in the set
    for number in range (1,len(A) +2):
        if number not in seen:
            return number
