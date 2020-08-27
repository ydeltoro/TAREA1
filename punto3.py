def esperfectoono(num):
    suma = 0
    for j in range(1,num):
        if (num % j == 0):
            suma += j
    if num == suma:
        return True
    else:
        return False       
    
num = int(input("introduzca un numero:"))
 
if esperfectoono(num):
    print("%s es un numero perfecto" % num)
else:
    print("%s NO es un numero perfecto" % num)
