file=open("./club/advent of code/input.txt")
lista=file.readlines()
file.close()

suma = 0

for i in range(len(lista)):
    num = ''

    for j in range(len(lista[i])):
        if lista[i][j].isnumeric():
            num += lista[i][j]
            break
        else:
            if lista[i][j] == 'o' and j+2 < len(lista[i]):
                if lista[i][j+1] == 'n' and lista[i][j+2] == 'e':
                    num += '1'
                    break
            elif lista[i][j] == 't' :
                if j+2 < len(lista[i]):
                    if lista[i][j+1] == 'w' and lista[i][j+2] == 'o':
                        num += '2'
                        break
                    
                if j+4 < len(lista[i]):
                    if lista[i][j+1] == 'h' and lista[i][j+2] == 'r' and lista[i][j+3] == 'e' and lista[i][j+4] == 'e':
                        num += '3'
                        break
                    
            
            elif lista[i][j] == 'f' and j+3 < len(lista[i]):
                if lista[i][j+1] == 'o' and lista[i][j+2] == 'u' and lista[i][j+3] == 'r':
                    num += '4'
                    break
                elif lista[i][j+1] == 'i' and lista[i][j+2] == 'v' and lista[i][j+3] == 'e':
                    num += '5'
                    break
            if lista[i][j] == 's' and j+2 < len(lista[i]):
                if lista[i][j+1] == 'i' and lista[i][j+2] == 'x':
                    num += '6'
                    break
            if lista[i][j] == 's' and j+4 < len(lista[i]):
                if lista[i][j+1] == 'e' and lista[i][j+2] == 'v' and lista[i][j+3] == 'e' and lista[i][j+4] == 'n':
                    num += '7'
                    break
            if lista[i][j] == 'e' and j+4 < len(lista[i]):
                if lista[i][j+1] == 'i' and lista[i][j+2] == 'g' and lista[i][j+3] == 'h' and lista[i][j+4] == 't':
                    num += '8'
                    break
            if lista[i][j] == 'n' and j+3 < len(lista[i]):
                if lista[i][j+1] == 'i' and lista[i][j+2] == 'n' and lista[i][j+3] == 'e':
                    num += '9'
                    break

    for k in range(len(lista[i])-1, -1, -1):
        if lista[i][k].isnumeric():
            num += lista[i][k]
            break
        else:
            if lista[i][k] == 'e' and k-2 >= 0:
                if lista[i][k-1] == 'n' and lista[i][k-2] == 'o':
                    num += '1'
                    break
            
            
            if lista[i][k] == 'e' and k-3 >= 0:
                if lista[i][k-1] == 'v' and lista[i][k-2] == 'i' and lista[i][k-3] == 'f':
                    num += '5'
                    break
                if lista[i][k-1] == 'n' and lista[i][k-2] == 'i' and lista[i][k-3] == 'n':
                    num += '9'
                    break
            
            if lista[i][k] == 'e' and k-4 >= 0:
                if lista[i][k-1] == 'e' and lista[i][k-2] == 'r' and lista[i][k-3] == 'h' and lista[i][k-4] == 't':
                    num += '3'
                    break
            

            if lista[i][k] == 'o' and k-2 >= 0:
                if lista[i][k-1] == 'w' and lista[i][k-2] == 't':
                    num += '2'
                    break
            
            if lista[i][k] == 'r' and k-3 >= 0:
                if lista[i][k-1] == 'u' and lista[i][k-2] == 'o' and lista[i][k-3] == 'f':
                    num += '4'
                    break
                
            if lista[i][k] == 'x' and k-2 >= 0:
                if lista[i][k-1] == 'i' and lista[i][k-2] == 's':
                    num += '6'
                    break
            
            if lista[i][k] == 'n' and k-4 >= 0:
                if lista[i][k-1] == 'e' and lista[i][k-2] == 'v' and lista[i][k-3] == 'e' and lista[i][k-4] == 's':
                    num += '7'
                    break
            if lista[i][k] == 't' and k-4 >= 0:
                if lista[i][k-1] == 'h' and lista[i][k-2] == 'g' and lista[i][k-3] == 'i' and lista[i][k-4] == 'e':
                    num += '8'
                    break
            
    suma += int(num)

print(suma)