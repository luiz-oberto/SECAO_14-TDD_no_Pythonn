"""
class Pessoa
__init__ 
    nome str
    sobrenome str
    dados_obtidos bool

API:
    obter_todos_os_dados -> method
    OK
    404
"""
import unittest
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    # instaciando a classe
    def setUp(self):
        self.p1 = Pessoa('Luiz', 'Otavio')

    def test_pessoa_attr_nome_valor_tem_o_valor_correto(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)