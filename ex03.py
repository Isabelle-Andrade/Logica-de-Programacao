'''Crie uma função que receba três números e mostre o maior deles'''

def maior_de_tres(num,numdois,numtres):

    num = int(input("Digite um número: "))
    numdois = int(input("Digite um número: "))
    numtres = int(input("Digite um número: "))

    if num >= numdois and num >= numtres:
        print (num)

    elif numdois >= num and num >= numtres:
        print (numdois)

    else: 
        print(numtres)

maior_de_tres(10,25,7)