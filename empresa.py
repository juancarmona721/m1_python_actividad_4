follow=True



while follow:
    print("==  EVALUACIÓN DE PERSONAL ==")
    try:
        num_empleados = int(input("¿Cuántos empleados va a evaluar?: "))
        
        if num_empleados <= 0:
            print("Error: El número debe ser 1 o más.")
            continue
        break
    except ValueError:
        print("Valor inválido. Debe ingresar un número entero.")

for i in range(num_empleados):
    c = i + 1
    nombre_empleado = input(f"Nombre del empleado {c}: ")
    print(f"--- VENTAS PARA {nombre_empleado} ---")

    while follow:
        try:
            vendido1 = float(input("Ingrese la venta mes 1: "))
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número (puede ser decimal).")
            continue
            
    while follow:
        try:
            vendido2 = float(input("Ingrese la venta mes 2: "))
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número (puede ser decimal).")
            continue

    while follow:
        try:
            vendido3 = float(input("Ingrese la venta mes 3: "))
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número (puede ser decimal).")
            continue

    promedio=(vendido1 + vendido2 + vendido3) / 3

    if promedio >= 6:
        print(f"El rendimiento de {nombre_empleado} es Excelente. ¡Sigue así!")
    elif promedio >= 2.0 and promedio < 5.0:
        print(f"La calificación de {nombre_empleado} es Buena. Puedes seguir mejorando.")
    elif promedio < 2.0:
        print(f"La calificación de {nombre_empleado} es Baja. Debes subir tu nivel.")