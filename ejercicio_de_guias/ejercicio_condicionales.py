
"""
edad no valida
niño/as <= 12
adolecentes <= 17
adultos <= 64
adulto mayor <= 120
edad no valida => 120
"""
edad = int(input("ingrese la edad de la persona: "))
if edad < 0 or edad > 120:
    categoria = "Edad no valida"
elif edad <= 12:
    categoria = "niño/a"
elif edad <= 17:
    categoria = "adolecente"
elif edad <= 64:
    categoria = "adulto"
elif edad <= 120:
    categoria = "adulto mayor"
print(f"la persona es: {categoria}")

