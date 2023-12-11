
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
#Ejercicio de Reservacion de hotel
costo_simple = 10
costo_doble = 20
costo_familiar = 40

costo_vista_mar = 10
costo_vista_restaurante = 5
costo_sin_adicional = 0

tipo_habitacion = int(input("Seleccione el tipo de habitación (1.-simple, 2.-doble, 3.-familiar): "))
adicional = int(input("Seleccione un adicional (1.-vista_mar, 2.-vista_restaurante, 3.-sin_adicional): "))
num_huespedes = int(input("Ingrese el número de huéspedes: "))

if tipo_habitacion == 1:
    costo_total = costo_simple
elif tipo_habitacion == 2:
    costo_total = costo_doble
elif tipo_habitacion == 3:
    costo_total = costo_familiar
else:
    print("Tipo de habitación no válido. Por favor, seleccione 1, 2 o 3.")
    costo_total = 0


if adicional == 1:
    costo_total += costo_vista_mar
elif adicional == 2:
    costo_total += costo_vista_restaurante
elif adicional == 3:
    costo_total += costo_sin_adicional
else:
    print("Adicional no es válido. Seleccione 1, 2 o 3.")

for i in range(num_huespedes):
    tipo_alimentacion = int(input(f"Tipo de alimentación para el huésped {i + 1} (1.-Todo incluido, 2.-Todo incluido niños, 3.-Solo desayuno, 4.-Sin alimentación): "))
    
    if tipo_alimentacion == 1:
        costo_total += 0  # Todoo incluido
    elif tipo_alimentacion == 2:
        costo_total += 0  # Todko incluido niños
    elif tipo_alimentacion == 3:
        costo_total += 5  # Solo desaykuno
    elif tipo_alimentacion == 4:
        costo_total += 0  # Sin alimenhntación
    else:
        print("Tipo de alimentación no válido. Seleccione 1, 2, 3 o 4.")


print(f"El costo total de la reserva es: ${costo_total}")
