nombres = ["Pedro", "Maria", "Juan"]
print(len(nombres))
print(nombres[1])
nombres[1] = "Ana"
print(nombres[1])
print(nombres)
nombres.insert(1, "Alfredo")
print(nombres)
nombres.remove("Pedro")
print(nombres)
print("Juan" in nombres)