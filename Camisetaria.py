def obter_modelo():
    precos = {"MCS": 1.80, "MLS": 2.10, "MCE": 2.90, "MLE": 3.20}
    while True:
        print("\n--- Modelos Disponíveis ---")
        print("MCS - Manga Curta Simples | MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa | MLE - Manga Longa Com Estampa")
        modelo = input("Escolha o modelo (sigla): ").upper()
        if modelo in precos:
            return precos[modelo]
        print("Erro: Modelo inválido. Tente novamente.")


def obter_quantidade():
    while True:
        try:
            qtd = int(input("\nEntre com o número de camisetas: "))
            if 0 < qtd <= 20000:
                return qtd
            print("Quantidade inválida (limite até 20.000).")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")


def obter_frete():
    opcoes = {"1": 100.00, "2": 200.00, "0": 0.00}
    print("\nEscolha o frete:")
    print("1 - Transportadora (R$ 100.00)\n2 - Sedex (R$ 200.00)\n0 - Retirar na fábrica (R$ 0.00)")
    while True:
        escolha = input("Opção >> ")
        if escolha in opcoes:
            return opcoes[escolha]
        print("Opção de frete inválida.")


def calcular_desconto(qtd):
    if qtd >= 2000: return 0.12
    if qtd >= 200: return 0.07
    if qtd >= 20: return 0.05
    return 0.00


def main():
    print("Bem vindo à Fábrica de Camisetas do Jason Ferraz")

    valor_unitario = obter_modelo()
    quantidade = obter_quantidade()
    frete = obter_frete()

    # Cálculo lógico
    desconto = calcular_desconto(quantidade)
    valor_bruto = valor_unitario * quantidade
    valor_final = (valor_bruto * (1 - desconto)) + frete

    # Exibição
    print("\n" + "=" * 30)
    print(f"Resumo do Pedido:")
    print(f"Modelo (un): R$ {valor_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Desconto aplicado: {desconto * 100:.0f}%")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Total a pagar: R$ {valor_final:.2f}")
    print("=" * 30)


if __name__ == "__main__":
    main()
