def juntar_listas(lista1, lista2):
    """Retorna a concatenação das duas listas."""
    return lista1 + lista2

if __name__ == "__main__":
    natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
    tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
    print(juntar_listas(natureza, tecnologia))
