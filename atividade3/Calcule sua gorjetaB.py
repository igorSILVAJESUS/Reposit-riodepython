def dolares_para_float(d):

    return float(d.replace('$', ''))

def percentual_para_float(p):

    return float(p.replace('%', '')) / 100

valor_em_dolares = dolares_para_float("$10.50")
percentual = percentual_para_float("15%")

print(f"Valor em dólares: {valor_em_dolares}")
print(f"Percentual: {percentual}")


