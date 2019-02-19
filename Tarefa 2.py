# Matheus Moreira - Retornar idade em dias
anos = int(input("Digite sua idade em anos:"))
meses = int(input("Digite sua idade em meses:"))
dias = int(input("Digite sua idade em dias:"))

total_anos_em_dias = anos * 365
total_meses_em_dias = meses * 30

total_dias = total_anos_em_dias + total_meses_em_dias + dias

print("Sua idade em dias é igual a ", total_dias, " dias")