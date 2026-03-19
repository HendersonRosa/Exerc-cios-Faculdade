#Fiz esse código pra relembrar de alguns conceitos básicos, fui tentando aumentar a dificuldade até ficar satisfeito com o código e não notar mais possíveis melhorias. A ideia era um código que verificasse se a pessoa era maior de idade ou não (Usei como contexto carteira de motorista).

while True:
    autenticador = input(
        "Para rodar verificador digite S, caso não queira digite N: "
    ).upper()

    if autenticador == "S":
        try:
            idade = int(input("Insira sua idade: "))

            if 1 <= idade < 120:
                if idade < 18:
                    print("Não pode dirigir")
                else:
                    print("Pode dirigir")
                break
            else:
                print("Para de mentir")

        except ValueError:
            print("Insira sua idade em número")

    elif autenticador == "N":
        break
    else:
        print("Digite um código válido")