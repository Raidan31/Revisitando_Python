os: fornece funções para interagir com o sistema operacional, como obter informações sobre o ambiente do sistema, manipular arquivos e pastas, etc.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

sys: fornece funções e variáveis relacionadas ao sistema, como a versão do interpretador Python, caminhos de pesquisa de módulos, etc.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

math: fornece funções matemáticas avançadas, como seno, cosseno, logaritmos, etc.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

random: fornece funções para gerar números aleatórios.

random(): Gera um número de ponto flutuante aleatório entre 0 e 1.
randint(a, b): Gera um número inteiro aleatório entre a e b (ambos incluídos).
uniform(a, b): Gera um número de ponto flutuante aleatório entre a e b (ambos incluídos).
choice(seq): Retorna um elemento aleatório da sequência seq.

shuffle(seq): Embaralha aleatoriamente a sequência seq:
    A função shuffle do módulo random é usada para embaralhar uma sequência. Ela pode ser usada para embaralhar qualquer tipo de sequência, como uma lista, tupla ou string.

    A função shuffle não retorna um valor. Em vez disso, ela altera a sequência original e a embaralha aleatoriamente. Ou seja, depois de usar a função shuffle, 
    a sequência original estará embaralhada e não poderá ser recuperada.

    A função shuffle trabalha de maneira determinística, o que significa que ela produz a mesma sequência de embaralhamento sempre que for chamada com a mesma sequência de entrada e com a mesma semente 
    (se a semente for especificada).

    A função shuffle é muito útil em jogos, como cartas e dados, quando se precisa de um embaralhamento aleatório dos elementos da sequência.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

datetime: fornece classes e funções para trabalhar com datas e horas.

datetime.date: representa uma data no formato (ano, mês, dia).
datetime.time: representa um horário no formato (hora, minuto, segundo, microssegundo).
datetime.datetime: representa uma data e hora combinadas no formato (ano, mês, dia, hora, minuto, segundo, microssegundo).
datetime.timedelta: representa uma diferença entre duas datas ou horários.
datetime.timezone: representa um fuso horário.

datetime.strftime(formato, [tupla]): converte a tupla retornada pela função localtime para uma string formatada de acordo com o formato fornecido. O formato é uma string que contém códigos de formatação que começam com %, como %Y para o ano, %m para o mês, %d para o dia, %H para a hora, %M para o minuto, %S para o segundo etc. Se a tupla não for fornecida, o tempo atual é usado.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

re: fornece suporte a expressões regulares.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

json: fornece suporte a JSON (JavaScript Object Notation), que é um formato de dados popular usado para intercâmbio de dados na web.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

csv: fornece suporte para arquivos CSV (Comma-Separated Values), que são comuns em aplicativos que lidam com grandes quantidades de dados tabulares.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

requests: fornece uma biblioteca fácil de usar para fazer solicitações HTTP.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

numpy: fornece suporte para arrays e matrizes multidimensionais, juntamente com funções matemáticas para trabalhar com eles.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pandas: fornece suporte para análise e manipulação de dados em tabelas.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

time : É frequentemente usado para medir o tempo de execução de um programa ou para pausar a execução de um programa por um determinado período de tempo.

