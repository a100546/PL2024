# TPC3: Somador on/off

## 2024-02-23

## Autor
- **Nome:** Tomás Monteiro Sousa
- **Id:** A100546

## Enunciado
```txt
Somador on/off: criar o programa em Python
     1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
     2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
     3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
     4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
```

## Solução
De forma a resolver o `TPC3` criei um programa em python que opera como um somador de acordo com as especificações fornecidas no enunciado.

A função `sumOnOff(lines)` recebe como entrada um conjunto de linhas de texto e percorre cada linha, aplicando uma expressão regular para identificar os padrões definidos no enunciado. Esta função controla a soma das sequências de dígitos encontrados, levando em consideração os comandos "ON" e "OFF" para ligar e desligar a operação de soma, respectivamente.

A expressão regular regex é definida para identificar quatro tipos de padrões:

- "(ON)": Correspondendo à string "ON" em qualquer combinação de maiúsculas e minúsculas.
- "(OFF)": Correspondendo à string "OFF" em qualquer combinação de maiúsculas e minúsculas.
- "([-|+]*\d+)": Correspondendo a uma sequência de dígitos, opcionalmente precedida por um sinal de adição ou subtração.
- "(=)": Correspondendo ao caractere "=".

A função `main()` é responsável por chamar a função sumOnOff com a entrada padrão (sys.stdin).

Dentro da função `sumOnOff`, cada linha de texto é analisada usando a expressão regular `re.findall()`. Os resultados são iterados e processados de acordo com os padrões encontrados. Se a string `ON` é encontrada, a variável `canSum` passa a ser verdadeira, permitindo que a soma ocorra. Se a string `OFF` for encontrada, a variável `canSum` passa a ser falsa, interrompendo a soma. Se uma sequência de dígitos é encontrada e `canSum` é verdadeira, a soma é atualizada com o valor encontrado. Se o `=` é encontrado, o resultado da soma atual é apresentado na saída padrão.

## Como executar o código
Para executar o código é necessário ter um ficheiro com sequências de digitos e caracteres e executar o código da seguinte forma:
```bash
$ cat <ficheiro de teste> | python3 sumOnOff.py
```

## Resultados
Foram utilizados os seguintes ficheiros para testar o programa:

Ficheiro 1:
```txt
3njvjeOn=fniesm4knfOFfknek9ene=7bekoNne4bfe3=fejej4bbfeObfjd=3bfh5jwd33jwfbegnOn39bbegndOff768678=ON2=
```

Ficheiro 2:
```txt
1 = ON 2 -3 = OFF 4 56 3 = ON 10 =
```

Foram obtidas as seguintes soluções, respetivamente:

Ficheiro 1:
```txt
Sum = 3
Sum = 7
Sum = 14
Sum = 18
Sum = 98
Sum = 100
```

Ficheiro 2:
```txt
Sum = 1
Sum = 0
Sum = 0
Sum = 10
```