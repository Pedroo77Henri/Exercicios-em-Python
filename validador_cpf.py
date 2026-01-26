import re
cpf = input('Digite o seu CPF: ')
cpf_limpo = re.sub(r'[^0-9]', '', cpf)
if len(cpf_limpo) != 11:
    print('CPF invalido')
    exit()
if cpf_limpo == cpf_limpo[0] * len(cpf_limpo):
    print('Invalido, é sequencial. ')
    exit()
calculo_digito_um = cpf_limpo[:9]
contador_regressivo_1 = 10
resultado_digito_um = 0 

for digito in calculo_digito_um:
    resultado_digito_um += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito1 = (resultado_digito_um * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0


calculo_digito_dois = calculo_digito_um + str (digito1)
contador_regressivo_2 = 11
resultado_digito_dois = 0

for digito2 in calculo_digito_dois:
    resultado_digito_dois += int(digito2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_dois = (resultado_digito_dois * 10) % 11
digito_dois = digito_dois if digito_dois <= 9 else 0


if digito1 == int(cpf_limpo[9]) and digito_dois == int(cpf_limpo[10]):
    print(f'CPF {cpf} valido')
else:
    print('CPF invalido')

