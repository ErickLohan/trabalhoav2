""" Questão 1 """
def calcular_area(basemenor, basemaior, h):
    resultado = (basemenor + basemaior) * h/2
    print(resultado)

basemaior = float(input('Insira o valor da base maior:'))
basemenor = float(input('Insira o valor da base menor:'))
h = float(input('Insira o valor da altura:'))
calcular_area(basemenor, basemaior, h)