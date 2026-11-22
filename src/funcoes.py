import random


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letra_valida(letra):
    return len(letra) == 1 and letra in ALFABETO


def sortear_palavras(palavras, quantidade, rng=random):
    return rng.sample(palavras, min(quantidade, len(palavras)))


def mascarar_palavra(palavra, usadas):
    return " ".join(letra if letra in usadas else "_" for letra in palavra)


def palavra_completa(palavra, usadas):
    return all(letra in usadas for letra in palavra)


def contar_ocorrencias(letra, palavra):
    return palavra.count(letra)


def escolher_sugestao_ia(palavra, usadas, chance_erro, rng=random):
    disponiveis = [letra for letra in ALFABETO if letra not in usadas]
    certas = [letra for letra in disponiveis if letra in palavra]
    erradas = [letra for letra in disponiveis if letra not in palavra]

    if rng.random() < chance_erro and erradas:
        return rng.choice(erradas)

    if certas:
        return rng.choice(certas)

    if erradas:
        return rng.choice(erradas)

    return ""


def sugestao_esta_certa(sugestao, palavra):
    return sugestao in palavra


def cobrar_conferencia(pontos, custo):
    return limitar_valor(pontos - custo, 0, pontos)
