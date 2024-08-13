print ("control de regsitro de litros")
produccion_litros = input("digite producido en litros: ")
print ("conversion")
conversion = int(produccion_litros)*float(3.785)

print ("valor del galon")
valor = input("digite el valor: ")

print ("ganacias")
ganancia = conversion*int(valor)
print (f'ganancia del productos son {ganancia}')