import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    MAX_ERROS,
    PALAVRAS_POR_PARTIDA,
    PONTOS_ACERTO,
    CUSTO_CONFERIR,
    CHANCE_IA_ERRAR,
    CAMINHO_RECORDE,
    CAMINHO_PALAVRAS,
)
from src.funcoes import (
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    cobrar_conferencia,
    sortear_palavras,
    palavra_completa,
    contar_ocorrencias,
    escolher_sugestao_ia,
    sugestao_esta_certa,
    letra_valida,
)
from src.dados import carregar_recorde, salvar_recorde, carregar_palavras
from src.desenho import criar_fontes, desenhar_tela


def criar_estado(palavras, recorde):
    estado = {
        "palavras": sortear_palavras(palavras, PALAVRAS_POR_PARTIDA),
        "indice": 0,
        "usadas": [],
        "vidas": MAX_ERROS,
        "pontos": 0,
        "recorde": recorde,
        "fase": "jogando",
        "mensagem": ("Digite uma letra ou use a sugestão da IA.", "info"),
        "sugestao": "",
        "sugestao_certa": False,
        "conferida": False,
    }
    gerar_sugestao(estado)
    return estado


def palavra_atual(estado):
    return estado["palavras"][estado["indice"]][0]


def dica_atual(estado):
    return estado["palavras"][estado["indice"]][1]


def gerar_sugestao(estado):
    palavra = palavra_atual(estado)
    estado["sugestao"] = escolher_sugestao_ia(palavra, estado["usadas"], CHANCE_IA_ERRAR)
    estado["sugestao_certa"] = sugestao_esta_certa(estado["sugestao"], palavra)
    estado["conferida"] = False


def registrar_recorde(estado):
    if estado["pontos"] > estado["recorde"]:
        estado["recorde"] = estado["pontos"]
        salvar_recorde(CAMINHO_RECORDE, estado["recorde"])


def verificar_fim_da_palavra(estado):
    palavra = palavra_atual(estado)

    if palavra_completa(palavra, estado["usadas"]):
        ultima = estado["indice"] == len(estado["palavras"]) - 1
        estado["fase"] = "vitoria" if ultima else "palavra_completa"
        if ultima:
            estado["mensagem"] = ("Você descobriu todas as palavras! Parabéns!", "ok")
            registrar_recorde(estado)
        else:
            estado["mensagem"] = ("Palavra descoberta! Aperte ENTER para continuar.", "ok")
    elif jogador_perdeu(estado["vidas"]):
        estado["fase"] = "derrota"
        estado["mensagem"] = ("O boneco foi completado. Fim de jogo.", "erro")
        registrar_recorde(estado)
    else:
        gerar_sugestao(estado)


def jogar_letra(estado, letra, pela_ia=False):
    if estado["fase"] != "jogando":
        return

    if letra in estado["usadas"]:
        estado["mensagem"] = (f"A letra {letra} já foi usada.", "info")
        return

    palavra = palavra_atual(estado)
    estado["usadas"].append(letra)

    if letra in palavra:
        estado["pontos"] = calcular_pontos(estado["pontos"], PONTOS_ACERTO)
        vezes = contar_ocorrencias(letra, palavra)
        if pela_ia:
            estado["mensagem"] = (f"A IA acertou! A letra {letra} aparece {vezes}x. +{PONTOS_ACERTO} pontos.", "ok")
        else:
            estado["mensagem"] = (f"Acertou! A letra {letra} aparece {vezes}x. +{PONTOS_ACERTO} pontos.", "ok")
    else:
        estado["vidas"] = tomar_dano(estado["vidas"], 1)
        if pela_ia:
            estado["mensagem"] = (f"A IA errou! Você aceitou {letra} sem conferir e perdeu uma parte do boneco.", "erro")
        else:
            estado["mensagem"] = (f"A letra {letra} não está na palavra.", "erro")

    verificar_fim_da_palavra(estado)


def aceitar_sugestao(estado):
    if estado["fase"] == "jogando":
        jogar_letra(estado, estado["sugestao"], pela_ia=True)


def conferir_sugestao(estado):
    if estado["fase"] != "jogando":
        return

    if estado["conferida"]:
        estado["mensagem"] = ("Essa sugestão já foi conferida.", "info")
        return

    estado["pontos"] = cobrar_conferencia(estado["pontos"], CUSTO_CONFERIR)
    estado["conferida"] = True

    if estado["sugestao_certa"]:
        estado["mensagem"] = (f"Conferência feita (-{CUSTO_CONFERIR}): a sugestão está correta.", "ok")
    else:
        estado["mensagem"] = (f"Conferência feita (-{CUSTO_CONFERIR}): a IA errou desta vez!", "erro")


def avancar_palavra(estado):
    if estado["fase"] != "palavra_completa":
        return

    estado["indice"] += 1
    estado["usadas"] = []
    estado["vidas"] = MAX_ERROS
    estado["fase"] = "jogando"
    estado["mensagem"] = ("Nova palavra! Digite uma letra ou use a IA.", "info")
    gerar_sugestao(estado)


def processar_evento_tecla(estado, evento, palavras):
    if evento.key == pygame.K_ESCAPE:
        return None

    if evento.key == pygame.K_RETURN:
        if estado["fase"] == "palavra_completa":
            avancar_palavra(estado)
        else:
            aceitar_sugestao(estado)
    elif evento.key == pygame.K_TAB:
        conferir_sugestao(estado)
    elif evento.key == pygame.K_r and estado["fase"] in ("vitoria", "derrota"):
        return criar_estado(palavras, estado["recorde"])
    elif pygame.K_a <= evento.key <= pygame.K_z:
        letra = chr(evento.key).upper()
        if letra_valida(letra):
            jogar_letra(estado, letra)

    return estado


def processar_eventos(estado, palavras):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return None

        if evento.type == pygame.KEYDOWN:
            estado = processar_evento_tecla(estado, evento, palavras)
            if estado is None:
                return None

    return estado


def executar_jogo():
    pygame.init()

    palavras = carregar_palavras(CAMINHO_PALAVRAS)
    if not palavras:
        print(f"Nenhuma palavra encontrada em {CAMINHO_PALAVRAS}.")
        pygame.quit()
        return

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fontes = criar_fontes()

    estado = criar_estado(palavras, carregar_recorde(CAMINHO_RECORDE))
    ultimo_estado = estado

    while estado is not None:
        relogio.tick(FPS)

        estado = processar_eventos(estado, palavras)
        if estado is None:
            break

        ultimo_estado = estado
        desenhar_tela(
            tela,
            fontes,
            estado,
            palavra_atual(estado),
            dica_atual(estado),
            len(estado["palavras"]),
        )

    registrar_recorde(ultimo_estado)
    pygame.quit()
