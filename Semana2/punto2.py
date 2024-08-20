#psicina

largo=float(input("digita el largo de la piscina:"))
ancho=float(input("digita el ancho de la piscina:"))
profundidad=float(input("digita la profundidad dela psicina en metros: "))


costoPorMetroCubico= float(input("Ingrese el costo por metro cúbico de agua:"))
volumen=largo*ancho*profundidad

pago=volumen*costoPorMetroCubico
print(f"su pago total es de: ${pago}pesos")