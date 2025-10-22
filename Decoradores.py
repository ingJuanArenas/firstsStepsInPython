import time
def decorator(func):
    def wrapper (a,b):
        print("Ingreso al wrapper  y ejecuto")
        c = func(a,b)
        print("retorno el valor")
        return c
    return wrapper

@decorator
def sum(a,b):
    return a+b

def decoratortime(func):
    def wrapper(name):
        inicio= time.time()
        s= func(name)
        print(s)
        return f"La tarea {func.__name__} tardó {time.time()- inicio} scs"
    return wrapper


@decoratortime
def process(name):
    time.sleep(3)
    return f"Hello {name}"


def counterDecorator(func):
    contador = 0
    def wrapper(name):
        nonlocal contador
        contador+=1
        print("Llamada: " ,contador )
        return func(name)
    return wrapper


@counterDecorator
def counter(name):
    print(f"hello, {name}")


def entrarAOficina(role):
    def decorador(func):
        def wrapper():
            func()
            if role == "Admin":
                return  saludarAdmin()
            else:
                return negar()
        return wrapper
    return decorador


def saludarAdmin():
    print("Bienvenido admin, login exitoso")

def negar():
    print("Acceso denegado..")

@entrarAOficina("Admin")
def entrarComoAdmin():
    print("Estoy entrando como admin")

@entrarAOficina("User")
def entrarComoUser():
    print("Entrando como user")


print(sum(5,10))
print("=======================")
print(process("Joel"))
print("=======================")
counter("Pedro")
counter("Manuel")
print("=======================")
entrarComoAdmin()
print("=======================")
entrarComoUser()
print("=======================")