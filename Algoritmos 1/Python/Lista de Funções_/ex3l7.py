def primos_ate_N(n):
    c = 1  
    while c <= n:  
        divisores = 0  
        i = 2  
        while i < c: 
            if c % i == 0:  
                divisores += 1  
            i += 1 
        if c > 1 and divisores == 0:  
            print(c, end=" ")  
        c += 1 
        
n = int(input('Informe o número: '))  
primos_ate_N(n)  
