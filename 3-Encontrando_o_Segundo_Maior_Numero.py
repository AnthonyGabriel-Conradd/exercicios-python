def segundo_maior(lista):
    """Retorna o segundo maior número (considerando valores repetidos)."""
    return sorted(set(lista))[-2] if len(set(lista)) >= 2 else None

if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    print(segundo_maior(numeros))
