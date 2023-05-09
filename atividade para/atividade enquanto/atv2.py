maior = 0
while True:
    num = int(input("Informe um valor: "))
    if num >= maior:
        maior = num
    if num == 0:
        break
printf(f"O maior valor digitador foi {maior}\n") 