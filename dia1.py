def validar(x):
    while x < 0:
        x = int (input("Numero invalido. Digite novamente: "))
    return x

def receber (lista):
    
    qntd = int (input("Quantos numeros deseja adicionar na lista? "))
    if qntd < 0:
        qntd = validar(qntd)

    cont = 0
    while cont < qntd:
        num = float (input("Digite para adicionar a lista: "))
        lista.append(num)
        cont += 1

def soma (lista):
    
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def mediana(s , lista):
    media = s/len(lista)
    return media

def definirMaior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

def definirMenor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def main():
    
    listaNum = []
    receber (listaNum)
    somatorio = soma (listaNum)
    media = mediana(somatorio,listaNum)
    maior = definirMaior(listaNum)
    menor = definirMenor(listaNum)
    
    print (f"O maior numero da lista {maior}")
    print (f"O menor numero da lista {menor}")
    print (f"A media entre os numeros {media}")
    print (f"A soma de todos {somatorio}")
    
main()