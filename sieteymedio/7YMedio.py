import random as r
cartas =[
    ("As oros",1),
    ("2 oros",2),
    ("3 oros",3),
    ("4 oros",4),
    ("5 oros",5),
    ("6 oros",6),
    ("7 oros",7),
    ("10 oros",0.5),
    ("11 oros",0.5),
    ("12 oros",0.5),
    ("As espadas",1),
    ("2 espadas",2),
    ("3 espadas",3),
    ("4 espadas",4),
    ("5 espadas",5),
    ("6 espadas",6),
    ("7 espadas",7),
    ("10 espadas",0.5),
    ("11 espadas",0.5),
    ("12 espadas",0.5),
    ("As copas",1),
    ("2 copas",2),
    ("3 copas",3),
    ("4 copas",4),
    ("5 copas",5),
    ("6 copas",6),
    ("7 copas",7),
    ("10 copas",0.5),
    ("11 copas",0.5),
    ("12 copas",0.5),
    ("As bastos",1),
    ("2 bastos",2),
    ("3 bastos",3),
    ("4 bastos",4),
    ("5 bastos",5),
    ("6 bastos",6),
    ("7 bastos",7),
    ("10 bastos",0.5),
    ("11 bastos",0.5),
    ("12 bastos",0.5)
    ]
cartas_b=[]
for carta in range(len(cartas)):
    cartas_b.append(cartas.pop(r.randint(0,len(cartas)-1)))
print (cartas_b)
#Repartir Cartas
puntosj1=0; puntosj2=0
j1=[]
j2=[]
j1.append(cartas_b.pop())
j2.append(cartas_b.pop())
print(f"J1: {j1}")
print(f"J2: {j2})")

while True:
    respuesta=input("J1:Quieres más cartas?")
    if respuesta=="si":
        j1.append(cartas_b.pop())
    else:
        break
    print(j1)
    
while True: #Se pone true para hacer el Do While 
    respuesta=input("J2:Quieres más cartas?")
    if respuesta=="si":
        j2.append(cartas_b.pop()) #se pone cartas 
        
    else:
        break
    print(j2)

#Contar puntos
for carta in j1:
    puntosj1 += carta[1]
for carta in j2:
    puntosj2 += carta[1]
b_j1=puntosj1 <= 7.5
b_j2=puntosj2 <= 7.5
if (b_j1 and b_j2):
    ganador="J1" if puntosj1 > puntosj2 else "J2"
elif(b_j1 or b_j2):
    ganador="J1" if b_j1 else "J2"
else: 
    ganador="empate"
print(ganador)