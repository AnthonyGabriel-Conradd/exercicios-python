def lista_vazia(lista):
    """Retorna True se a lista estiver vazia, False caso contrário."""
    return len(lista) == 0

if __name__ == "__main__":
    print(lista_vazia([]))
    print(lista_vazia([1, 2, 3]))
