class estudiante():
    def __init__(self):
        self.promedio = []
        self.materias = []
        self.nombre = []
        self.filas = 0
        self.columnas = 0
    
    def registro_alumnos(self):
        self.promedio = []
        self.materias = []
        self.nombre = []
        self.filas = 0
        self.columnas = 0
    
    def promedio_es(self):
        if not self.nombre:
            print("INGRESA MAS VALORES (promedios) primero (Opción 2).")
            return
            
        print("--- INGRESO DE PROMEDIOS FINALES ---")
        
        for i in range(len(self.nombre)):
            while True:
                try:
                    promedio = float(input(f"INGRESA EL PROMEDIO FINAL de {self.nombre[i]}: "))
                    if 0 <= promedio <= 100:
                        self.promedio.append(promedio)
                        break
                    else:
                        print("Promedio fuera de rango (0-100).")
                except ValueError:
                    print("INGRESA EL PROMEDIO EN FORMATO NUMÉRICO.")
            
    def alumnos_total(self):
        self.registro_alumnos()
        
        while True:
            try:
                total = int(input("Cuantos alumnos se registraran: "))
                if total > 0:
                    self.filas = total
                    break
                else:
                    print("el numero de alumnos deve ser mayor a 0")
            except ValueError:
                print("Ingresa un número entero.")
        
        while True:
            try:
                unidades = int(input("¿Cuántas unidades/parciales tiene la materia? "))
                if unidades > 0:
                    self.columnas = unidades
                    break
                else:
                    print("El número de unidades debe ser mayor a 0.")
            except ValueError:
                print("Ingresa un número entero.")

        for i in range(total):
            print(f"numero de alumnos {i+1}")
            nombre_alumno = input("Ingresa nombre del alumno:")
            self.nombre.append(nombre_alumno)
            
        self.materias = [['L'] * self.columnas for _ in range(self.filas)]
        print(f"Matriz de calificaciones inicializada {self.filas}x{self.columnas}.")

    def materias_al(self):
        if not self.promedio or len(self.promedio) <= 0:
            print("INGRESA MAS VALORES (promedios) primero (Opción 2).")
            return
            
        Mayor_prom = max(self.promedio)
        indice_mas = self.promedio.index(Mayor_prom)
        
        print(f"Nombre del alumno con mas promedio es {self.nombre[indice_mas]}")
        print(f"Con un promedio de {Mayor_prom:.2f}")

        Min_prom = min(self.promedio)
        indice_min = self.promedio.index(Min_prom)
        
        print(f"El nombre del alumno con promedio mas bajo es: {self.nombre[indice_min]}")
        print(f"Cuenta con un promedio de {Min_prom:.2f}")

    def matriz(self):
        if self.filas == 0:
            print("Primero registra alumnos (Opción 1).")
            return
            
        print("Calificaciones de alumnos")
        print(f"Hay {self.filas} alumnos y {self.columnas} unidades.")

        try:
            r = int(input(f"Elige el numero de lista de alumno (0 al {self.filas-1}):"))
            c = int(input(f"Elige el numero de unidad de la materia (0 al {self.columnas-1}):"))
        except ValueError:
            print("deves de ingresar numeros enteros")
            return
        
        if not (0 <= r < self.filas and 0 <= c < self.columnas):
            print("No encontrado. El índice de alumno o unidad está fuera de rango.")
            return

        while True:
            try:
                calificacion = float(input(f"Ingresa la calificación de {self.nombre[r]} en Unidad {c}: "))
                if 0 <= calificacion <= 100:
                    break
                else:
                    print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")
        
        self.materias[r][c] = calificacion
        print(f"calificacion guardada: {self.nombre[r]} en Unidad {c} con {calificacion}")

        print("\n--- MATRIZ DE CALIFICACIONES ---")
        for fila in self.materias:
            print(fila)
            
    def menu(self):
        while True:
            print("\n--- MENU DE REGISTRO ---")
            print("registra alumno (1)")
            print("Guardar promedios (2)")
            print("Calificacion por unidad (3)")
            print("Alumno mayor y menor promedio (4)")
            print("SALIR (5)")

            op = input("Elije una opcion: ")

            if op == '1':
                self.alumnos_total() 
            elif op == '2':
                self.promedio_es()
            elif op == '3':
                self.matriz()
            elif op == '4':
                self.materias_al()
            elif op == '5':
                print("saliendoooo")
                break
            else:
                print("obsion del 1 al 5")

if __name__ == "__main__":
    registro1 = estudiante()
    registro1.menu()