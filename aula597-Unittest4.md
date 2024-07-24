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


Nesse caso nossos testes apresentará alguns erros por não conseguir importar os métodos que precisa para testar, então temos que acrescentar as seguintes linhas de código para que voltem a fucionar corretamente:

~~~python
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
                # -> 'suba uma pasta e vá até a pasta src'
            )
        )
    )

except:
    raise
~~~
Essas linhas vão tentar importar os módulos *sys* e *os* e em seguida vai adicionar o caminho /src de forma que quando os teste for executado vai parecer que eles estã sendo executado dentro da pasta *src*.
- obs: Lembrando que isso precisa ser feito bem no topo do arquivo, senão dará erro nos import.