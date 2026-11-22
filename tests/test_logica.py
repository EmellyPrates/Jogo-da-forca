from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

import random

from src.funcoes import (
    letra_valida,
    mascarar_palavra,
    palavra_completa,
    contar_ocorrencias,
    escolher_sugestao_ia,
    sugestao_esta_certa,
    cobrar_conferencia,
    sortear_palavras,
    tomar_dano,
)
from src.dados import carregar_palavras


class SorteioFixo:
    def __init__(self, valor):
        self.valor = valor

    def random(self):
        return self.valor

    def choice(self, opcoes):
        return opcoes[0]


def test_letra_valida_aceita_apenas_maiusculas_de_a_a_z():
    assert letra_valida("A") is True
    assert letra_valida("a") is False
    assert letra_valida("1") is False
    assert letra_valida("AB") is False


def test_mascarar_palavra_mostra_apenas_letras_usadas():
    assert mascarar_palavra("VIES", ["V", "E"]) == "V _ E _"


def test_palavra_completa():
    assert palavra_completa("ETICA", ["E", "T", "I", "C"]) is False
    assert palavra_completa("ETICA", ["E", "T", "I", "C", "A"]) is True


def test_contar_ocorrencias():
    assert contar_ocorrencias("A", "ALGORITMO") == 1
    assert contar_ocorrencias("I", "PRIVACIDADE") == 2
    assert contar_ocorrencias("Z", "ETICA") == 0


def test_tomar_dano_reduz_vidas_ate_derrota():
    vidas = 6
    for _ in range(6):
        vidas = tomar_dano(vidas, 1)
    assert jogador_perdeu(vidas) is True


def test_ia_sugere_letra_errada_quando_sorteio_abaixo_da_chance():
    sugestao = escolher_sugestao_ia("VIES", [], 0.3, rng=SorteioFixo(0.1))
    assert sugestao_esta_certa(sugestao, "VIES") is False


def test_ia_sugere_letra_certa_quando_sorteio_acima_da_chance():
    sugestao = escolher_sugestao_ia("VIES", [], 0.3, rng=SorteioFixo(0.9))
    assert sugestao_esta_certa(sugestao, "VIES") is True


def test_ia_nunca_sugere_letra_ja_usada():
    usadas = ["V", "I", "E"]
    for semente in range(50):
        sugestao = escolher_sugestao_ia("VIES", usadas, 0.3, rng=random.Random(semente))
        assert sugestao not in usadas


def test_cobrar_conferencia_desconta_pontos():
    assert cobrar_conferencia(20, 5) == 15


def test_cobrar_conferencia_nao_deixa_pontos_negativos():
    assert cobrar_conferencia(3, 5) == 0
    assert cobrar_conferencia(0, 5) == 0


def test_sortear_palavras_respeita_a_quantidade():
    palavras = [("A", "a"), ("B", "b"), ("C", "c"), ("D", "d")]
    assert len(sortear_palavras(palavras, 2)) == 2
    assert len(sortear_palavras(palavras, 10)) == 4


def test_carregar_palavras_le_formato_palavra_e_dica(tmp_path):
    arquivo = tmp_path / "palavras.txt"
    arquivo.write_text("etica;Dica um\nlinha invalida\nVIES;Dica dois\n", encoding="utf-8")
    assert carregar_palavras(str(arquivo)) == [("ETICA", "Dica um"), ("VIES", "Dica dois")]


def test_carregar_palavras_arquivo_inexistente(tmp_path):
    assert carregar_palavras(str(tmp_path / "nao_existe.txt")) == []
