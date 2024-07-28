file=open("./club/advent of code/input.txt")
lista=file.readlines()
file.close()

suma = 0

#only 12 red cubes, 13 green cubes, and 14 blue cubes

for i in range(len(lista)): # per line
    flag = 0
    game = i + 1
    s = lista[i].split('; ')
    a = s[0].split(': ')

    s.remove(s[0])
    s.append(a[1])
    
    red = 0
    blue = 0
    green = 0
    print(s)
    
    for j in range(len(s)): 
        balls = s[j].split(', ') # game
        
        for k in range(len(balls)):
            q = balls[k].split()  # per ball
            #print(q)
            if 'red' == q[1]:
                if int(q[0]) > red:
                    red = int(q[0])
                    
            elif 'green' == q[1]:
                if int(q[0]) > green:
                    green = int(q[0])
                    
            else:
                if int(q[0]) > blue:
                    blue = int(q[0])

            #print(red, blue, green)
    suma += red*blue*green
        
     
        
print(suma)
        