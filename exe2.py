#validaçã do nome
while True:
    nome = input("Digite seu nome: ")

    if len(nome) >= 3:
        break
    else:
        print ("Erro: É obrigatório que o nome tenha mais de 3 caracteres, tente novamente! \n")
    
#validação de idade
while True:
    idade = int(input("Digite sua idade(entre 0 e 150): "))

    if 0 <= idade <= 150:
        break
    else: 
        print("Erro: A idade deve ser entre 0 e 150.")

#validação de salário
while True:
    salario = float (input("Digite seu salário: "))

    if salario > 0: 
        break
    else:
        print("Erro: o salário deve ser maior que zero!")

#validação de genêro
while True:
    genero = input ("Digite seu gênero: ('F' para feminino, 'M' para masculino, 'O' para outros)").upper()
    if genero in ['F', 'M', 'O']:
        break
    else: 
        print("Erro: Você deve colocar 'F', 'M', 'O'.")

#validação de estado civil
while True: 
    estado_civil = input("Digite 'S' para solteiro, 'C' para casado, 'D' para divorciado e 'V' para viúvo. ").lower()
    if estado_civil in ['S','C', 'V', 'D']:
        break
    else:
        print("Erro: Estado civil inválido!")

print("Informações completas: ")
print(f"Nome: {nome}")
print(f"Idade: {nome}")
print(f"Salário: {nome}.")

if genero == "F":
    print ("Genêro: Feminino")

elif genero == "M":
    print ("Genêro: Masculino")

else:
    print("Genêro: Outro")   


if estado_civil == "S":
    print("Estado civil: Solteiro(a).")

elif estado_civil == "C":
    print("Estado civil: Casado(a).")

elif estado_civil == "D":
    print("Estado civil: Divorciado(a).")
     
else:
    print("Estado civil: Viúvo(a).")
    
     


