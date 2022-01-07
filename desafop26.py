from unidecode import unidecode
frasea = input('digite uma frase: ').strip()
frase = frasea.casefold() #.casefold() == lower() // transforma as letras para minúsculas
frase = unidecode(frase)
print('A frase tem {} caracteres'.format(len(frase)))
print('A letra "A", aparecem {} vezes'.format(frase.count('a')))
print('A letra "A", aparece pela primeira vez na posição {} '.format(frase.find('a')))
print('A letra "A", aparece pela última vez na posição {} '.format(frase.rfind('a')))
#em que posição aparece a primeira vez
#em que posição aparece a ultima vez
#na frase a letra A aparecem n vezes que eu não sei dizer, mas que o programa me contará