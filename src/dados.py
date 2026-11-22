def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except (FileNotFoundError, ValueError):
        return 0


def carregar_palavras(caminho_arquivo):
    palavras = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if ";" not in linha:
                    continue

                palavra, dica = linha.split(";", 1)
                palavra = palavra.strip().upper()

                if palavra.isalpha():
                    palavras.append((palavra, dica.strip()))

    except FileNotFoundError:
        return []

    return palavras
