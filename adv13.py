with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

patterns = [[]]
c = 0
for i in range(len(lista)):
    if len(lista[i]) == 0:
        patterns.append([])
        c += 1
    else:
        patterns[c].append(lista[i])

def idhori(pattern):
    possible = []
    for i in range(1, len(pattern)):
        if pattern[i-1] == pattern[i]:
            possible.append(i) # line at i and i +1
    if len(possible) != 0:
        c = 1
        for i in possible:
            #print(i)
            pat = 0
            while True:
                
                if i-c-1 < 0 or i+c > len(pattern)-1:
                    break
                if pattern[i-c-1] != pattern[i+c]:
                    pat = 1
                #print(pattern[i-c-1], pattern[i+c])
                c += 1
            
            if pat == 0:
                return i
    return -1

def idvert(pattern):
    possible = []
    for i in range(len(pattern[0])-1):
        c = 0
        for j in range(len(pattern)):
            if pattern[j][i] != pattern[j][i+1]:
                c = 1
        if c == 0:
            possible.append(i+1)
    
    if len(possible) != 0:
        #print(possible)
        for i in possible:
            c = 1
            pat = 0
            #print(i)
            while True:
                #print(i-c-1, i+c, len(pattern[0])-1)
                if i-c-1 < 0 or i+c > len(pattern[0])-1:
                    break
                
                for j in range(len(pattern)):
                    #print(pattern[j][i-c-1], pattern[j][i+c])
                    if pattern[j][i-c-1] != pattern[j][i+c]:
                        pat = 1
                        break
                
                if pat == 1:
                    break
                c += 1
                #print('')

            if pat == 0:
                return i
        
    return -1

s = 0
for i in range(len(patterns)):
    print(i)
    if idvert(patterns[i]) > 0:
        s += idvert(patterns[i])
    if idhori(patterns[i]) > 0:
        s += idhori(patterns[i])*100

print(s)

#print(idvert(patterns[0]))