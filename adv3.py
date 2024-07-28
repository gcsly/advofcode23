##file=open("./club/advent of code/input.txt")
##lista=file.readlines()
##file.close()

with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

def surroundings(inputa, i, j):
    
    if i == 0:# top border
        if j == 0:
            for a in range(i, i+2):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()): # if surrounding A B is symbol
                            if not (inputa[a][b] == '.'): # if Nawt period
                                return True
        elif j == len(inputa[i])-1:
            for a in range(i, i+2):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True
        else:
            for a in range(i, i+2):
                for b in range(j-1, j+2):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True
    
    elif i == len(inputa)-1: # bottom border
        if j == 0:
            for a in range(i-1, i+1):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True
        elif j == len(inputa[i])-1:
            for a in range(i-1, i+1):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True 
        else:
            for a in range(i-1, i+1):
                for b in range(j-1, j+2):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True

    if j == 0:
        if i != 0 and i != len(inputa)-1:
            for a in range(i-1, i+2):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if not (inputa[a][b].isnumeric()):
                            if not (inputa[a][b] == '.'):
                                return True
    
    elif j == len(inputa[i])-1:
        if i != 0 and i != len(inputa)-1:
            for a in range(i-1, i+2):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                            if not (inputa[a][b].isnumeric()):
                                if not (inputa[a][b] == '.'):
                                    return True

    if i > 0 and i < len(inputa)-1 and j > 0 and j < len(inputa[i])-1: # centre
        for a in range(i-1, i+2):
            for b in range(j-1, j+2):
                if not (a == i and b == j):
                    if not (inputa[a][b].isnumeric()):
                        if not (inputa[a][b] == '.'):
                            return True
    return False


def part1(inputa):
    suma = 0
    
    for i in range(len(inputa)):
        numa = ''
        fla = 0
        for j in range(len(inputa[i])):
            if inputa[i][j].isnumeric():
                # check surroundings
                if surroundings(inputa, i, j):
                    fla = 1

                numa += inputa[i][j]

            else: 
                if fla == 1:
                    suma += int(numa)
                numa = ''
                fla = 0

            if j == len(inputa[i])-1:
                if fla == 1:
                    suma += int(numa)
                numa = ''
                fla = 0 

    return suma
            

#print(part1(lista))

def surround(inputa, i, j): # to Find Number, should Return TWO Sets of Um. indexes
    p = []
    if i == 0:# top border
        if j == 0:
            for a in range(i, i+2):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is symbol
                                p.append([a, b])
        elif j == len(inputa[i])-1:
            for a in range(i, i+2):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is symbol
                                p.append([a, b])
        else:
            for a in range(i, i+2):
                for b in range(j-1, j+2):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])
    
    elif i == len(inputa)-1: # bottom border
        if j == 0:
            for a in range(i-1, i+1):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])
        elif j == len(inputa[i])-1:
            for a in range(i-1, i+1):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])
        else:
            for a in range(i-1, i+1):
                for b in range(j-1, j+2):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])

    if j == 0:
        if i != 0 and i != len(inputa)-1:
            for a in range(i-1, i+2):
                for b in range(j, j+2):
                    if not (a == i and b == j):
                        if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])
    
    elif j == len(inputa[i])-1:
        if i != 0 and i != len(inputa)-1:
            for a in range(i-1, i+2):
                for b in range(j-1, j+1):
                    if not (a == i and b == j):
                            if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])

    if i > 0 and i < len(inputa)-1 and j > 0 and j < len(inputa[i])-1: # centre
        for a in range(i-1, i+2):
            for b in range(j-1, j+2):
                if not (a == i and b == j):
                    if (inputa[a][b].isnumeric()): # if surrounding A B is NUMBEr
                                p.append([a, b])

    return p

def wholenumber(inputa, i, j):
    numa = inputa[i][j]
    if inputa[i][j+1].isnumeric():
        numa += inputa[i][j+1]
        if inputa[i][j+2].isnumeric():
            numa += inputa[i][j+2]
    if inputa[i][j-1].isnumeric():
        numa = inputa[i][j-1] + numa
        if inputa[i][j-2].isnumeric():
            numa = inputa[i][j-2] + numa

    return int(numa)

def part2(inputa):
    gearratio = 0
    for i in range(len(inputa)):
        for j in range(len(inputa)):
            if not inputa[i][j].isalnum():
                if inputa[i][j] != '.':
                    # checm surroundings
                    indexs = surround(inputa, i, j)
                    
                    previ = -1
                    prevj = -2
                    print(indexs)
                    adja = 0

                    sa = []
                    for k in range(len(indexs)):
                        if indexs[k][0] == previ: # if same row
                            if indexs[k][1] != prevj + 1: # assume moving forward
                                po = wholenumber(inputa, indexs[k][0], indexs[k][1])
                                sa.append(po)
                                adja += 1
                            #elif indexs[k][1] == prevj + 2:
                                #continue
                                
                        else: 
                            po = wholenumber(inputa, indexs[k][0], indexs[k][1])
                            sa.append(po)
                            adja += 1
                        previ = indexs[k][0]
                        prevj = indexs[k][1]
                        
                        #print(previ, prevj)
                        print(i,j,k, adja, sa)
                        if adja == 2:
                            gearratio += sa[0]*sa[1]
                            break


    return gearratio


print(part2(lista))
