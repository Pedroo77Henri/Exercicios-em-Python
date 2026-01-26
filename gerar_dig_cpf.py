cpf = '74682489070'
dez_digitos = cpf[:10]
contador_regressivo2 = 11

resultado_digito2 = 0
for digito_2 in dez_digitos:
    resultado_digito2 += int(digito_2) * contador_regressivo2
    contador_regressivo2 -= 1
digito2 = (resultado_digito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0 
print(digito2)
