# TPC1: Análise de um dataset

## 2024-02-09

## Autor
- **Nome:** Tomás Monteiro Sousa
- **Id:** A100546

## Enunciado
1. Proibido usar o módulo CSV;
2. Ler o dataset, processá-lo e criar os seguintes resultados:
    - Lista ordenada alfabeticamente das modalidades desportivas; 
    - Percentagens de atletas aptos e inaptos para a prática desportiva;
    - Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

## Resultados
De modo a resolver o *TPC1* foi fornecido um dataset nomeado `"emd.csv"` onde são apresentados dados sobre atletas.
A primeira linha do *dataset* aprsenta os dados relativamente a cada atleta:

0|1|2|3|4|5|6|7|8|9|10|11|12
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
_id | index | dataEMD | nome/primeiro | nome/último | idade | género | morada | modalidade | clube | email | federado | resultado

Para resolver o problema, sem utilizar o módulo CSV do Python, decidi criar uma função `parse_file` que lê linha a linha o dataset e recolhe a informação pertinente para a resolução do problema. Os dados essenciais para a resolução do exercício são: a modalidade, a idade e o resultado do teste físico do atleta. Desta forma, podemos obter a seguinte função:

```py
def parse_file(ficheiro):
     modalidades = set()
     aptos = 0
     qtd = 0
     f_etaria = [0] * 20

     for line in ficheiro:
          dados = line.strip().split(',')
          modalidades.add(dados[8])
          if(dados[12].strip() == "true"):
               aptos += 1
          f_etaria[int(dados[5])//5] += 1
          qtd += 1
     
     return modalidades,aptos,qtd,f_etaria
```
Após analisar todo o dataset, teremos um conjunto com todas as modalidades presentes no dataset (`modalidades`), o número total de atletas (`qtd`), quantos atletas passaram no exame médico desportivo (`aptos`) e uma lista com a quantidade de pessoas presentes em intervalos de 5 anos dos 0 aos 100 anos (`f_etaria`).

De modo o cumprir os resultados esperados foram criadas três funções diferentes. A função `print_modalidades` ordena as modalidades alfabeticamente e imprime uma a uma:

```py
def print_modalidades(modalidades):
     modalidades = sorted(modalidades)
     print("Modalidades ordenadas alfabeticamente: ")
     for modalidade in modalidades:
          print(f" • {modalidade}")
     print()
```

A função `print_aptos` apresenta a quantidade total de atletas e a quantidade e percentagem de atletas que estão aptos e inaptos:

```py
def print_aptos(aptos,qtd):
     perAptos = (aptos * 100.) / qtd
     print(f"Quantidade total de atletas: {qtd}")
     print(f"Percentagem de atletas aptos: {perAptos}%")
     print(f"Percentagem de atletas inaptos: {100-perAptos}%")
     print()
```

A função `print_distribuicao` imprime a quantidade e percentagem de atletas com idade compreendida dentro de um certo intervalo de 5 anos:

```py
def print_distribuicao(f_etaria,qtd):
     print("Distribuição de atletas por faxa etária (Intervalo de 5 anos): ")
     for i,escalao in enumerate(f_etaria):
          if(escalao != 0):
               percentagem = (escalao * 100.) / qtd
               print(f" • [{i*5},{i*5+4}] -> {escalao} atletas - {percentagem}%") 
```
Finalmente, usando o ficheiro `"tpc1.py"` e o dataset `"emd.csv"` obtive o seguinte *output*:

```py
> cat emd.csv | python3 tpc1.py

Modalidades ordenadas alfabeticamente:
 • Andebol
 • Atletismo
 • BTT
 • Badminton
 • Basquetebol
 • Ciclismo
 • Dança
 • Equitação
 • Esgrima
 • Futebol
 • Karaté
 • Orientação
 • Parapente
 • Patinagem
 • Triatlo

Quantidade total de atletas: 300
Percentagem de atletas aptos: 54.0%
Percentagem de atletas inaptos: 46.0%

Distribuição de atletas por faxa etária (Intervalo de 5 anos):
 • [20,24] -> 80 atletas - 26.666666666666668%
 • [25,29] -> 102 atletas - 34.0%
 • [30,34] -> 104 atletas - 34.666666666666664%
 • [35,39] -> 14 atletas - 4.666666666666667%
```
