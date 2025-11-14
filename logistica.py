normal=0
express=0
urgent=0
follow=True

while follow:
    print("---ENVIOS DE PAQUETES LA CUCHA---")
    try:
        packages_count=int(input("ingrese la cantidad de paquetes a enviar: "))
        for i in range (packages_count):
            c = i + 1
            print("=================")
            print(f"-  -PAQUETE {c}-  -")
            print("=================")
            descision=int(input("que prioridad es su paquete\n1. NORMAL\n2. EXPRESS\n3.URGENTE: "))
            if descision == 1:
                normal +=1
            elif descision == 2:
                express +=1
            elif descision == 3:
                urgent +=1
            else:
                print("dato invalido, ingrese el valor nuevamente")
                continue    
        
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print(f"TIENES:\npaquetes normales:{normal}\npaquetes express:{express}\npaquetes urgentes{urgent}")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

    except ValueError:
        print("solo datos numericos")  
