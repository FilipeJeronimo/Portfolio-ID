import random
#tarefa 1
#Ex 1
num1 = float(input("Introduz um numero: "))
num2 = float(input("Introduz outro numero: "))

print("Resultado: ", num1 + num2)

#Ex 2
num3 = float(input("Introduz o um número: "))
num4 = float(input("Introduz o outro número: "))

if num3 > num4:
    print(f"O maior número é: {num1}")
elif num4 > num3:
    print(f"O maior número é: {num2}")
else:
    print("Os dois números são iguais.")

#Ex 3
num5=random.randint(1,6)

#Ex 4
lancar = "s"
while lancar != "n":
    lancar = input("Deseja lançar o dado? (s/n): ")
    if lancar != "n":
        num6 = random.randint(1, 6)
        print("Dado lançado:", num6)
print("Terminado")

#tarefa 2
#ex 1
num5 = int(input("Introduz um número: "))
num6 = int(input("Introduz outro número: "))

if num6 == 0:
    invalido = "Não é possivel dividir por 0"
else:
    invalido = num5 / num6
print("Resultado: \n\tSoma = ", int(num5+num6),"\n\tSubtração = ", int(num5-num6),"\n\tMultiplicação = ", float(num5*num6), "\n\tDivisão = ",invalido)

#ex 2
num7 = float(input("Introduz um número: "))
for i in range(10):
    print(num7,"x",i,"=",num7*i)

#ex 3
num8 = float(input("Introduz um número: "))
num9 = int(input("Introduz o primeiro número: "))
num10 = int(input("Introduz o último numero: "))
for i in range(num9, num10+1):
    print(num8,"x",i,"=",num8*i)

#ex 4
print(f"Dado Lançado: {random.randint(1,6)}")

#ex 5
continuar = "s"
while continuar != "n":
    print(f"Dado Lançado: {random.randint(1, 6)}")
    continuar = input("Deseja continuar? (s/n): ")

#ex 6
continuar = "n"
while continuar != "s":
    continuar = input("Quantos dados(1,2, s -sair)? ")
    if continuar == "1":
        print(random.randint(1, 6))
    if continuar == "2":
        num11 = random.randint(1, 6)
        num12 = random.randint(1, 6)
        print(num11," ", num12 , "Total: ",int(num11+num12))

#ex 7
# a diferença entre os dois é que no randrange o segundo número não é incluso na variável dai ser ás vezes necessário ser feito randrange(num,num1+1)

#ex8
num13 = random.randint(1,10)
guess = int(0)
while guess != num13:
    guess = int(input("Introduza um número de 1 a 10: "))
    if guess == num13:
        print("“PARABÉNS!! Acertaste no número!")
    else:
        print("Tenta Outra vez!")

#ex 9
num13 = random.randint(1,10)
guess = int(0)
for i in range(3):
    guess = int(input("Introduza um número de 1 a 10: "))
    if guess == num13:
        print("“PARABÉNS!! Acertaste no número!")
    else:
        print("Tenta Outra vez!")

print("Que pena! Não foi desta. Tenta outra vez!")

#ex 10
rand1 = int(input("Introzuda o número inicial do random: "))
rand2 = int(input("Introduza o segundo número e final do random: "))
tentativas = int(input("Introduza a quantidade de tentativas: "))

num13 = random.randint(rand1,rand2)
guess = int(0)
for i in range(tentativas):
    guess = int(input(f"Introduza um número de {rand1} a {rand2}: "))
    if guess == num13:
        print("“PARABÉNS!! Acertaste no número!")
    else:
        print("Tenta Outra vez!")

print("Que pena! Não foi desta. Tenta outra vez!")

#ex 11
def bom_dia():
    print("Bom dia!")
bom_dia()

#ex 12
def bom_dia():
    print("Bom dia!")
def boa_tarde():
    print("Boa tarde!")
def boa_noite():
    print("Boa noite!")

hora = int(input("Introduza uma hora: "))
if hora < 10:
    bom_dia()
elif hora < 18:
    boa_tarde()
elif hora < 24:
    boa_noite()

#ex 13
def boa_vindas(hora):
    if hora < 10:
        print("Boa dia!")
    elif hora < 18:
        print("Boa tarde!")
    elif hora < 24:
        print("Boa noite!")

hora = int(input("Introduza uma hora: "))
boa_vindas(hora)

#ex 14
#resultado que acho 1 5 1, e depois de executar foi isso que deu
def exemplo():
 n = 5
 print(n)

n = 1
print(n)
exemplo()
print(n)

#ex 15
#resultado que acho 1 5 5, porque a palavra reservada faz com que o "n" seja substituido porque está a ser chamado depois de imprimir o 1º "n", e foi isso que deu
def exemplo():
 global n
 n = 5
 print(n)

n = 1
print(n)
exemplo()
print(n)

#ex 16
def tabuada(numero):
    for i in range(11):
        print(numero,"x",i,"=",numero*i)

tabuada_num = int(input("Introduza um número para apresentar a tabuada: "))
tabuada(tabuada_num)