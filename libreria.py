# CREAMOS CLASE LIBRO
class Libro:
    # Atributos
    def __init__(self, titulo, autor, anho):
        self.titulo = titulo
        self.autor = autor
        self.anho = anho

    # Métodos
    def mostrar_info(self):
        return f"\n- {self.titulo} - {self.autor} del año {self.anho}"

# CREAMOS CLASE BIBLIOTECA
class Biblioteca:
    # Atributos
    def __init__(self):
        self.libros = []

    # Métodos
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def vender_libro(self, libro):
        self.libros.remove(libro)

    def buscar_libro(self, busca):
        for libro in self.libros:
            if busca == libro.titulo:
                print(f"\n¡Encontrado!: {libro.mostrar_info()}")
                return

        print("\nEl libro no le tenemos en la biblioteca")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca no tiene libros en este momento.")
        else:
            print("\nLibros disponibles:")
            for libro in self.libros:
                print(libro.mostrar_info())

    # EXTRA:
    def prestar_libro(self, libro):
        print(f"\n{libro.mostrar_info()} ha sido prestado")

    def intercambiar_libro(self, libro_entregado, n_libro):
        self.libros[n_libro] = libro_entregado
        self.mostrar_libros()

# Agregamos coches
libro1 = Libro("La Chica del Tren", "Paula Hawkins", "2012")
libro2 = Libro("El Cuco de Cristal", "Javier Castillo", "2017")
libro3 = Libro("La Mujer de Arriba", "Freida McFadden", "2024")
libro_entregado = Libro("La Chica de Nieve", "Javier Castillo", "2014")

casa_del_libro = Biblioteca()

casa_del_libro.agregar_libro(libro1)
casa_del_libro.agregar_libro(libro2)
casa_del_libro.agregar_libro(libro3)

#casa_del_libro.vender_libro(libro1)

casa_del_libro.mostrar_libros()

casa_del_libro.buscar_libro("El Cuco de Cristal")

# EXTRA
#casa_del_libro.prestar_libro(libro1)

#casa_del_libro.intercambiar_libro(libro_entregado, 1)