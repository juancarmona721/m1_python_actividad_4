available_rooms_count = 0
occuped_rooms_count = 0
available_room_list = []
follow = True
print("===== BIENVENIDO AL SISTEMA DEL HOTEL =====")

while follow:
    try:
        total_room_input = int(input("Ingrese el número total de habitaciones a registrar: "))
        if total_room_input <= 0:
            print("ERROR: El número de habitaciones debe ser 1 o más.")
            continue
        break
    except ValueError:
        print("Entrada no válida: Por favor, ingrese un número válido.")

for i in range(total_room_input):
    c = i + 1
    while follow:
        try:
            room_id_input = int(input(f"Ingrese el ID para la habitación {c}: "))
            break
        except ValueError:
            print("Entrada no válida: Por favor, ingrese un número para el ID.")
            continue
    
    print("................")
    
    while follow:
        status_input = input(f"La habitación {room_id_input} está ocupada? (si/no): ").lower()
        
        if status_input == "si":
            print(f"Habitación {room_id_input} registrada como ocupada.")
            occuped_rooms_count += 1
            break
        elif status_input == "no":
            print(f"Habitación {room_id_input} registrada como disponible.")
            available_rooms_count += 1
            available_room_list.append(room_id_input)
            break
        else:
            print("Opción inválida. Por favor, ingrese (si/no).")

print("====================================")
print("Las siguientes habitaciones están disponibles:")
for room_num in available_room_list:
    print(f"-> Habitación {room_num}")
print("====================================")
print(f"Reporte Final: {occuped_rooms_count} habitación(es) ocupada(s) y {available_rooms_count} habitación(es) disponible(s).")