#joel 
#alondra 
#paz
j1=float(input("ingrese la nota de joel "))
j2=float(input("ingrese la segunda nota de joel "))
j3=float(input("ingrese la tercera nota de joel "))
#notas de el joel

a1=float(input("ingrese la nota de alondra "))
a2=float(input("ingrese la segunda nota de alondra "))
a3=float(input("ingrese la tercera nota de alondra "))
#notas de alondra

p1=float(input("ingrese la nota de paz "))
p2=float(input("ingrese la segunda nota de paz "))
p3=float(input("ingrese la tercera nota de paz "))
#nota de paz 

print(" la nota mas baja de joel es : ", min (j1,j2,j3))

print(" la nota mas baja de alondra es : ", min (a1,a2,a3))

print(" la nota mas baja de paz es : ", min (p1,p2,p3))

jf = (j1 + j2 + j3 )/3

af = (a1 + a2 + a3)/3

pf = (p1 + p2 + p3)/3

f = ( jf + af + pf)/3

ff = round(f,3)

print("la nota final de los tres promedios sumados es : ",ff)

