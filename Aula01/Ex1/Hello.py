#!/usr/bin/env python3

# Criar função Def Nomefunção (Inputs)
def print_hi(name):
    #definir o que vai a função fazer, print escreve na consola "Hi" colocar variavel constante e +name variavel dinamica
    print("Hi," + name)

#quando não há inputs colocar apenas os paranteses e os :
alunos=['joao', 'manel', 'rui', 'carlos']
for idx in range(0, len(alunos)):
    def boas_vindas():
     print("Bem vindo a PSR," + "\n" +  alunos[idx])


lista = ['paula', 'luisa', 'mariana', 'rute']
for aluno in lista:
    def cumprimento():
        print("olá querida" + " " + aluno)
    #Colocar sempre que queremos correr algumas função desta forma

#for x in range(0, 10):     #correr várias vezes o comando
    if __name__ == '__main__':
        print_hi('José Pedro')  #utilizar a variavel "x" convertido em string
        boas_vindas()
        cumprimento()
#ativar permissões: chmod 777 Hello.py


