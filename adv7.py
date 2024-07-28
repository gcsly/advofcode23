with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

def retnum(ke):
    if ke == 'T':
        kn = 10
    elif ke == 'Q':
        kn = 12
    elif ke == 'K':
        kn = 13
    elif ke == 'A':
        kn = 14
    elif ke == 'J':
        kn = 1
    else:
        kn = int(ke)
    return kn

def gettypewj(cards):
    d = {}    

    for cha in cards: # count nmber of instances of each digit
        if cha in d:
            d[cha] += 1
        else:
            d[cha] = 1
    greates = 0
    
    if 'J' in d:
        if d['J'] == 5 or d['J'] == 4:
            return 6
        
        # c = card w greates freq
        for it in d:
            if it == 'J':
                continue
            elif d[it] > greates:
                greates = d[it]
                c = it
        
        if d['J'] == 3:
            if greates == 2:
                return 6
            elif greates == 1:
                return 5
        elif d['J'] == 2:
            if greates == 3:
                return 6
            elif greates == 2:
                return 5
            else:
                return 3
        else:
            if greates == 4:
                return 6
            elif greates == 3:
                return 5
            elif greates == 2:
                if len(d) == 4:
                    return 3
                else:
                    return 4
            else:
                return 1
    else:
        return gettype(cards)
    
def gettype(cards):
            
    d = {}    

    for cha in cards: # count nmber of instances of each digit
        if cha in d:
            d[cha] += 1
        else:
            d[cha] = 1
    
    if len(d) == 1: # identify type byy lengtth of dictinary
        type = '6'
    elif len(d) == 4:
        type ='1'
    elif len(d) == 5:
        type ='0'
    elif len(d) == 2:
        if 4 in d.values():
            type ='5'
        else:
            type ='4'
    else:
        if 2 in d.values():
            type ='2'
        else:
            type ='3'

    return int(type)

def compare2(ii, ij):
    # if greater, return True
    line1 = lista[ii].split()
    line2 = lista[ij].split()
    type1 = gettypewj(line1[0])
    type2 = gettypewj(line2[0])
    if type1 > type2: # compare type
        return True
    elif type1 < type2:
        return False
    else: # if type same
        for i in range(5): # compare character by chaacter
            if retnum(line1[0][i]) > retnum(line2[0][i]):
                return True
            elif retnum(line1[0][i]) < retnum(line2[0][i]):
                return False
              
def part1(lista):     
    for i in range(len(lista)): # bubble sort
        for j in range(0, len(lista)-i-1):
            if compare2(j, j+1): # comopare which bigger
                r = lista[j] # if bigger, swap
                lista[j] = lista[j+1]
                lista[j+1] = r
    sum = 0
    for i in range(len(lista)):
        sum += int(lista[i].split()[1]) * (i+1) # calculate sum
    print(sum)


def part2(lista):
    for i in range(len(lista)): # bubble sort
        for j in range(0, len(lista)-i-1):
            if compare2(j, j+1): # comopare which bigger
                r = lista[j] # if bigger, swap
                lista[j] = lista[j+1]
                lista[j+1] = r
    sum = 0
    for i in range(len(lista)):
        sum += int(lista[i].split()[1]) * (i+1) # calculate sum
    print(sum)

part2(lista)


