def comentar_idade():
    idade_input = input("Informe sua idade: ")

    try:
        idade = int(idade_input)  # Tenta converter a entrada para um inteiro
        if idade < 0:
            return "Valor informado é inválido."  # Idade não pode ser negativa
        elif idade < 18:
            return "Você é menor de idade."
        elif 18 <= idade < 60:
            return "Você é adulto."
        else:
            return "Você é idoso."
    except ValueError:
        return "Valor informado é inválido."  # Tratamento para valor não numérico

# Chama a função e imprime o resultado
resultado = comentar_idade()
print(resultado)
