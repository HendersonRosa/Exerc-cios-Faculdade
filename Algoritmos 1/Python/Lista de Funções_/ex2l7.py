def eh_primo(n):
    if n <= 1:
        print('número não é primo')
        return
    elif n == 2:
        print('número é primo')
        return
    elif n % 2 == 0:
        print('número não é primo')
        return
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            print('número não é primo')
            return
        i += 2
    
    print('número é primo')

n = int(input('Informe o número: '))
eh_primo(n)
