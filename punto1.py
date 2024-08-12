#AREA RECTANGULO
print ("area del rectangulo")
base_rectangulo = input("digite la base: ")
altura_rectangulo = input("digite la altura: ")
area_rectangulo = int(base_rectangulo)*int(altura_rectangulo)
print (f'la area del rectangulo es {area_rectangulo}')

#AREA TRIANGULO
print ("area del triangulo")
base_triangulo = input("digite la base: ")
altura_triangulo = input("digite la altura: ")
area_triangulo = int(base_triangulo)*int(altura_triangulo)/2
print (f'la area del triangulo es {area_triangulo}')

#AREA DEL TERRENO 
print ("area del terreno")
area_terreno = area_rectangulo+area_triangulo
print (f'la area del terreno es {area_terreno}')

