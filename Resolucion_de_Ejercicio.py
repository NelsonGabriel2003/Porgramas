
#Menus
opcion_doblecontocino=0
opcion_doble=0
opcion_simple=0
resultado_opc=0
opc_un_cuarto=0
opc_un_octavo=0
opc_un_medio=0
opc_familiar=0
opc_leches=0
opc_brawnie=0
cont=0 #inicializo mi contador en 0 para simular un do while con un while y un contador
while True:
    print("""Bienvenido a mi restaurante
                    El menu es:""")
    print("1.Opcion Hamburguesas\n2.Opcion pollo\n3.Opcion Postres\n4.Salir") #Strings que visualiza las opciones
    menu=input("Que opcion desearia:  ")
    if menu=="1": #Strings y casos de mis opciones  
        print("1.1 Simples 1.50\n1.2 Dobles 2\n1.3 Doble Con Tocino 2.50")
        menu=input("Que opcion de hamburguesa desearia: ")
        opcion_1=float(menu)
        if opcion_1==1.1:
            opcion_simple=int(input("Cuantas deseria?: "))
            resultado_opc+= opcion_simple*1.50 #resultado_opc va a ser el que almacene todos los valores de la multiplicacion
            
        elif opcion_1==1.2:
            opcion_doble=int(input("Cuantas deseria?: ")) 
            resultado_opc+= opcion_doble*2
            
        elif opcion_1==1.3:
            opcion_doblecontocino=int(input("Cuantas deseria?: "))
            resultado_opc+= opcion_doblecontocino*2.50
    elif menu=="2" :
        print("2.1 1/4 3\n2.2 1/8 2.50\n2.3 1/2 4\n2.4 familiar 8") #opc_un_cuarto,opc_un_octavo,opc_un_medio,opc_familiar
        menu=input("Que opcion de pollo desearia: ")
        opcion_2=float(menu)
        if opcion_2==2.1:
                    opc_un_cuarto=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_un_cuarto*3
        if opcion_2==2.2:
                    opc_un_octavo=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_un_cuarto*2.50
        if opcion_2==2.3:
                    opc_un_medio=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_un_cuarto*4
        if opcion_2==2.4:
                    opc_familiar=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_un_cuarto*8
    elif menu=="3":
        print("\n3.1 3 Leches 3.75\n3.2 Brownie 4.10")
        menu=input("Que opcion de postre desearia: ")
        opcion_3=float(menu)
        if opcion_3==3.1:
                    opc_leches=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_leches*3.75
        if opcion_3==3.2:
                    opc_brawnie=int(input("Cuantas deseria?: "))
                    resultado_opc+= opc_brawnie*4.10
    else:
        print("vuelva pronto")  
        break                    
    cont+=1
    if cont>7:
        break
    print("")
    print(f"Hamburguesas simples: {opcion_simple}\nHamburguesas dobles: {opcion_doble}\nHamburguesas dobles con tocino: {opcion_doblecontocino}")
    print("")
    print(f"1/4 Pollo: {opc_un_cuarto}\n1/8 Pollo: {opc_un_octavo}\n1/2 Pollo: {opc_un_medio}\nPollo Familiar: {opc_familiar}")
    print("")
    print(f"3 leches: {opc_leches}\nbrawnie: {opc_brawnie}")
    print("")
    print(f"El valor total a pagar es:{resultado_opc}")

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
