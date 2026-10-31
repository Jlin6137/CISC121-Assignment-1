def solution(A):
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
