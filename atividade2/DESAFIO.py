def calculadora():
    # Solicita a operação que o usuário deseja realizar
    operacao = input("Escolha a operação (soma, subtração, multiplicação, divisão): ").strip().lower()

    # Verifica se a operação é válida
    if operacao not in ["soma", "subtração", "multiplicação", "divisão"]:
        print("Opção inválida. Por favor, escolha uma operação válida.")
        return

    # Solicita os dois números ao usuário
    primeiro_numero = float(input("Informe o primeiro número: "))
    segundo_numero = float(input("Informe o segundo número: "))

    # Realiza a operação escolhida
    if operacao == "soma":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "subtração":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "multiplicação":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "divisão":
        if segundo_numero == 0:
            print("Não é possível dividir por zero.")
            return
        resultado = primeiro_numero / segundo_numero

    # Retorna o resultado
    print(f"O resultado da {operacao} é: {resultado}")

# Chama a função calculadora
calculadora()
