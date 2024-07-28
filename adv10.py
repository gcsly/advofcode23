with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

for i in range(len(lista)):
    if 'S' in lista[i]:
        x = i
        for j in range(len(lista[i])):
            if lista[i][j] == 'S':
                y = j

visited = []
for i in range(len(lista)):
    row=[]
    for j in range(len(lista[i])):
        row.append(-1) 
    visited.append(row)         
#print(visited[0])

visited[x][y] = 0

def getFirstPoint(lista, x,y, visited):
    a = []
    if lista[x-1][y] in '|7F' and visited[x-1][y] == -1:
        a.append([x-1, y])
        visited[x-1][y] = 1
    if lista[x+1][y] in '|JL' and visited[x+1][y] == -1:
        a.append([x+1, y])
        visited[x+1][y] = 1
    if lista[x][y-1] in '-FL' and visited[x][y-1] == -1:
        a.append([x, y-1])
        visited[x][y-1] = 1
    if lista[x][y+1] in '-J7' and visited[x][y+1] == -1:
        a.append([x, y+1])
        visited[x][y+1] = 1
    
    return a

def getPoints(lista, x,y, visited, step):
    a = []
    
    if lista[x][y] == '|':
        if visited[x-1][y] == -1:
            a = [x-1, y]
            visited[x-1][y] = step
        elif visited[x+1][y] == -1:
            a = [x+1, y]
            visited[x+1][y] = step
    
    elif lista[x][y] == '-':
        if visited[x][y-1] == -1:
            a = [x, y-1]
            visited[x][y-1] = step
        elif visited[x][y+1] == -1:
            a = [x, y+1]
            visited[x][y+1] = step
    
    elif lista[x][y] == 'L':
        if visited[x-1][y] == -1:
            a = [x-1, y]
            visited[x-1][y] = step
        elif visited[x][y+1] == -1:
            a = [x, y+1]
            visited[x][y+1] = step
    
    elif lista[x][y] == 'J':
        if visited[x-1][y] == -1:
            a = [x-1, y]
            visited[x-1][y] = step
        elif visited[x][y-1] == -1:
            a = [x, y-1]
            visited[x][y-1] = step
    
    elif lista[x][y] == '7':
        if visited[x+1][y] == -1:
            a = [x+1, y]
            visited[x+1][y] = step
        elif visited[x][y-1] == -1:
            a = [x, y-1]
            visited[x][y-1] = step
    
    elif lista[x][y] == 'F':
        if visited[x+1][y] == -1:
            a = [x+1, y]
            visited[x+1][y] = step
        elif visited[x][y+1] == -1:
            a = [x, y+1]
            visited[x][y+1] = step
    return a

def printVisited(visited):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            print(visited[i][j],end='')
        print()

def part1(lista, visited, x, y):
    step = 1
    firststeps = getFirstPoint(lista, x,y, visited)
    print(firststeps)
    while True:
        step += 1

        for i in range(len(firststeps)):
            firststeps[i] = getPoints(lista, firststeps[i][0], firststeps[i][1], visited, step)

        #print(firststeps)
        #print(step)
        #printVisited(visited)

        if len(firststeps[1]) == 0:
            #printVisited(visited)
            print(step)
            break
        
part1(lista, visited, x, y)
