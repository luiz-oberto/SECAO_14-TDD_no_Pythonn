# aula 594 Unitest #1
- Vamos criar um arquivo para testar a calculadora chamado test_calculadora.py
nela vamos importar o unittest e criar a seguinte classe

        class TestCalculadora(unittest.TestCase):
            pass

- todos os testes que voce escrever aqui dentro tem que começar com a palavra teste
- por exemplo:

        def test_soma_5_e_5_deve_retornar_10(self):
            self.assertEqual(soma(5, 5), 10)

        def test_soma_5_negativo_e_5_deve_retornar_0(self):
            self.assertEqual(soma(-5, 5), 0)

- Você pode também testar várias saídas da seguinte maneira:

        def test_soma_varias_entradas(self):
                x_y_saidas = (
                    (10, 10, 20),
                    (5, 5, 10),
                    (1.5, 1.5, 3.0),
                    (-5, 5, 1),
                    (100, 100, 200),
                )

                for x_y_saida in x_y_saidas:
                    with self.subTest(x_y_saida=x_y_saida):
                        x, y, saida = x_y_saida
                        self.assertEqual(soma(x,y), saida)

- O 'with' aqui é utilizado para retornar os valores que possam dar erro no teste  

podemos fazer o mesmo para a função subtrai ficando da seguinte maneira:

    def test_subtrai_5_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_5_negativo_na_posicao_x_e_5_positivo_na_posicao_y_deve_retornar_10_negativo(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def test_subtrai_5_positivo_na_posicao_x_e_5_negativo_na_posicao_y_deve_retornar_10_positivo(self):
        self.assertEqual(subtrai(5, -5), 10)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai("11", 0)

    def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(11, "0")