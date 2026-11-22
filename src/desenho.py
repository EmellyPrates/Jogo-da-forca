import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    MAX_ERROS,
    FUNDO,
    PAINEL,
    TEXTO,
    TEXTO_SUAVE,
    DESTAQUE,
    VERDE,
    VERMELHO,
    AMARELO,
    FORCA_COR,
    CUSTO_CONFERIR,
)
from src.funcoes import ALFABETO, mascarar_palavra


CORES_MENSAGEM = {
    "ok": VERDE,
    "erro": VERMELHO,
    "info": AMARELO,
}


def criar_fontes():
    return {
        "titulo": pygame.font.Font(None, 40),
        "palavra": pygame.font.Font(None, 72),
        "normal": pygame.font.Font(None, 28),
        "pequena": pygame.font.Font(None, 22),
        "letra": pygame.font.Font(None, 30),
        "sugestao": pygame.font.Font(None, 64),
    }


def escrever(tela, fonte, texto, cor, posicao, centralizar=False):
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect()

    if centralizar:
        retangulo.center = posicao
    else:
        retangulo.topleft = posicao

    tela.blit(imagem, retangulo)


def desenhar_forca(tela, erros):
    base_x = 60
    base_y = 430

    pygame.draw.line(tela, FORCA_COR, (base_x, base_y), (base_x + 260, base_y), 8)
    pygame.draw.line(tela, FORCA_COR, (base_x + 60, base_y), (base_x + 60, base_y - 320), 8)
    pygame.draw.line(tela, FORCA_COR, (base_x + 60, base_y - 320), (base_x + 200, base_y - 320), 8)
    pygame.draw.line(tela, FORCA_COR, (base_x + 200, base_y - 320), (base_x + 200, base_y - 280), 4)

    centro_x = base_x + 200
    cabeca_y = base_y - 250

    if erros >= 1:
        pygame.draw.circle(tela, TEXTO, (centro_x, cabeca_y), 30, 4)
    if erros >= 2:
        pygame.draw.line(tela, TEXTO, (centro_x, cabeca_y + 30), (centro_x, cabeca_y + 120), 4)
    if erros >= 3:
        pygame.draw.line(tela, TEXTO, (centro_x, cabeca_y + 55), (centro_x - 40, cabeca_y + 100), 4)
    if erros >= 4:
        pygame.draw.line(tela, TEXTO, (centro_x, cabeca_y + 55), (centro_x + 40, cabeca_y + 100), 4)
    if erros >= 5:
        pygame.draw.line(tela, TEXTO, (centro_x, cabeca_y + 120), (centro_x - 35, cabeca_y + 180), 4)
    if erros >= 6:
        pygame.draw.line(tela, TEXTO, (centro_x, cabeca_y + 120), (centro_x + 35, cabeca_y + 180), 4)


def desenhar_cabecalho(tela, fontes, estado, total_palavras):
    numero = estado["indice"] + 1
    escrever(tela, fontes["titulo"], "IA FORC-A", DESTAQUE, (30, 20))
    texto = f"Palavra {numero}/{total_palavras}    Pontos: {estado['pontos']}    Recorde: {estado['recorde']}"
    imagem = fontes["normal"].render(texto, True, TEXTO)
    retangulo = imagem.get_rect(topright=(LARGURA_TELA - 30, 28))
    tela.blit(imagem, retangulo)


def desenhar_dica(tela, fontes, dica):
    escrever(tela, fontes["normal"], "Dica: " + dica, TEXTO_SUAVE, (30, 68))


