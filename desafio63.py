n = int(input('Digite quantos termos deseja que sejam mostrados na sequência de Fibonacci'))
total = 0
n1 = 1
n2 = 0
c = 0
if n == 0 or n ==1:
    print(0)
else:
    while c < n:

        total = n1 + n2
        n1 = n2
        n2 = total
        c = c + 1
    print(total)