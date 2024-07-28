with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

s = lista[0].split(':')
seeds = s[1].split()

'''for i in range(0, len(seeds), 2):
    for j in range(int(seeds[i+1])):
        realseeds.append(int(seeds[i])+j)
    #print(realseeds)'''
    

mapss = []
for i in range(7):
    mapss.append([])

"""
0 seedtosoil 1 soiltofertilizer 2 fertilizertowater 3 watertolight 4 lighttotemp 5 temptohumidity 6 humiditytolocation 
"""

cou = 0
for i in range(3, len(lista)):
    if len(lista[i]) == 0:
        cou += 1
    else:
        if lista[i][0].isnumeric():
            mapss[cou].append(lista[i].split())

maps = []
for i in range(len(mapss)):
    maps.append([])
    for j in range(len(mapss[i])):
        maps[i].append([])
        for k in range(len(mapss[i][j])):
            a = int(mapss[i][j][k])
            maps[i][j].append(a)

#print(maps)
#print(seeds)
prev = 9**99         

def maoo(ranges, maps, f):
    
    if f == 0:
        r = [ranges[0], ranges[0]+ranges[1]-1]
    else:
        r = [ranges[0], ranges[1]]

    ##print("maoo-r: " + str(r))
    mappable = []
    ##print(maps)
    for i in range(len(maps)):
        
        ed = maps[i][0] - maps[i][1]

        if r[0] < maps[i][1] and r[1] < maps[i][1]+maps[i][2]-1 and r[1] >= maps[i][1]:
            mappable.append([maps[i][1]+ed, r[1]+ed])
            mappable.append([r[0], maps[i][1]-1])
        elif r[0] >= maps[i][1] and r[1] <= maps[i][1]+maps[i][2]-1:
            mappable.append([r[0]+ed, r[1]+ed])
        elif r[0] >= maps[i][1] and r[0] <= maps[i][1]+maps[i][2]-1 and r[1] > maps[i][1]+maps[i][2]-1:
            mappable.append([r[0]+ed, maps[i][1]+maps[i][2]-1+ed])
            mappable.append([maps[i][1]+maps[i][2], r[1]])
        elif r[0] < maps[i][1] and r[1] > maps[i][1]+maps[i][2]-1:
            mappable.append([maps[i][1]+ed, maps[i][1]+maps[i][2]-1+ed])
            mappable.append([r[0], maps[i][1]-1])
            mappable.append([maps[i][1]+maps[i][2], r[1]])
        ##print("maco-mappable:", i)
        ##print(mappable)
    

        
    return mappable

f = 0
smallest = 99*99
for i in range(0, len(seeds), 2):

    output1 = maoo([int(seeds[i]), int(seeds[i+1])], maps[0], f)
    f = 1

    ##print("output1:")
    ##print(output1)
    mapinput = output1
    for k in range(1, len(maps)):
        aa = 0
        output2 = []
        for j in range(len(mapinput)):
            
            pp = maoo([mapinput[j][0], mapinput[j][1]], maps[k], f)
            if len(pp) != 0:
                output2.extend(pp)
                aa = 1
                ##print(i,j,k,mapinput[j], maps[k], output2,pp)

        if len(output2) != 0:
            mapinput = output2
        #print("mapinput at end " , i, k)
        #print(mapinput)
        # when does not go into any of the maps, keep same range.s
    
    for j in range(len(mapinput)):
        if mapinput[j][0] < smallest:
            smallest = mapinput[j][0]
    print(i,str(smallest))
    f =0

print(smallest)
'''
for i in range(len(seeds)):
    location = int(seeds[i])
    for j in range(len(maps)):
        for k in range(len(maps[j])):
            if location >= int(maps[j][k][1]) and location <= int(maps[j][k][1]) + int(maps[j][k][2]) -1:
                ed = location - int(maps[j][k][1])
                location = int(maps[j][k][0]) + ed
                break
                
    if location < prev:
        prev = location

print(prev)'''

            
    
    
    