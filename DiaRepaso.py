# Sorteo para 5 personas, 
# hay 3 premios 
# OJO: una persona no puede ganar 2 veces

from random import randint

cant_part = input("Cuantos participantes tendra el sorteo?")
print("")
cant_premios = input("Cuantos ppremios habra?")
print("")

lista_ganadores = [""]
len(lista_ganadores)
for i in range(6):

ganador1 = randint(0, 4)
ganador2 = randint(0, 4)
ganador3 = randint(0, 4)

while ganador2 == ganador1:
    ganador2 = randint(0, 4)
while ganador3 == ganador1 or ganador3 == ganador2:
    ganador3 = randint(0, 4)

print("Ganador 1:", partic[ganador1])
print("Ganador 2:", partic[ganador2])
print("Ganador 3:", partic[ganador3])