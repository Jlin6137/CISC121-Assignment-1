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
