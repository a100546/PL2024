import sys

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

def print_modalidades(modalidades):
     modalidades = sorted(modalidades)
     print("Modalidades ordenadas alfabeticamente: ")
     for modalidade in modalidades:
          print(f" • {modalidade}")
     print()

def print_aptos(aptos,qtd):
     perAptos = (aptos * 100.) / qtd
     print(f"Quantidade total de atletas: {qtd}")
     print(f"Percentagem de atletas aptos: {perAptos}%")
     print(f"Percentagem de atletas inaptos: {100-perAptos}%")
     print()
     
def print_distribuicao(f_etaria,qtd):
     print("Distribuição de atletas por faxa etária (Intervalo de 5 anos): ")
     for i,escalao in enumerate(f_etaria):
          if(escalao != 0):
               percentagem = (escalao * 100.) / qtd
               print(f" • [{i*5},{i*5+4}] -> {escalao} atletas - {percentagem}%") 

def main():
     with open(sys.stdin.fileno(), 'r', encoding='utf-8') as ficheiro:
          _ = ficheiro.readline()
          modalidades,aptos,qtd,f_etaria = parse_file(ficheiro)
     
     print_modalidades(modalidades)
     print_aptos(aptos,qtd)
     print_distribuicao(f_etaria,qtd)

if __name__ == "__main__":
    main()