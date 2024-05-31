p1 = input("ingresa un producto con mas de 40 caracteres: " ).upper()
while len(p1)<40:
    p1 = input("Repite el producto hasta que tenga 40 caracteres")
s1="patatatatatatta"
l1 = s1 + " ".join(p1.split(" "))
print(l1)
p2 = input("ingresar el segundo producto que tenga mas dwe 40 caracteres: ").upper()
while len(p2)<40:
    p2 = input("Repite el producto hasta que tengas mas de 40 caracteres")

