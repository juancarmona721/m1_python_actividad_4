follow = True
estudiantes=[]
while follow:
    quantity_students=int(input("cuantos estudiantes se les calculara el promedio? "))
    for i in range (quantity_students):
            c = i + 1
            try:
                print(f"notas del estudiante {c}")
                while follow:  
                    try:
                        puntuation_1=float(input("ingrese nota 1: "))
                        if puntuation_1 >5 or puntuation_1<0:
                            print("ERROR: solo notas de 0-5")
                            continue
                    except ValueError:
                        print("valor invalido")
                        continue
                    break        
                while follow:
                    try:                 
                        puntuation_2=float(input("ingrese nota 2: "))       
                        if puntuation_2 >5 or puntuation_2<0:
                            print("ERROR: solo notas del 0-5")
                            continue                        
                    except ValueError:
                        print("dato invalido")
                        continue
                    break    
                while follow:
                    try:                
                        puntuation_3=float(input("ingrese nota 3: "))       
                        if puntuation_3 >5 or puntuation_3<0:
                            print("ERROR: solo notas de 0-5")
                            continue
                    except ValueError:
                        print("dato invalido")
                        continue
                    break    
                average= (puntuation_1 + puntuation_2 + puntuation_3) / 3
                if average <3:
                    print(f"su estudiante {c} reprobo")
                else:
                    print(f"su estudiante {c} aprobo")
                dictionary={
                    'student': c,
                    'average': average,
                }
                estudiantes.append(dictionary)
            except ValueError:
                print("LAS NOTAS SON INVALIDA")   

    print(f"este es el promedio de cada estudiante es {estudiantes}")
    
        
