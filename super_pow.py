def superPow(a, b):
    # Função auxiliar para calcular a^b mod m
    def pow_mod(a, b, m):
        result = 1
        a %= m

        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            b //= 2

        return result

    result = 1
    m = 1337

    # Aplica a propriedade de divisão e conquista
    for digit in b:
        result = (pow_mod(result, 10, m) * pow_mod(a, digit, m)) % m

    return result

# Exemplos de uso:
print(superPow(2, [3]))       # Saída: 8
print(superPow(2, [1, 0]))    # Saída: 1024
print(superPow(1, [4, 3, 3, 8, 5, 2]))  # Saída: 1
