#import random
from random import randint
import osos.system("cls")

os system("cls")
sorteio = []# criando uma lista vazia

for contador in range(1,11):
    sorteio.append(randit(1,100))# gerando valores aleatórios e salvando na lista
    
#valor = randit(1,100)# essa função irá gerar um número aleatório entre 1 e 100
print(sorteio)
print(sorteio.sort(reverse=True))# a função sort() ordena de forma crescente. O parâmetro reverse=True, faz o contrário, ordena de forma decrescente
print(sorteio)
os.system("pause")#irá pausar o sistema até  uma tecla ser pressionada
