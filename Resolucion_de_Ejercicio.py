
#Menus


#Unidades
print("Ejercicio de Unidades")
unidad1 = input("Ingresar unidad actual  mm, cm, m, hm, km: ")
unidad2 = input("Ingresar unidad requerida mm, cm, m, hm, km: ")
print("Conversion")
valor = float(input("Ingresa valor: "))
if unidad1 == "mm":
    cantidad_en_metros = valor / 1000
elif unidad1 == "cm":
    cantidad_en_metros = valor / 100
if unidad1 == "m":
    cantidad_en_metros = valor
elif unidad1 == "hm":
    cantidad_en_metros = valor * 100
elif unidad1 == "km":
    cantidad_en_metros = valor * 1000
else:
    print("Unidad actual no reconocida.")
if unidad2 == "mm":
    cantidad_convertida = cantidad_en_metros * 1000
if unidad2 == "cm":
    cantidad_convertida = cantidad_en_metros * 100
if unidad2 == "m":
    cantidad_convertida = cantidad_en_metros
elif unidad2 == "hm":
    cantidad_convertida = cantidad_en_metros / 100
elif unidad2 == "km":
    cantidad_convertida = cantidad_en_metros / 1000
else:
    print("Unidad requerida no reconocida.")
print(f"{valor} {unidad1} son {cantidad_convertida} {unidad1}")


#Reservacion de Hotel

