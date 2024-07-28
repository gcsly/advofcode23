import math
with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

def part1(lista):
    a = []
    for i in range(len(lista)):
        if '#' not in lista[i]:
            print("new line " + str(i))
            a.append(lista[i])
        a.append(lista[i])

    b = []
    for i in range(len(a)):
        b.append('')

    for i in range(len(a[0])):
        f = 0
        for j in range(len(a)):
            if a[j][i] == '#':
                f = 1
                break
        if f == 0:
            for j in range(len(b)):
                b[j] += '.'
            print("new column " + str(i))
        
        for j in range(len(a)):
            b[j] += a[j][i]
    #print(b)

    c = []
    nu = 1
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == '#':
                c.append([nu, i, j])
                nu += 1
            
    #print(c)
    #ncr = math.comb(nu, 2)
    #for i in range(ncr):
    tot = 0
    aa = 0
    for i in range(1, nu):
        for j in range(i+1, nu):
            # combo is i and j

            xi = c[i-1][1]
            yi = c[i-1][2]

            xj = c[j-1][1]
            yj = c[j-1][2]
            
            tot += abs(xi - xj) + abs(yi - yj)
            #print(i, j, abs(xi - xj) + abs(yi - yj))
            aa += 1
    print(tot, aa)

def part2(lista):
    a = [] # empty row indexs
    for i in range(len(lista)):
        if '#' not in lista[i]:
            a.append(i)
    print(a)
    b = [] # empty column indexes

    for i in range(len(lista[0])):
        f = 0
        for j in range(len(lista[0])):
            if lista[j][i] == '#':
                f = 1
                break
        if f == 0:
            b.append(i)
    print(b)

    c = []
    nu = 1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == '#':
                c.append([nu, i, j])
                nu += 1
    print(c)

    tot = 0
    aa = 0
    gap = 1000000-1
    for i in range(1, nu):
        for j in range(i+1, nu):
            # combo is i and j

            xi = c[i-1][1]
            yi = c[i-1][2]

            xj = c[j-1][1]
            yj = c[j-1][2]
            #print(xi, yi, xj, yj)
            crossd = 0
            for k in range(len(a)):
                if a[k] > xi and a[k] < xj:
                    tot += gap
                    crossd += 1
                if a[k] < xi and a[k] > xj:
                    tot += gap
                    crossd += 1

            for k in range(len(b)):
                if b[k] > yi and b[k] < yj: #AND OTEHR WAY AROUND
                    tot += gap
                    crossd += 1
                if b[k] < yi and b[k] > yj: #AND OTEHR WAY AROUND
                    tot += gap
                    crossd += 1
            tot += abs(xi - xj) + abs(yi - yj)
    print(tot)
            

part2(lista)