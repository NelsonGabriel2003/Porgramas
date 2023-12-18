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
