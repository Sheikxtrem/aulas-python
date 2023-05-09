import os#importando biblioteca para trabalhar com sistema operacional
dentroIntervalo = 0
foraIntervalo = 0
contador = 1

os.system("cls")#irá limpar a tela
while contador <= 5:
    valor = int(input("informe um valor qualquer: "))
    if valor >= 10 and valor <= 20:
        dentrointervalo += 1
    else:
        foraIntervalo += 1
    contador += 1
    
print(f"Valores dentro do intervalo: {dentroIntervalo}")
print(f"Valores fora do intervalo: {foraIntervalo}")

    