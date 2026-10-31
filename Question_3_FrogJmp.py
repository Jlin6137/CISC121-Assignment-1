def frog_jmp(X, Y, D):
    distance = Y - X
    # Number of full jumps that fit in the distance
    jumps = distance // D
    # If some distance is left over, one more jump is needed
    if distance % D != 0:
        jumps += 1
    return jumps
