"""Questão 3"""
def converter(horario, minutos):
    if horario >= 12:
        horario = horario-12
    else:
        horario = horario


def saida(horario, minutos, notacao):
    if horario > 12:
        horario = horario-12
    elif horario == 0:
        horario+12
    else:
        horario = horario

    if notacao == ('P.M.'):
        print(f'O horário convertido é: {horario}:{minutos} {notacao}')
    else:
        print(f'O horário convertido é: {horario}:{minutos} {notacao}')


while True:
    comecar = int(input('Ditite 1 para começar ou 0 para sair: '))
    if comecar == 1:
        hora = int(input('Digite as horas: '))
        minuto = int(input('Digite os minutos: '))

        if hora == 00:
            hora = hora+12
            passarnotacao = ('A.M')

        elif hora >= 12:
            passarnotacao = ('P.M')

        else:
            passarnotacao = ('A.M')
        converter(hora, minuto)
        saida(hora, minuto, passarnotacao)

    if comecar == 0:
        print('Você saiu!')
        break