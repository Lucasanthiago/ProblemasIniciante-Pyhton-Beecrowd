
loop = 1
win_inter = 0
win_gremio = 0
empate = 0
grenais = 0

while loop == 1:
    grenais += 1

    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)

    if inter > gremio:
        win_inter += 1
    if gremio > inter:
        win_gremio += 1
    if gremio == inter:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    loop = int(input())

print(grenais,"grenais")
print("Inter:%d" %win_inter)
print("Gremio:%d" %win_gremio)
print("Empates:%d" %empate)

if win_gremio > win_inter:
    print("Gremio venceu mais")
if win_gremio < win_inter:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
