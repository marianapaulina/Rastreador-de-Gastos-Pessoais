import json
from datetime import datetime

def salvar_despesas(despesas):
    with open('despesas.json', 'w') as arquivo:
        json.dump(despesas, arquivo, indent=2)

def carregar_despesas():
    try:
        with open('despesas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def adicionar_despesa(despesas, data, categoria, valor):
    despesa = {'data': data, 'categoria': categoria, 'valor': valor}
    despesas.append(despesa)
    salvar_despesas(despesas)

def exibir_despesas(despesas):
    for despesa in despesas:
        print(f"{despesa['data']} | {despesa['categoria']} | R${despesa['valor']}")

def calcular_gastos_totais(despesas):
    total = sum(despesa['valor'] for despesa in despesas)
    print(f"\nGastos totais: R${total}")

def main():
    despesas = carregar_despesas()

    while True:
        print("\n### Rastreador de Gastos Pessoais ###")
        print("1. Adicionar Despesa")
        print("2. Visualizar Despesas")
        print("3. Calcular Gastos Totais")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            categoria = input("Digite a categoria da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            adicionar_despesa(despesas, data, categoria, valor)

        elif opcao == '2':
            exibir_despesas(despesas)

        elif opcao == '3':
            calcular_gastos_totais(despesas)

        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

