# Aula 596 - Unittest 3 com TDD
Nesta aula vamos trabalhar com dados fakes aonde simulamos uma requisição para uma API está up ou down. Vamos começar criando o arquivo test_pessoa.py

- Vamos seguir a seguinte estrutura

        class Pessoa
        __init__ 
            nome str
            sobrenome str
            dados_obtidos bool

        API:
            obter_todos_os_dados -> method
            OK
            404

- Criando a classe TestPessoa:

        import unittest

        class TestPessoa(unittest.TestCase):
            def setUp(self):
                self.p1 = Pessoa('Luiz')

            def test_pessoa_attr_nome_valor_tem_o_valor_correto(self):
                pass


        if __name__ == '__main__':
            unittest.main(verbosity=2)



## Uma curiosidade: Instanciar
-> vamos relembrar algumas coisas
### Classe 
- é como um molde, que por sua vez gerar instancias de um certo tipo
- Ela quem define os comportamentos dos objetos, através de métodos (que são suas "Funções") que os objetos podem executar

### Objeto 
- é algo que existe fisicamente que foi "moldado" na classe
- pode ser algo concreto (como um carro, animal, pessoa,), como pode ser algo abstrato (como um sistema bancário ou um 
processo)

### Instanciar
- na programação orientada a objetos quer dizer criar. Quando você cria um objeto derivado de uma classe você está 
instanciando um objeto nessa classe.
- ela também envolve
    - Alocar memória para o objeto na memória do computador.
    - Inicializar os atributos do objeto com valores iniciais (se definidos na classe).
    - Tornar os métodos do objeto acessíveis.

### Atalho que aprendi (sem querer)
- No Pycharm quando se usa a combinação Ctrl+Shift+(seta p/ cima ou p/ baixo) você move a linha em que o cursor está para
cima ou para baixo