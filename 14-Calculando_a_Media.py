def calcular_media(lista):
    """Retorna a média aritmética dos valores da lista."""
    return sum(lista) / len(lista) if lista else 0

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    print(calcular_media(numeros))
