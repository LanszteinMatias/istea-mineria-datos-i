class Libro:
    def __init__(self,titulo, autor, genero,  puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion


def AgregarLibro():
     lIngresoValido = False
     cTituloLibro = input("Ingrese titulo del libro: ")
     cAutorLibro = input("Ingrese el autor del libro: ")
     cGeneroLibro = input("Ingrese genero del libro: ")

     while not lIngresoValido:
          nPuntuacionLibro = input("Ingrese una puntuacion numerica entera para el libro entre el numero  1 y 10: ")
          try:
               nPuntuacionLibro = float(nPuntuacionLibro)
               lIngresoValido = True

          except:
               print("Error, no se ah ingresado un numero.")
               
          if lIngresoValido and (nPuntuacionLibro > 10 or nPuntuacionLibro < 1):
               lIngresoValido = False
               print("El Nro. Ingresado debe estar entre 1 y 10")

     lista_libros.append(Libro(cTituloLibro,cAutorLibro,cGeneroLibro,nPuntuacionLibro))
     if input("Si desea agregar otro libro escriba 'SI'.").upper() == "SI": AgregarLibro()
      



def BuscarLibrosPorGenero():
     listaLibrosGeneroSeleccionado = []
     cGeneroSeleccionado = input("Ingrese un genero: ").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").upper()
     for Libro in lista_libros:
          if cGeneroSeleccionado == Libro.genero.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").upper():
               listaLibrosGeneroSeleccionado.append(Libro)
               
     return listaLibrosGeneroSeleccionado

def RecomendarLibro():
     listaDeLibros1 = BuscarLibrosPorGenero()
     listaDeLibros = sorted(listaDeLibros1,key=lambda libro : libro.puntuacion,reverse=True)
     print(f"Segun el genero seleccionado, se recomienda leer el libro: {listaDeLibros[0].titulo}, del autor: {listaDeLibros[0].autor}")

lista_libros = [] 
lista_libros.append(Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5))
lista_libros.append(Libro("1984", "George Orwell", "Ciencia Ficción", 4.3))
lista_libros.append(Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7))
lista_libros.append(Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2))
lista_libros.append(Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4))
lista_libros.append(Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1))
lista_libros.append(Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6))
lista_libros.append(Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8))
lista_libros.append(Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4))
lista_libros.append(Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0))





lIngresoCorrecto = False
lSalir = False

while not lSalir:
     while not lIngresoCorrecto:
          print("Si desea agregar un Libro, digite '1'")
          print("Si desea buscar un Libro por genero, digite '2'")
          print("Si desea una re comendacion de un Libro a partir de un genero, digite '3'")
          print("Si desea salir digite '0'")
          try:
               nOpcionIngresada = int(input(". . ."))
               if nOpcionIngresada in(1,2,3,0):
                    lIngresoCorrecto = True
          except:
               print("No se se ha ingresado un numero correctamete")
     if nOpcionIngresada == 1: AgregarLibro()
     elif nOpcionIngresada == 2:
          listaConLibrosPorGenero = BuscarLibrosPorGenero()
          print("Los titulos para este genero en stock son:")
          for libro in listaConLibrosPorGenero:
               print(f"{libro.titulo} de {libro.autor}")
     elif nOpcionIngresada == 3: RecomendarLibro()
     elif nOpcionIngresada == 0: lSalir = True
     lIngresoCorrecto = False



print("Gracias por venir.")
exit()


