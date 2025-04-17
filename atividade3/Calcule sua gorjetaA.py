def dolares_para_float(d):

    return float(d.replace('$', ''))
valor = dolares_para_float("$50.00")
print(valor)