def desenhar_painel_ia(tela, fontes, estado):
    caixa = pygame.Rect(400, 110, 370, 190)
    pygame.draw.rect(tela, PAINEL, caixa, border_radius=12)
    pygame.draw.rect(tela, DESTAQUE, caixa, 2, border_radius=12)

    escrever(tela, fontes["normal"], "IA assistente sugere:", DESTAQUE, (caixa.x + 18, caixa.y + 14))

    centro_x = caixa.x + caixa.width // 2

    if estado["fase"] == "jogando":
        escrever(tela, fontes["sugestao"], estado["sugestao"], TEXTO, (centro_x, caixa.y + 62), centralizar=True)

        if not estado["conferida"]:
            status = "Sugestão não conferida"
            cor_status = AMARELO
        elif estado["sugestao_certa"]:
            status = "Conferida: sugestão CORRETA"
            cor_status = VERDE
        else:
            status = "Conferida: sugestão ERRADA"
            cor_status = VERMELHO

        escrever(tela, fontes["normal"], status, cor_status, (centro_x, caixa.y + 100), centralizar=True)
    else:
        escrever(tela, fontes["normal"], "Aguardando...", TEXTO_SUAVE, (centro_x, caixa.y + 80), centralizar=True)

    escrever(tela, fontes["pequena"], "ENTER: aceitar a sugestão", TEXTO_SUAVE, (caixa.x + 18, caixa.y + 124))
    escrever(
        tela,
        fontes["pequena"],
        f"TAB: conferir (custa {CUSTO_CONFERIR} pontos)",
        TEXTO_SUAVE,
        (caixa.x + 18, caixa.y + 146),
    )
    escrever(tela, fontes["pequena"], "Ou digite outra letra de A a Z", TEXTO_SUAVE, (caixa.x + 18, caixa.y + 168))


def desenhar_alfabeto(tela, fontes, palavra, usadas):
    inicio_x = 400
    inicio_y = 325
    largura_celula = 28
    altura_celula = 36

    for indice, letra in enumerate(ALFABETO):
        coluna = indice % 13
        linha = indice // 13
        x = inicio_x + coluna * largura_celula
        y = inicio_y + linha * altura_celula

        if letra in usadas:
            cor = VERDE if letra in palavra else VERMELHO
        else:
            cor = TEXTO_SUAVE

        escrever(tela, fontes["letra"], letra, cor, (x + largura_celula // 2, y + 12), centralizar=True)


def desenhar_palavra(tela, fontes, palavra, usadas, revelar=False):
    if revelar:
        texto = " ".join(palavra)
    else:
        texto = mascarar_palavra(palavra, usadas)

    escrever(tela, fontes["palavra"], texto, TEXTO, (LARGURA_TELA // 2, 500), centralizar=True)


def desenhar_mensagem(tela, fontes, estado):
    texto, tipo = estado["mensagem"]
    cor = CORES_MENSAGEM.get(tipo, TEXTO)
    escrever(tela, fontes["normal"], texto, cor, (LARGURA_TELA // 2, 553), centralizar=True)


def desenhar_rodape(tela, fontes, estado):
    if estado["fase"] == "palavra_completa":
        texto = "ENTER: próxima palavra    ESC: sair"
    elif estado["fase"] in ("vitoria", "derrota"):
        texto = "R: jogar de novo    ESC: sair"
    else:
        texto = "A-Z: chutar    ENTER: aceitar IA    TAB: conferir IA    ESC: sair"

    escrever(tela, fontes["pequena"], texto, TEXTO_SUAVE, (LARGURA_TELA // 2, ALTURA_TELA - 16), centralizar=True)


def desenhar_tela(tela, fontes, estado, palavra, dica, total_palavras):
    tela.fill(FUNDO)

    desenhar_cabecalho(tela, fontes, estado, total_palavras)
    desenhar_dica(tela, fontes, dica)
    desenhar_forca(tela, MAX_ERROS - estado["vidas"])
    desenhar_painel_ia(tela, fontes, estado)
    desenhar_alfabeto(tela, fontes, palavra, estado["usadas"])
    desenhar_palavra(tela, fontes, palavra, estado["usadas"], revelar=estado["fase"] == "derrota")
    desenhar_mensagem(tela, fontes, estado)
    desenhar_rodape(tela, fontes, estado)

    pygame.display.flip()
