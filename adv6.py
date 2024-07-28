with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 
s = lista[0].split(':')
times = s[1].split() # string

#print(times)
a = lista[1].split(':')
distances = a[1].split() # string

ti = []
for i in times:
    b = int(i)
    ti.append(b)

di = []
for i in distances:
    b = int(i)
    di.append(b)
#print(ti, di)

for i in range(len(di)):
    s = ti[i]//2
    maxi = s*(ti[i]-s)
    #rint(maxi)

def part1(ti, di):
    a = 1
    for i in range(len(di)):
        pp = 0
        for j in range(ti[i]+1):
            distan = (ti[i]-j)*(j)
            if distan > di[i]:
                pp += 1
            #print(distan)
        print(pp)
        a = a*pp
    print(a)
        #break

def part2(ti, di):
    time = ''
    distance = ''
    for i in range(len(ti)):
        time += ti[i]
        distance += di[i]
    
    #a = 1
    
    pp = 0
    for j in range(int(time)+1):
        distan = (int(time)-j)*(j)
        if distan > int(distance):
            pp += 1
        #print(distan)
    print(pp)
        
    #print(time, distance)

part2(times, distances)