from catalogo import repository

def obter_livros(termo=None):
    if termo:
        return repository.buscar_livros(termo)
    return repository.listar_livros()


def adicionar_livro(titulo, autor, genero, ano):
    if not titulo or not autor or not genero or not ano:
        raise ValueError("Preencha todos os campos.")
    livro = {
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "genero": genero.strip(),
        "ano": int(ano)
    }
    return repository.cadastrar_livro(livro)

def preparar_catalogo():
    repository.inicializar_livros()
