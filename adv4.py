with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

def part1(lista):
    worth = 0

    for i in range(len(lista)):
        total = 0
        card = lista[i].split(': ') # see card[1]
        a = card[1].split(' | ') # a[0] winning numbers, a[1] numbers you have
        winnum = a[0].split()
        #print(winnum, a[1])
        for j in range(len(winnum)):
            if winnum[j] in a[1].split():
                if total == 0:
                    total += 1
                else:
                    total = 2*total
        print(total)
        worth += total

    print(worth)

def part2(lista):
    suma = 0
    instances = []
    for i in range(len(lista)):
        instances.append(1)
    #print(instances)

    for i in range(len(lista)):
        total = 0
        card = lista[i].split(': ') # see card[1]
        a = card[1].split(' | ') # a[0] winning numbers, a[1] numbers you have
        winnum = a[0].split()
        #print(winnum, a[1])
        for j in range(len(winnum)):
            if winnum[j] in a[1].split():
                total += 1 # number of matching numbers
        
        for j in range(i+1, total+i+1):
            instances[j] += instances[i]
        
        
    for j in range(len(instances)):
        suma += instances[j]
        #print(suma)
        #print(i, total, instances,len(instances))

    return suma
        #

print(part2(lista))
