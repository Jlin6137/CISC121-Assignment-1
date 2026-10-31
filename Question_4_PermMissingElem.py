def solution(A):
    #Puts the elements into a set so it can check them quickly
    seen = set(A)
    #Checks every number from 1 to N+1;return the one not in the set
    for number in range (1,len(A) +2):
        if number not in seen:
            return number
