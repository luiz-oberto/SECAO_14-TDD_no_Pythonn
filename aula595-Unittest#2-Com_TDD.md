# Aula 595 - Unittest #2
- vamos enteder o ciclo do TDD
    - RED - precisamos testar as coisas
    - GREEN - depois de testar e verificar se vai falhar, a gente cria essa coisa
    - REFACTORED - depois de criar, a gente melhora essa coisa

### vamos criar um novo arquivo python chamado baconcomovos.py
 a lógica vai ser:
- 1 - Receber um número inteiro
- 2 - Saber ser um número é multiplo de 3 e 5
    Bacon com ovos
- 3 - Saber se o número é multiplo de 3:
    Bacon
- 4 - Saber se o número é multiplo somente de 5
    Ovos
- 5 - Saber se o número NÃO é multiplo de 3 e 5
    Passa fome

## TDD -> Test Driven Development
### Red
- parte 1 -> Criar o teste e ver falhar

### Green
- parte 2 -> Criar o código e ver o teste passar

### Refactor
- parte 3 -> Melhorar meu código

Nesta aula partimos da criação dos testes (vide: test_baconcomovos.py) para criar as funções do nosso arquivo principal (baconcomovos.py)