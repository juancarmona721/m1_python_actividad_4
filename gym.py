days=[]
follow = True
total_days=0
total_points=0

while follow:
    print("---GYM PROFIT---")
    try:
        weeks=int(input("cuantas semanas quieres ingresar: "))
        for i in range (weeks):
            c = i + 1
            print("/ / / / / / / ")
            print(f"ingrese los dias para semana {c}")
            print("/ / / / / / / ")
            days_count =int(input("Ingrese la cantidad de dias entrenados: "))
            
            
            if days_count >7 :
                while follow:
                    try:
                        print("dato invalido, solo hay 7 dias en la semana")
                        break
                    except ValueError:
                        pass
                week_points = 0    
            elif days_count >=5:
                print("Excelente!! +10 puntos")
                week_points=10
            elif days_count  >=3:
                print("!Muy bien! +5 puntos")
                week_points=5
            elif days_count <3:
                print("Puedes hacerlo mejor +2 puntos")
                week_points=2
            dictionary = {
                'dias':days_count,
                'puntos':week_points
            }
            days.append(dictionary)

        respuesta = input("¿Quieres ingresar más semanas? (s/n): ")
        if respuesta.lower() != 's':
            follow = False 

    except ValueError:
        print("ingrese numeros por favor")
        print("\n--- ¡CÁLCULO TOTAL! ---")

total_dias = 0
total_puntos = 0

for semana in days:
    total_dias = total_dias + semana['dias']
    total_puntos = total_puntos + semana['puntos']

print(f"En total entrenaste {total_dias} días.")
print(f"¡Acumulaste un total de {total_puntos} puntos!")            
