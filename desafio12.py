preco = float(input('informe o preço do produto: '))

desconto = preco * 0.05

precoFinal = preco - desconto

print('O valor do produto é R${:.2f} e com o desconto de 5% sairá por aprenas R${:.2f}'.format(preco, precoFinal))