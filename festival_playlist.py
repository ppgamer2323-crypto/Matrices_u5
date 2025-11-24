
class festival:
    def __init__(self):
        self.nombre = ["no asignado"]
        self.artista = ["no asignado"]
        self.duracion_minutos = ["no asignado"]
        self.popularidad = ["no asignado"]

    def registrar_caniones(self, nombre, artista, duracion_minutos):
        self.nombre = ["no asignado"]
        self.artista = ["no asignado"]
        self.duracion_minutos = ["no asignado"]
        self.popularidad = ["no asignado"]

    def cancion2(self, nombre):
        print("===========================")
        while True:
            try:
                total = int(input("cuantas canciones deseas agregar: "))
                if total > 0:
                    break
                else:
                    print("El número debe ser mayor o igual a 1")
            except ValueError:
                print("Ingresa un valor numérico válido")

        for i in range(total):
            print(f"numero de canción {i+1}")
            n_nombre = input("Ingresa el nombre de la canción: ")
            nombre.append(n_nombre)

        print(f"canciones guardadas: {nombre}")

    def artistas(self, artista):
        print("===========================")

        while True:
            try:
                nuevos_nombres = int(input("¿Cuántos artistas deseas agregar?: "))
                if nuevos_nombres > 0:
                    break
                else:
                    print("Debe ser un número mayor a 0")
            except ValueError:
                print("Valor inválido. Ingresa un número.")

        for i in range(nuevos_nombres):
            nombre_artista = input(f"Ingresa el nombre del artista {i+1}: ")
            artista.append(nombre_artista)

        print("===========================")

    def cancion_mas_popular(self, popularidad):
        print("===========================")

        if len(self.popularidad) <= 1:
            print("No hay datos suficientes para calcular la canción más popular.")
            return

        mayor_popu = max(self.popularidad[1:])
        mas = self.popularidad.index(mayor_popu)
        print(f"La canción más popular es: {self.nombre[mas]}")
        print(f"Artista: {self.artista[mas]}")
        print(f"Popularidad: {mayor_popu}")

        mini_popu = min(self.popularidad[1:])
        mini = self.popularidad.index(mini_popu)
        print(f"La canción más popular es: {self.nombre[mini]}")
        print(f"Artista: {self.artista[mini]}")
        print(f"Popularidad: {mini_popu}")

    def buscar_por_popullaridad(self, popularidad, nombre, artista):
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))

        encontrado = False
        for i in range(len(popularidad)):
            if minimo <= popularidad[i] <= maximo:
                print(f"{nombre[i]} - {artista[i]} (Popularidad: {popularidad[i]})")
                encontrado = True

        if not encontrado:
            print("No se encontro canciones")

    def buscar_por_artista(self, artista, nombre):
        artista_buscar = input("Ingresa el nombre del artista: ")
        print("Resultados")
        encontrado = False

        for i in range(len(artista)):
            if artista[i].lower() == artista_buscar.lower():
                print(f"{nombre[i]} - {artista[i]} (Popularidad: {self.popularidad[i]})")
                encontrado = True

        if not encontrado:
            print("No se encontraron canciones de ese artista.")


obj = festival()

while True:
    print("===== MENU =====")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        obj.cancion2(obj.nombre)
        obj.artistas(obj.artista)

        print("===========================")
        cant = int(input("¿Cuántas popularidades deseas agregar?: "))
        for i in range(cant):
            pop = int(input(f"Ingresa popularidad de la canción {i+1}: "))
            obj.popularidad.append(pop)

        print("Popularidades guardadas:", obj.popularidad)
        print("===========================")

    elif opcion == "2":
        obj.cancion_mas_popular(obj.popularidad)

    elif opcion == "3":
        print( "Buscar por artista")
        print("2. Buscar por rango de popularidad")
        sub = input("Elige una opción: ")

        if sub == "1":
            obj.buscar_por_artista(obj.artista, obj.nombre)

        elif sub == "2":
            obj.buscar_por_popullaridad(obj.popularidad, obj.nombre, obj.artista)

        else:
            print("Opción inválida")

    elif opcion == "4":
        print("Playlist recoendada.")

    elif opcion == "5":
        print("Saliendo del programa")
        break


programa_principal = festival()


       
    
    
         






    
    
         








       






