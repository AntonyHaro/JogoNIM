# Jogo do NIM

Bem-vindo ao jogo do NIM! Este é um jogo de estratégia simples implementado em Python, onde o jogador que retirar a última peça do tabuleiro ganha.

## Descrição

- O Jogo do NIM é um jogo matemático em que dois jogadores se alternam para retirar um número de peças de um tabuleiro. Em cada turno, um jogador deve retirar pelo menos uma peça e no máximo um número fixo de peças. O jogador que retirar a última peça ganha o jogo.
- Nesta aplicação, foi implementado um sistema inteligente para que o computador faça a melhor jogada possível para que vença o jogador.

## Regras

1. O tabuleiro começa com `n` peças.
2. Cada jogador pode retirar entre 1 e `m` peças em seu turno.
3. O jogador que retirar a última peça do tabuleiro ganha.

## Instalação

Para jogar, você precisa ter o Python instalado em sua máquina. Se você não tem o Python instalado, pode baixá-lo em [python.org](https://www.python.org/).

Clone este repositório ou faça o download dos arquivos para sua máquina.

## Como Jogar

1. Execute o arquivo Python `jogo_do_nim.py`.
2. Escolha se deseja jogar uma partida isolada ou um campeonato:
   - Digite `1` para uma partida isolada.
   - Digite `2` para um campeonato (melhor de 3 partidas).

### Exemplo de Uso

```bash
python jogo_do_nim.py
```

---

## Estrutura do Código

O código está dividido em funções principais:

- `computador_escolhe_jogada(n, m)`: Calcula a jogada do computador.
- `usuario_escolhe_jogada(n, m)`: Captura a jogada do usuário.
- `partida()`: Controla a lógica de uma partida isolada.
- `campeonato()`: Controla a lógica de um campeonato.
- `main()`: Função principal que inicia o jogo.
