# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> IA FORC-A.

## 2. Integrantes do grupo

- Nome 1: Bruno Calazans dos Reis 
- Nome 2: Emelly Vitória Prates Maciel
- Nome 3: Júlia Vitória Santiado Assunção
- Nome 4: Ruan Pablo Silva Pinto

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Confiabilidade de sistemas inteligentes.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> Durante o jogo, uma "IA assistente" sugere uma letra para o jogador. Às vezes a sugestão está errada. O jogador pode aceitar, conferir antes (perdendo alguns pontos) ou escolher outra letra. Se aceitar uma sugestão errada, perde uma parte do corpo do boneco.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Jogo da forca.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> Aparece na tela a forca, a palavra escondida com traços, as letras já usadas, uma dica, a pontuação e a sugestão da IA. O jogador digita letras para descobrir a palavra. As palavras são sobre IA e uso responsável (ex.: PRIVACIDADE, ALGORITMO, DEEPFAKE).

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Descobrir 5 palavras sem ser enforcado e fazer o máximo de pontos.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: o jogador pode errar até 6 vezes em cada palavra.
- Regra 2: cada letra certa vale 10 pontos.
- Regra 3: a IA sugere uma letra a cada jogada e pode estar errada.
- Regra 4: aceitar uma sugestão errada da IA conta como erro.
- Regra 5: conferir a sugestão custa 5 pontos.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> Acertar as 5 palavras.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> O jogador perde quando o boneco é completado (6 erros). Também pode sair apertando ESC.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** a palavra secreta e o boneco da forca.
- **Obstáculos ou desafios:** as sugestões erradas da IA e o limite de erros.
- **Itens ou objetos de interação (se houver):** a caixa com a sugestão da IA e a dica da palavra.
- **Pontuação, vidas, tempo ou progresso:** pontos, número de erros e quantas palavras já foram acertadas. O recorde fica salvo em arquivo.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

>  Letras A a Z para chutar uma letra, ENTER para aceitar a sugestão da IA, TAB para conferir a sugestão e ESC para sair.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: pegar as letras digitadas no teclado e não deixar repetir letra.
- Dificuldade 2: fazer a IA errar de vez em quando de forma equilibrada.
- Dificuldade 3: usar o GitHub em grupo.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Tela com a forca, a palavra e a sugestão da IA. O jogador chuta letras, os erros desenham o boneco e os acertos mostram as letras. Tem pontuação, vitória e derrota. As palavras ficam em um arquivo de texto e o recorde é salvo. Testes simples das funções principais.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: tela inicial com as instruções.
- Melhoria 2: ranking com os melhores jogadores.
- Melhoria 3: sons de acerto e erro.
