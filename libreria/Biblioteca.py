from typing import Dict

books : list[dict] = list()
salir= False

def showMenu():
    print(""" 
    1. agregar libros
    2. mostrar libros 
    3. buscar libros por nombre
    4. buscar libros por genero
    5. buscar libros por año
    6. buscar por numero de paginas
    7. actualizar estado libro
    8. eliminar libro
    9. estadisticas lector
    """)


def basicStats(dataToStats: dict[str,int]):
    n= len(books)
    moda:list[dict]= list()
    maxFreq= 0
    for k,v in dataToStats.items():
        promedi = (v/n)*100
        print(f"{k} tiene: {promedi:.2f} %")
        if v>maxFreq:
            maxFreq=v
            moda=[{k:v}]
        elif v==maxFreq:
            moda.append({k:v})
    print("La moda es: ", maxFreq)
    print(moda)

    

def groupCategories():
    categoryToStats = input("Ingrese la categoria: Genre/Status/#Pages")
    items:Dict[str, int]= {}
    for x in books:
        for k,vobj in x.items():
            bookData:dict = vobj
            value:str= str(bookData.get(categoryToStats))
            if value not in items:
                items[value]=1
            else:
                items[value] +=1
    print(items)
    return items
                
def deleteBook():
    global books
    bookToDelete= getDataToSearch()
    copy = books.copy()
    for x in copy:
        if bookToDelete in x:
            copy.remove(x)
            print("eliminado exitosamente.")
            break
    else: 
        print("No se ha encontrado nada con ese nombre")
    books = copy

def updateBookStatus():
    name= input("Ingrese el nombre del libro: ")
    status= input("Ingrese el estado (leyendo/finalizado): ")
    bookToUpdate= dict()
    for x in books:
        if name in x:
            bookToUpdate = x
            bookToUpdate["Status"]= status
            print(bookToUpdate)
            break
    else:
        print("No se ha encontrado nada")
    

def addBooks() -> None:
    """Agrega libros a la lista con validación completa."""
    quantity: int = int(input("Cantidad de libros a ingresar: "))
    i: int = 0
    
    while i < quantity:
        print(f"\n--- Libro {i + 1} de {quantity} ---")
        title: str = input("Título: ")
        author: str = input("Autor: ")
        year: int = int(input("Año: "))
        nPages: int = int(input("# de páginas: "))
        
        while year < 1700 or year>2025 or nPages <= 0:
            print("❌ Datos inválidos. El año debe ser entre 1700 y 2025 y las páginas > 0")
            print("Intente nuevamente.")
            year = int(input("Año: "))
            nPages = int(input("# de páginas: "))
        
        genre: str = input("Género: ")
        bookToAdd= {
            title: {
                "Author": author,
                "Year": year,
                "#Pages": nPages,
                "Genre": genre,
                "Status": "PorLeer"
            }
        }
        
        books.append(bookToAdd)
        print("✅ Libro agregado correctamente.")
        i += 1
    
    print(f"\n🎉 Se agregaron {quantity} libro(s) exitosamente.")

def showAll()-> None:
    for x in books:
        print(x)

def getDataToSearch()-> str:
    infoTo = input("Ingrese el dato a buscar: ")
    return infoTo
def searchByName()->list:
    nameToSearch = getDataToSearch()
    booksFound:list = list()
    for x in books:
        if nameToSearch in x.keys():
            booksFound.append(x)
    
    return booksFound
    

def searchBy(field:str):
    """Busca libros que contengan el dato especificado."""
    booksFound= []
    data_lower = getDataToSearch().lower()
    
    for x in books:  # 1er for: cada libro (que es un dict)
        for title, book_data in x.items():  # 2do for: obtener título y datos
            value: str = str(book_data.get(field, ""))
            if data_lower in value.lower():
                booksFound.append(x)
    return booksFound

def printValues(listToPrint:list)-> None:
    for x in listToPrint:
        print(x)


    
while salir != True:
    showMenu()
    op= int(input("Ingrese la opcion: "))
    match op:
        case 1: addBooks()
        case 2: showAll()
        case 3: 
            values = searchByName()
            printValues(values)
        case 4: 
            values = searchBy("Genre")
            printValues(values)
        case 5: 
            values = searchBy("Year")
            printValues(values)
        case 6: 
            values = searchBy("#Pages")
            printValues(values)
        case 7:
            updateBookStatus()
        case 8:
            deleteBook()
        case 9:
            data= groupCategories()
            basicStats(data)
        case 0: salir = True
        case _: print("Opcion invalida")
    

        

