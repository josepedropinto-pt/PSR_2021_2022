#!/usr/bin/env python3
#This is just a testing for building documentation
#José Pedro Pinto 2021
#Programação Sistemas Robóticos
maximum_number = 10


from colorama import Fore, Style
#Importa o foreground color e style para personalizar saídas

def isPerfect(value):
    print('\n Vamos confirmar se o número' + " " +
          str(value) + " " + 'é perfect...')
    soma=0 #Iniciar a variavel soma a zero
    for div in range(1, value): # Percorrer nº até ao valor em analise
        if value % div == 0 :
          soma +=div #se for divisor somamos à variavel "soma"

    if soma==value:  # Se a soma for igual ao valor em analise
        return True  #então return true porque é perfeito!
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print(Fore.GREEN + Style.BRIGHT+
            'Number ' + str(i) + ' is perfect.'+Style.RESET_ALL)

        else:
            print(Fore.RED + Style.BRIGHT +
                  'Ora bolas, o ' + str(i) + ' não é perfeito'+Style.RESET_ALL)

if __name__ == "__main__":
    main()

    #pydoc -w ./ cria a documentação HTML