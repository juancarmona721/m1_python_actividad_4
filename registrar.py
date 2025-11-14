inventory =[]

follow = True

while follow:
    print("==================")
    print("====BIENVENIDO====")
    print("==================")
    try:
        print("==================")
        number_repeat=int(input("ingrese el numero de productos que vas a registrar: "))
        print("==================")
        for i in range (number_repeat):
            c = i + 1
            print(f"Ingresa los datos para el producto {c}")
            caducity=input("su producto esta vencido? SI/NO: ")
            if caducity == "si".lower():
                print(" producto no apto para registro")
            else:
                product_name=input("ingrese el nombre del producto: ")
                product_price=float(input("ingrese el valor de su producto: "))
                quantity_product=int(input("ingrese la cantida de su producto: "))
                dictionary={
                    'name':product_name, 
                    'price':product_price,
                    'quantity':quantity_product
                }
                inventory.append(dictionary)
                print("/ / / / /")
                print(f"Producto registrado: {dictionary['name']} | Precio: {dictionary['price']} | Cantidad: {dictionary['quantity']}")
                print("/ / / / /")
                total_value=print(f"El valor total para este producto es: {dictionary['price'] * dictionary['quantity']}")
                print("/ / / / /")
                print(inventory)
    except ValueError:
        print("\ \ \ \ \ \ \ \ \ \ \ ")
        print("ingrese un dato valido")
        print("\ \ \ \ \ \ \ \ \ \ \ ")
    break

    