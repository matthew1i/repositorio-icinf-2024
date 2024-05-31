a1 = input("ingresa un breve resumen de tu articulo menor a 60 caracteres ").upper()
a2 = len(a1)<60
print(a2)
print(a1[-10:])
print("-".join(a1.split()))


