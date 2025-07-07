'''Crie uma função que calcule a área de um retângulo'''

def area(base,altura):

    base = int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))

    multiplicacao = base * altura

    print(f"A área do retângulo é: ", multiplicacao)

area()