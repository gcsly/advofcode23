with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 


s = 0

for i in range(len(lista)):
    c = True
    diffs = [lista[i].split()]
    j = 0
    diffs[j] = [int(i) for i in diffs[j]]
    #print(diffs[j])
    
    while c:
        a = []
        for k in range(1, len(diffs[j])):
            d = diffs[j][k] - diffs[j][k-1]
            a.append(d)
        
        p = 0
        diffs.append(a)
        
        for ip in a:
            if ip != 0:
                p = 1
                break
        if p == 0:
            break
        j += 1

    pppp = diffs[-1][0]
    #print(diffs)
    
    for m in range(len(diffs)-2, -1, -1):
        #print(m)
        pppp = diffs[m][0] - pppp
        #print(diffs[m][0])
    s += pppp

print(s)

def part1(diffs):
    pppp = diffs[0][-1]
    for m in range(len(diffs)-2, 0, -1):
        print(diffs[m])
        pppp += diffs[m][-1]
    s += pppp
    print(s)

