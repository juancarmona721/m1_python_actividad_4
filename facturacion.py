print("  BIENVENIDO A FACTURAS ")

grand_total = 0

while True:
    try:
        invoice_count = int(input("¿Cuántas facturas va a registrar?: "))
        if invoice_count <= 0:
            print("Error: Debe ingresar al menos 1.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

for i in range(invoice_count):
    print(f"\n--- Factura {i+1} ---")
    customer_name = input("Ingrese el nombre del cliente: ")
    
    while True:
        try:
            invoice_amount = float(input("Ingrese el valor de la factura: "))
            if invoice_amount < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número (puede ser decimal).")
    
    print("\nTipos de Cliente:")
    print("1. Premium")
    print("2. Normal")
    
    while True:
        try:
            customer_tier = float(input("Seleccione el tipo de cliente (1 o 2): "))
            if customer_tier < 1 or customer_tier > 2:
                print("Error: El tipo debe ser 1 o 2.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número (1 o 2).")
    
    if customer_tier == 1:
        discount_amount = invoice_amount * 0.05
        print(f"¡Descuento! El cliente obtiene un 5% (Valor: {discount_amount}).")
        print(f"El total de esta factura es: {invoice_amount - discount_amount}")
        grand_total = invoice_amount
    elif customer_tier == 2:
        discount_amount = invoice_amount * 0.10
        print(f"¡Descuento! El cliente obtiene un 10% (Valor: {discount_amount}).")
        print(f"El total de esta factura es: {invoice_amount - discount_amount}")
        grand_total = invoice_amount
    
print(f"\nzLa suma total de sus facturas es: {grand_total}")

print()