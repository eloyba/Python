monedero = 1000
print ("Tu saldo disponible es:", monedero)
comprado = []
class Soldado:
    def __init__(self , raza):
        self.raza = raza
        if raza == "Elfo":
            self.vida = 80
            self.velocidad = 10
            self.coste = 200
        elif raza == "Humano":
            self.vida = 100
            self.velocidad = 7
            self.coste = 100
        elif raza == "Enano":
            self.vida = 120
            self.velocidad = 3
            self.coste = 180
class Armas:
    def __init__(self, arma):
        self.arma = arma
        if arma == "Espada":
            self.daño = 15
            self.velocidad = 4
            self.coste = 50
        elif arma == "Hacha":
            self.daño = 20
            self.velocidad = 2
            self.coste = 60
        elif arma == "Arco":
            self.daño = 10
            self.velocidad = 8
            self.coste = 30
terminamos = False
while terminamos == False:
    opciones = input("¿Que quieres hacer? Si eliges 1 puedes comprar, si eliges 2 puedes ver lo que has comprado y si eliges 3 finalizar la compra: ")
    while opciones != "1" and opciones != "2" and opciones != "3":
        opciones = input("Esa opcion no es valida, elige 1, 2 o 3: ")
    if opciones == "1":
        opcines_compra = ["Humano","Elfo","Enano","Espada","Hacha","Arco"]
        print ("Esto es lo que puedes comprar:")
        print ("Soldados: 1-Humano, 2-Elfo, 3-Enano.")
        print ("Armas: 4-Espada, 5-Hacha, 6- Arco.")
        compra = input("¿Que quieres comprar?: ")
        while compra != "1" and compra != "2" and compra != "3" and compra != "4" and compra != "5" and compra != "6":
            compra = input("No has elegido un opcion correcta, ¿Que quieres comprar?: ")
        if compra == "1":
            valor = Soldado("Humano")
            print ("Un humano cuesta:", valor.coste)
            cobrar = input("¿Quieres comprarlo (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.raza)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
        elif compra == "2":
            valor = Soldado("Elfo")
            print ("Un elfo cuesta", valor.coste)
            cobrar = input("¿Quieres comprarlo (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.raza)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
        elif compra == "3":
            valor = Soldado("Enano")
            print ("Un enano cuesta", valor.coste)
            cobrar = input("¿Quieres comprarlo (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.raza)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
        elif compra == "4":
            valor = Armas("Espada")
            print ("Una espada cuesta", valor.coste)
            cobrar = input("¿Quieres comprarla (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.arma)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
        elif compra == "5":
            valor = Armas("Hacha")
            print ("Una hacha cuesta", valor.coste)
            cobrar = input("¿Quieres comprarla (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.arma)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
        elif compra == "6":
            valor = Armas("Arco")
            print ("Un arco cuesta", valor.coste)
            cobrar = input("¿Quieres comprarlo (Si/No)?: ")
            while cobrar != "Si" and cobrar != "No":
                cobrar = input("Por favor responde Si o No: ")
            if cobrar == "Si":
                if monedero >= valor.coste:
                    monedero = monedero - valor.coste
                    comprado.append(valor.arma)
                    print ("Ahora tu saldo es", monedero)
                elif monedero < valor.coste:
                    print ("No tienes suficiente dinero")
            elif cobrar == "No":
                pass
    elif opciones == "2":
        print ("Esto es lo que has comprado", comprado, "y tu saldo es", monedero)
    else:
        print ("Hemos terminado")
        terminamos = True
