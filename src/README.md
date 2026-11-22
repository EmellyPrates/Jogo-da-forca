# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, estado da partida, eventos e regras de interação.
- `funcoes.py`: funções de regra e lógica, sem Pygame (testadas em `tests/`).
- `desenho.py`: funções que desenham a tela (forca, painel da IA, alfabeto, palavra).
- `dados.py`: leitura e gravação de dados (palavras e recorde).
- `config.py`: constantes globais (tela, cores, regras, caminhos, FPS).
- `sprites.py`: recorte de spritesheet do template (não usado nesta etapa).

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.
