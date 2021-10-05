numero = int(input("Elige un numero: "))
if numero > 9 and numero%2 == 0:
    print("El numero es mayor que 9 y es par")
elif numero > 9 and numero%2 ==1:
    print("El numero es mayor que 9 y es impar")
elif numero <= 9 and numero%2 == 0:
    print("El numero es menor que 9 y es par")
else:
    print("El numero es menor o igual que 9 y es impar")