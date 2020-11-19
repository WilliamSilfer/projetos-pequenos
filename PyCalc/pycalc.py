escolha = 1
while escolha != 0:

    # Inicialização
    choisen = input("""Bem-Vindo, Use a PyCalc como queira!!\n
Faça sua escolha de operação de acordo.
    Soma = " + " 
    Subtração = " - "
    Multiplicação = " * " 
    Divisão = "/"
    Potênciação = "**" 
    Mod/Resto = "%" """)

    vlr1 = int(input("Valor 1: "))
    vlr2 = int(input("\nValor2: "))

# Funções da escolha
    if choisen == '+':
        def soma(x, y):
            return x + y
        print(f'\n{vlr1} + {vlr2} = ', soma(vlr1, vlr2))

    elif choisen == '-':
        def sub(x, y):
            return x - y
        print(f'\n{vlr1} - {vlr2} = ', sub(vlr1, vlr2))

    elif choisen == '*':
        def multi(x, y):
            return x * y
        print(f'\n{vlr1} * {vlr2} = ', multi(vlr1, vlr2))

    elif choisen == '/':
        def div(x, y):
            return x / y
        print(f'\n{vlr1} / {vlr2} = ', div(vlr1, vlr2))

    elif choisen == '**':
        def pot(x, y):
            return x ** y
        print(f'\n{vlr1} ** {vlr2} = ', pot(vlr1, vlr2))

    elif choisen == '%':
        def rest(x, y):
            return x % y
        print(f'\n{vlr1} % {vlr2} = ', rest(vlr1, vlr2))
    else:
        print("Resposta inexistente. O programa será encerrado!!")
        break

    print("\n 1 = Continuar, 0 = Sair")
    escolha = input()
