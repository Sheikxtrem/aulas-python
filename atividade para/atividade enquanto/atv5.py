while True:
    num = int(input("Informe um valor entre 1 e 9: "))
    if num >=1 and num <= 9:
        break

while True:
    if num % 2 == 0:
        print(f"{num} x {contador} = {num * contador}")
    else:
        print(f"{num} x {contador} = {num + contador}")
        pass
    contador += 1