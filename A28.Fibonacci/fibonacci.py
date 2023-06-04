def fibonacci(numero):
    sequencia = [0, 1]

    while sequencia[-1] < numero:
        sequencia.append(sequencia[-1] + sequencia[-2])

    return sequencia

numero = int(input("Digite um número: "))

sequencia_fibonacci = fibonacci(numero)
print(f"A sequência de Fibonacci até {numero} é: {sequencia_fibonacci}")



