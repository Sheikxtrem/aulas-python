texto= "Técnico em Desenvolvimento de Sistemas"
print ("*******Título*******")
print("*"*10)
print(texto)

idade = int(input("Informe sua idade: "))
print("# "*idade)

#Manipulando textos (String)
print(f"O total de letras é",{len(texto)})#len() vem de length, que significa total

print(texto.upper())#upper()coloca todo texto em maiúsculo
print(texto.capitalize())# coloca a 1º letra em maiúsculo

print(texto.replace("sistemas","web"))#replace troca um texto por outro

#TRABALHANDO COM FATIAMENTO

print("Fatiando variável texto")
print(texto[:3])#Vai exibir todo o texto até a posição 2, no caso a posição 3 não conta.

print(texto[3:])#Vai exibir todo o texto a partit da posição 3
print(texto[3:10])#Vai exibir todo o texto que está na posição 3 até 10