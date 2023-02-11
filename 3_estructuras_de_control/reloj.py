seg = 0
minutos = 0
horas = 0
bandera = True
print(f"{horas%24}:{minutos%60}")
while(horas<=30):
    seg+=1
    print(seg % 60)
    print("",end="")
    if (seg % 60 == 0):
        print(minutos)
        minutos+=1
        bandera = True
    if(minutos!=0 and minutos%60==0):
        horas+=1
        bandera=True
    # if(bandera):
    #     print(f"{horas%24}:{minutos%60}")
        # print(f"{horas%24} aqui ")
    bandera = False