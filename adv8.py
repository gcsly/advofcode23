from math import lcm
with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

direcetion = lista[0]
di = ''
for i in range(len(direcetion)):
    if direcetion[i] == 'L':
        di += '1'
    else:
        di += '2' # index

print(di)

mps = {}
for i in range(2, len(lista)):
    a = ''
    pr = 0
    for j in range(len(lista[i])):
        if lista[i][j].isalnum():
            if pr == 3:
                a += ' '
                pr = 0
            a += lista[i][j]
            
            pr += 1 
    b = a.split()
    mps[b[0]] = b[1], b[2]

#print(mps['AAA'][0])




def part1(direcetion, mps):
    cou = 0
    curr = 'AAA'
    c = True
    while c:
        for i in range(len(direcetion)):
            if direcetion[i] == 'L':
                curr = mps[curr][0]
            else:
                curr = mps[curr][1]
            cou += 1
            #print(curr)
            if curr == 'ZZZ':
                print(cou)
                c = False

def part2(direcetion, mps):
    star = []
    for i in mps.keys():
        
        if i[2] == 'A':
            star.append(i)
    print(star)
    cou = 0
    c = True
    while c:
        for i in range(len(direcetion)):
            p = 0 # if end in z change to 1 uh 
            for j in range(len(star)):
                if direcetion[i] == 'L':
                    star[j] = mps[star[j]][0]
                else:
                    star[j] = mps[star[j]][1]
                aq = star[j]
                #print(aq)
                if aq[2] == 'Z':
                    p += 1
            print(cou, star)
            cou += 1
            if p == len(star):
                print(cou)
                c = False
            

        
def part3(direcetion, mps):
    star = []
    aa = []
    
    for i in mps.keys():
        if i[2] == 'A':
            star.append(i)
    print(star)
    for i in range(len(star)):
        aa.append(0)
    
    for j in range(len(star)):
        cou = 0
        c = True
        while c:
            for i in range(len(direcetion)):
                cou += 1
                if direcetion[i] == 'L':
                    star[j] = mps[star[j]][0]
                else:
                    star[j] = mps[star[j]][1]
                aq = star[j]
                #print(aq)
                #print(aq)
                if aq[2] == 'Z':
                    aa[j] += cou
                    c = False
                    break
    print(aa)
        
    p = aa[0]
    for i in range(1, len(aa)):
        p = lcm(p, aa[i])
        
        print(i, p)

part3(direcetion, mps)             
