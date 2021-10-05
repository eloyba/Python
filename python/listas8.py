notas = [4,3,2,7,6,8,5,10,3,8]
suspensos = 0
aprobados = 0
sumatorio_aprobados = []
sumatorio_suspensos = []
for nota in notas:
    if nota < 5:
        suspensos = suspensos + 1
        sumatorio_suspensos.append(nota)
    elif nota >= 5:
        aprobados = aprobados + 1
        sumatorio_aprobados.append(nota)
suma_suspensos = sum(sumatorio_suspensos)
suma_aprobados = sum(sumatorio_aprobados)
print ("Hay" ,suspensos, "suspensos.")
print ("Hay" ,aprobados, "aprobados.")
print ("La nota media de suspensos es:",(suma_suspensos) // suspensos)
print ("Porcentaje de suspensos", (100 * suspensos) // 10, "%")
print ("La nota media de aprobados es:", suma_aprobados // aprobados)
print ("Porcentaje de aprobados", (100 * aprobados) // 10, "%")