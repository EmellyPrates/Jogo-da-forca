# IA FORC-A

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Bruno Calazans dos Reis
- Emelly Vitória Prates Maciel
- Júlia Vitória Santiado Assunção
- Ruan Pablo Silva Pinto

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo.
  - `jogo.py`: loop principal, estado da partida, eventos e regras de interação.
  - `funcoes.py`: regras puras (sem Pygame), fáceis de testar.
  - `desenho.py`: tudo que é desenhado na tela (forca, painel da IA, alfabeto, palavra).
  - `dados.py`: leitura e gravação de arquivos (palavras e recorde).
  - `config.py`: constantes (tela, cores, regras, caminhos).
- `data/`: `palavras.txt` (formato `PALAVRA;dica`) e `recorde.txt`.
- `tests/`: testes unitários com `pytest`.
- `docs/`: proposta do jogo e registro de mudanças de planejamento.

## Descrição do jogo

Jogo da forca sobre inteligência artificial e uso responsável. Uma "IA assistente" sugere uma letra a cada jogada, mas às vezes a sugestão está errada. O jogador decide se confia na IA, se confere a sugestão antes (gastando pontos) ou se escolhe outra letra.

## Objetivo do jogador

Descobrir 5 palavras sem completar o boneco da forca e fazer o máximo de pontos.

## Regras do jogo

- Cada palavra permite até 6 erros; no sexto erro o boneco é completado e a partida acaba.
- Cada letra certa vale 10 pontos.
- A IA sugere uma letra por jogada e erra em cerca de 30% das vezes.
- Aceitar uma sugestão errada da IA conta como erro.
- Conferir a sugestão custa 5 pontos (a pontuação nunca fica negativa) e revela se ela está certa ou errada.
- O recorde é salvo em `data/recorde.txt`.

## Controles

- `A` a `Z`: chutar uma letra
- `ENTER`: aceitar a sugestão da IA (ou ir para a próxima palavra)
- `TAB`: conferir a sugestão da IA
- `R`: jogar de novo (após vitória ou derrota)
- `ESC`: sair

## Como executar o projeto

```bash
git clone LINK_DO_REPOSITORIO
cd Jogo-da-forca
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Status da entrega atual

Já funciona: janela Pygame, loop principal, chute de letras, sugestão da IA (aceitar ou conferir), boneco desenhado a cada erro, pontuação, vitória, derrota, reinício e recorde salvo.

Ainda não feito (melhorias previstas na proposta): tela inicial com instruções, ranking, sons.
