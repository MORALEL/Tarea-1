3#Solicitar al usuario que ingrese su ingreso anual
ingreso = float(input("Ingrese su ingreso anual en colones: "))

#Calcular el impuesto o bono 
if ingreso < 200000:
    bono = ingreso * 0.03
    print("No paga impuesto, Recibe un bono de", round(bono, 2), "colones.")
elif ingreso <= 380500:
    impuesto = ingreso * 0.015
    print("El impuesto a pagar es de", round(impuesto, 2), "colones.")
else:
#Impuestos
    impuestoBajo = 380500 * 0.015
    impuestoAlto = (ingreso - 380500) * 0.15
    totalImpuesto = impuestoBajo + impuestoAlto
    print("El impuesto a pagar es de", round(totalImpuesto, 2), "colones.")