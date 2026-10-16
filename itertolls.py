from itertools import combinations, permutations, product

pessoas = ['Joao','Fernanda','Jose','Maria']
camiseta = ['preta','branca'],['p','m','g']

def print_pessoa(itertols):
    print (*list(itertols), sep='\n')
    print()
    
print_pessoa(combinations (pessoas, 2))
#print_pessoa(permutations (pessoas, 2))
#print_pessoa(product (*camiseta))