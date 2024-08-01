import math

while True:
    print("Seleccione el numero asociado a la operacion que desee:")
    print("1-Convertir Grados a Radianes")
    print("2-Convertir Radianes a Grados")
    x = int(input())
    if x == 1:
        y = float(input("Ingrese los grados: "))
        z = y * ((math.pi) / 180)
        print(f"{y}B0 son {z} rad")
        break
    elif x == 2:
        y = float(input("Ingrese los radianes: "))
        z = y * (180 / (math.pi))
        print(f"{y} rad son {z}B0")
        break
    else:
        print("Por favor ingrese un numero que corresponda a las operaciones")
