# aula 597 - Unittest 4 - Executando todos os testes de ma vez
É possível executar todos os testes usando o seguinte comando 

        python3.x -m unittest -v

x -> a versão do python que está utilizando

- lembrando que ao final dos arquivos de testes você precisa ter o swguinte código escrito nele, senão retornará um erro:

~~~pyhton
if __name__ == '__main__':
    unittest.main(verbosity=2)
~~~

Feito isso agora você pode organizar seus teste numa pasta chamada **tests** contendo não só os testes que você fez até agora como também o arquivo ´__init__.py´ pelo fato de que essa pasta  á um pacote. Tendo feeito apenas isso não tem problema, porém, e se os arquivos que estamos testando estiver em uma outra pasta chamada 'src'?
