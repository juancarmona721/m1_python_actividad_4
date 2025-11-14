cars=[]
follow = True
piece_value=50000
hour_value=20000

while follow:
    try:
        quantity_cars=int(input("cuantos vehiculos ingresan? "))
        for i in range (quantity_cars):
            c = i + 1
            print(f"-----Datos vehiculo {c}-----")
            worked_hours=int(input("ingrese la cantidad de horas trabajadas en el vehiculo:  "))
            changed_pieces=int(input("ingrese la cantidad de piezas cambiadas:  "))
            dictionary={
                'hours':worked_hours,
                'pieces':changed_pieces
            }
            cars.append(dictionary)
            if worked_hours >10:
                print("esta reparacion fue COMPLICADA")
            elif    changed_pieces >4:
                print("esta reparacion fue COMPLICADA")
            else:
                print("la reparacion fue LLEVADERA")   
        total = (worked_hours * hour_value)+(changed_pieces * piece_value)
        for car in cars:
            print("/ / / / / / / / / / / / / ")
            print(f"el valor de horas trabajadas es de {worked_hours * hour_value} y el valor de las piezas es {changed_pieces * piece_value}\nEl total es {total}")
    except ValueError:
        print("ERROR: solo datos numericos por favor")

            
