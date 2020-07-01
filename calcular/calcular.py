#########################################################
#Código de baixa qualidade escrito por Pedro dos santos #
#Pedro.dos.santos1997@gmail.com                         #
#São paulo, SP, 29 de junho de 2020                     #
#########################################################
from sys import argv
try:
#Procura os comandos digitados e adiciona a lista
    comandos = []

    for argumentos in argv:
        comandos.append(argumentos)

#faz os calculos
    if comandos[2] == '+':
        contar1 = int(comandos[1])
        contar2 = int(comandos[3])
        print(contar1+contar2)

    if comandos[2] == '-':
        contar1 = int(comandos[1])
        contar2 = int(comandos[3])
        print(contar1-contar2)

    if comandos[2] == '.':
        contar1 = int(comandos[1])
        contar2 = int(comandos[3])
        print(contar1*contar2)

    if comandos[2] == '/':
        contar1 = int(comandos[1])
        contar2 = int(comandos[3])
        print(contar1/contar2)
except:
#comandos adicionais
    if comandos[1] == '-h':
        print('''Aplicativo simples de calculadora escrita em Python 3
A sintaxe de calculos é simples, você vai digitar:
calcular [numero] [operador] [numero]
os operadores são + para adição, - para subtração . para multiplicação e / para divisão.
exemplo: calcular 2 + 2''')
    elif len(comandos) < 4:
        print('falta de argumentos: verifique a opção help com "calcular -h"')

#foi mal aê véi
#sorry about that
