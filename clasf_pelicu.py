movies = []
follow = True
while follow:
        print("/ / / / / /")
        print("--CINEMA--")
        print("/ / / / / /")
        try:
            quantity_movies = int(input("ingrese la cantidad de peliculas: "))
            for i in range (quantity_movies):
                duration = int(input("ingrese la duracion de la pelicula: "))
                if type(duration) != int:
                    print("//ingrese solo numeros por favor//")
                    dictionary = {
                        'duracion':duration
                    }
                    movies.append(dictionary)                    
                elif duration <= 100:
                    clasf_1 = print("la pelicula es corta")
                elif duration <= 150:
                    clasf_2 = print("la pelicula es media")
                elif duration >150:
                    clasf_3 = print("la pelicula es larga")

                    
        except ValueError:
            print("solo valores numericos")
