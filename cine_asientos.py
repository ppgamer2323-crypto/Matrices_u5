class CINE:
    def __init__(self):
        self.sala = None
        self.filas = 0
        self.columnas = 0
        self.nombre_funcion = "No asignada"

    def inicializar_sala(self):
        while True:
            try:
               
                filas_input = int(input("Ingresa el número de FILAS de la sala: "))
                columnas_input = int(input("Ingresa el número de COLUMNAS: "))
                
                if filas_input <= 0 or columnas_input <= 0:
                    print("Valor incorrecto, tiene que ser mayor a 0")
                    continue
                
                self.filas = filas_input
                self.columnas = columnas_input
                
                self.sala = [['L'] * self.columnas for _ in range(self.filas)]
                
                n_nuevo = input("Ingresa el nombre de la película/función: ")
                self.nombre_funcion = n_nuevo
                
                print(f"\n La sala de cine se registro {self.filas}x{self.columnas}")
                print(f"Nombre de la función: {self.nombre_funcion}")
                break 
            except ValueError:
                print("Entrada inválida")
            

    def mostrar_sala(self):
        if self.sala is None:
            print("\nLa sala aún no ha sido inicializada.")
            return

    
        
    
        header = "   " + " ".join([str(c) for c in range(self.columnas)])
        print(header)
        print("  " + "=" * (self.columnas * 2 + 1))

        for r in range(self.filas):
            fila_str = " ".join(self.sala[r])
            print(f"{r} | {fila_str}")
        print("__________________________________________")

    def reservar_asiento(self):
        
        if self.sala is None:
            print("Primero inicializa la sala.")
            return

        print("\n=====RESERVAR ASIENTO=====")
        try:
            r = int(input(f"Elige la FILA (0 a {self.filas - 1}): "))
            c = int(input(f"Elige la COLUMNA (0 a {self.columnas - 1}): "))
        except ValueError:
            print(" Debes ingresar números enteros.")
            return

        if not (0 <= r < self.filas and 0 <= c < self.columnas):
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            return
        
        if self.sala[r][c] == 'L':
            self.sala[r][c] = 'X'
            print(f"\nAsiento ({r}, {c}) ocupado con éxito.")
        else:
            print("\nEste asiento ya está ocupado (X)")


    def contar_asientos(self):
        if self.sala is None:
            print("Primero inicializa la sala.")
            return
            
        ocupados = 0
        libres = 0
        
        for fila in self.sala:
            for asiento in fila:
                if asiento == 'R':
                    ocupados += 1
                else: 
                    libres += 1
                    
        total = ocupados + libres
        
        
        print("__________________________________________")
        print(f"Función actual: {self.nombre_funcion}")
        print("__________________________________________")
        print(f"Total de Asientos: {total}")
        print("__________________________________________")
        print(f"Asientos Libres ('L'): **{libres}**")
        print("__________________________________________")
        print(f"Asientos Ocupados ('R'): **{ocupados}**")
        print("__________________________________________")

    def menu(self):
        self.inicializar_sala() 
        
        while True:
            print("\n Ingresa alguna opcion para poder continuar")
            print("__________________________________________")
            print("(1) Mostrar sala")
            print("__________________________________________")
            print("(2) Reservar asiento")
            print("__________________________________________")
            print("(3) . Liberar asiento y  Contar asientos ocupados y libres")
            print("__________________________________________")
            print("(4) Salir")
            print("__________________________________________")
            
            opcion = input("ELIJE UNA OPCIÓN: ")
            
            if opcion == '1':
                self.mostrar_sala()
            elif opcion == '2':
                self.reservar_asiento()
            elif opcion == '3':
                self.contar_asientos()
            elif opcion == '4':
                print("saliendo")
                break
            else:
                print(" Opción no válida, " \
                "Por favor, elige un número del 1 al 4.")


if __name__ == "__main__":
    programa_cine = CINE()
    programa_cine.menu()




  
