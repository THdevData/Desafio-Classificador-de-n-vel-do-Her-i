hero = "Destruidor de Mundo 123"
xp = 100000
nivel = ""

if xp <= 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Radiante"
elif xp <= 100000:
    nivel = "Deus"

print(f"O Herói de nome {hero} está no nível {nivel}")