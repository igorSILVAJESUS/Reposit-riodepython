def verificar_par_impar():
    valor = input("Informe um número: ")

    try:
        numero = int(valor)  # Tenta converter o valor para um inteiro
        if numero % 2 == 0:
            return True  # Número é par
        else:
            return False  # Número é ímpar
    except ValueError:
        return "Valor informado é inválido"  # Tratamento para valor não inteiro

# Chama a função e imprime o resultado
resultado = verificar_par_impar()
print(resultado)
