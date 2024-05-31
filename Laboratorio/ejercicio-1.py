manzana = 100 
pera = 250 
durazno = 300 
print(int(manzana))
print(int(pera))
print(int(durazno))
mf = manzana * 150
pf = pera * 80
df = durazno * 120
print("la suma del precio final de las manzanas y las peras da: ")
print(mf+pf)
print("el valor mas alto es: ")
print(max(mf,pf,df))
print("el valor mas bajo es: ")
print(min(mf,pf,df))
print("el promedio de los 3 es: ")
print(round((manzana+pera+durazno)/3))