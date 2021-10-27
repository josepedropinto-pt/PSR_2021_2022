

def isPerfect(value):
    print('\n Vamos confirmar se o número' + " " +
          str(value) + " " + 'é perfect...')
    soma=0
    for div in range(1, (value)):
        if value % div == 0 :
          soma +=div

    if soma==value:
        return True
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
                  'Ora bolas, o ' + str(i) + ' não é perfeito'
                  +Style.RESET_ALL)