pronombres = {"yo" : "I" , "tu": "you" , "él" : "he"}
suministros_acero = {"Aceralia":["636777888","info@aceralia.com"], "Aceros Mateo": ["679888123", "acerosmateo@gmail.com"]}
print (suministros_acero)
print (suministros_acero["Aceralia"])
suministros_acero["Hierros Mategui"] = ["699887678", "infomategui@hotmail.com"]
print (suministros_acero)
del pronombres["yo"]
print (pronombres)
print (suministros_acero.keys())
print (suministros_acero.values())