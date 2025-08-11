class Objeto:
    def __init__(self, nome):
        self.nome = nome

def extrair_nomes(lista_objetos):
    """Retorna uma lista contendo apenas os nomes dos objetos."""
    return [obj.nome for obj in lista_objetos]

if __name__ == "__main__":
    objetos = [Objeto("Cadeira"), Objeto("Mesa"), Objeto("Computador")]
    print(extrair_nomes(objetos))
