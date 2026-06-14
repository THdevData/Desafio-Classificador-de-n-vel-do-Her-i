def saldo(vitorias, derrotas):
    return vitorias - derrotas

def nivel(saldo):
    if saldo <= 10:
        return "Ferro"
    elif saldo >= 11 and saldo <= 20:
        return "Bronze"
    elif saldo >= 21 and saldo <= 50:
        return "Prata"
    elif saldo >= 51 and saldo <= 80:
        return "Ouro"
    elif saldo >= 81 and saldo <= 90:
        return "Diamante"
    elif saldo >= 91 and saldo <= 100:
        return "Lendário"
    elif saldo >= 101:
        return "Imortal"
    
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))
saldo_heroi = saldo(vitorias, derrotas)
nivel_heroi = nivel(saldo_heroi)
print(f"O Herói tem de saldo de {saldo_heroi} e está no nível {nivel_heroi}")