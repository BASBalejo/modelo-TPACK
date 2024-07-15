import numpy

print("tablas de multiplicar")
c=int()
mult=int()
print("ingrese el numero para la tabla ")
x=int(input())
for c in range (0,11,1):
    mult=c*x
    print("la multiplicacion es: ",x," * ",c,"= ",mult)
    