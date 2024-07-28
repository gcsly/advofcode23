with open("./club/advent of code/input.txt") as f:
    lista = f.read().splitlines() 

inp = []
for i in range(len(lista)):
    a = lista[i].split()
    b = a[1].split(',')
    c = ''
    d = []
    for j in range(5):
        c += a[0]
        d.extend(b)
    inp.append([c, d])
    

print(inp)


def compare(line, num):
    c = 0
    templist = []
    for i in range(len(line)):
        if line[i] == '#':
            c += 1
            if i == len(line)-1:
                templist.append(c)
            
        if line[i] == '.':
            if c != 0:
                templist.append(c)
                c = 0
    
    if len(num) != len(templist):
        return False

    for i in range(len(num)):
        if int(num[i]) != templist[i]:
            return False

    return True
          
def case(line):
    c = 0 # num of qmarks

    #print(line)
    for i in range(len(line)):
        if line[i] == '?':
            c += 1
    
    a = []
    for i in range(2**c):
        a.append('')
        
    for i in range(2**c):
        for j in range(c):
            if (i//(2**j)) % 2 == 0:
                a[i] += '#'
            else:
                a[i] += '.'
    
    return a


def allposs(original, subs):
    a = ''
    j=0
    for i in range(len(original)):
        #print(original[i])
        if original[i] == '?':
            a += subs[j]
            j += 1
        else:
            a += original[i]
    
    return a

count = 0
for i in range(len(inp)):
    subs = case(inp[i][0])
    
    for j in range(len(subs)):
        new = allposs(inp[i][0], subs[j])

        if compare(new, inp[i][1]):
            count += 1
    print(i)
print(count)