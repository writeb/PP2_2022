def Solve(heads, legs):
    chicken = 0
    rabbit = 0
    if (heads>=legs): return "no solution"
    elif (legs%2!=0): return "no solution"
    else:
        rabbit = (legs - 2*heads)/2
        chicken = heads - rabbit
        return int(chicken), int(rabbit)
problem1 = Solve(35, 94)
print(problem1)