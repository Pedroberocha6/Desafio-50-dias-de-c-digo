def validarInt():
    while True:
        try:
            num = int (input("> "))
            if num < 1:
                    print("Numero invalido. Digite novamente: ")
            else:
                return num
        except:
            print ("Nao li um inteiro. Digite novamente: ")

def validarFloat():
    while True:
        try:
            num = float (input("> "))
            return num
        except:
            print ("Nao li um valor valido. Digite novamente: ")

def receber (lista):
    
    print ("Digite a quantidade de numeros que deseja adicionar a lista: ")
    qntd = validarInt()
    cont = 0
    while cont < qntd:
        print ("Digite para adicionar a lista: ")
        num = validarFloat()
        lista.append(num)
        print (f"Numero {num} adicionado.")
        cont += 1

def soma (lista):
    
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def tirarMedia(s , lista):
    media = s/len(lista)
    return media

def definirMaior(lista):
    maior = lista[0]
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
    media = tirarMedia(somatorio,listaNum)
    maior = definirMaior(listaNum)
    menor = definirMenor(listaNum)
    
    print (f"O maior numero da lista {maior}")
    print (f"O menor numero da lista {menor}")
    print (f"A media entre os numeros {media}")
    print (f"A soma de todos {somatorio}")
    
main()