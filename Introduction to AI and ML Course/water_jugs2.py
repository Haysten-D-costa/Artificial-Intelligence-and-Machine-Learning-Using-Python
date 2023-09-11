#2 Water jug problem
jugA = int(input("Enter the maximum capacity of jug A : "))
jugB = int(input("Enter the maximum capacity of jug B : "))
goal = int(input("Enter the goal state in jug B : "))

def pour(jug1, jug2):
    print(jug1, "\t", jug2)
    if jug2 is goal:
        return True        
    elif jug2 is jugB:
        pour(0, jug1)
    elif jug1 != 0 and jug2 == 0:
        pour(0, jug1)
    elif jug1 < jugA:
        pour(jugA, jug2)
    elif jug1 < (jugB - jug2):
        pour(0, (jug1 + jug2))
    else:
        pour(jug1 - (jugB - jug2), (jugB - jug2) + jug2)
    return
print("JUG1\tJUG2")
pour(0, 0)