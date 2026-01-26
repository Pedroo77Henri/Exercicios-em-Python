palavra = input('Escreva uma palavra: ')
quant_vogais = ''
vogais = 'aeiou'
for letra in palavra:
    if letra in vogais:
        quant_vogais += letra
if quant_vogais == '':
    print('A palavra não tem vogais')
else:
    numero = len(quant_vogais)
    vogais_formatadas = ', '.join(quant_vogais)
    print(f'A palavra {palavra} tem {numero} vogais: "{vogais_formatadas}"')
