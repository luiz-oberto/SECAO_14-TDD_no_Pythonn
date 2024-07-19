# AULA 1 - Criando o Projeto
## Começando
- vamos começar criando uam pasta e uma VENV dentro da pasta do nosso projeto
- instale também o code runner na parte de extensions
- configure o settings.json da seguinte maneira:

{
    "python.pythonPath": ".\\venv\\Scripts\\python",
    "code-runner.executorMap": {
        "python": ".\\venv\\Scripts\\python",
    }
}

- Dessa maneira a gente roda todo e qualquer código dentro do ambiente virtual

## Vantagens
- Perdemos pouco tempo criando o teste quando criamos a função
- por conta disso, qualquer um que chegar e ver os testes vai entender o programa faz e como funciona e vai entender o que fez de errado caso o programa quebre

## Doctest & Unittest (LEIA!)
https://docs.python.org/pt-br/3/library/doctest.html
https://docs.python.org/pt-br/3/library/unittest.html