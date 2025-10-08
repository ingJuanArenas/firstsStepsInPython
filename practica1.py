lista = ["Juan", "Arenas", "SWE", 19, 1.76]
tupla = ("Pepe", "Manchas", "Pupi")
setex = {"AGM", "AL", "I5","POO2", "E2","BS2"}
dictex={
    "mom":{
        "name":"alcira",
        "age":54,
        "city": "cucuta"
    },
    "sister":{
        "name":"Pilar",
        "age":21,
        "city": "cucuta"
    },
    "brother":{
        "name":"jan",
        "age":29,
        "city": "cucuta"
    }
}
family = {"mom": dictex["mom"], "sister": dictex["sister"], "brother": dictex["brother"]}


def mostrarFamilia():
    for n,v in family.items():
        print(n,v)


def mostrarUno(*member):
    print(dictex.get(member))

def agregar(role,name,age,city):
    family.update({
        role:{
            "name": name,
            "age": age,
            "city": city
        }
    })
    mostrarFamilia()
def remove(role):
    family.pop(role)
    mostrarFamilia()

mostrarFamilia()
mostrarUno("mom", "brother")
mostrarUno()
agregar("tio", "juan", 50, "cucutilla")
remove("sister")