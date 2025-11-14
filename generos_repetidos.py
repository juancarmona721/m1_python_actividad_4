song=[]
follow = True
while follow:
    try:
        print("[[[ESTA ES TU LISTA DE CANCIONES]]]")
        song_input= int(input("cuantas canciones vas a ingresar? "))
            
        
        for i in range (song_input):
            song_name=input(" ingrese el nombre de la cancion: ")
            song_gender=input("cual es el genero de su cancion? ")
            dictionary={
                'nombre':song_name,
                'genero':song_gender
            }
            song.append(dictionary)
        print(f"{song}.")

        for gender in {song['genero']}:
            print("genero ya esxiste")

    
        print(f"sus canciones ya generos son{song}")
    
    except ValueError:
        pass
