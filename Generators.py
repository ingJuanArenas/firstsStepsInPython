

def generator1(init, limit):
    for i in range(init,limit):
        yield i

for value in generator1(1,10):
    print(value , "=====")

gen= (x for x in range(1,10))
print(list(gen))

def generator2(n):
    for i in range(n):
        if i%2 ==  0:
            yield i


for v in generator2(10):
    print(v, "//////")


genvaluespair= (x for x in range(10) if x%2==0)
print(list(genvaluespair))


def genWords(words: list[str]):
    for word in words:
        if len(word) >= 5:
            yield word

palabras = ["hola", "programación", "python", "sol", "decoradores"]
for w in genWords(palabras):
    print(w)

genWordsl= (x for x in palabras if len(x) >= 5)
print(list(genWordsl))



def genSend():
    while True:
        num= yield
        print("Entró ", num)

nums= genSend()
next(nums)

for i in range(1,10):
    nums.send(i)



def genPlus():
    total = 1
    while True:
        value= yield total
        if value is None:
           break
        total *=value

nums= genPlus()
print(next(nums))


for i in range(1,20,4):
   print(nums.send(i))