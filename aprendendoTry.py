def validar():
    while True:
        try:
            while True:
                num = int (input("Digite o numero: "))
                while num < 0:
                    num = int(input("Numero invalido. Digite novamente: "))
                return num
        except:
            print ("Nao li um inteiro.")

def main ():
    num = validar()
    print (num)
    
main()