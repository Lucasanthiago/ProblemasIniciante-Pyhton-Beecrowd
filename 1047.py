hora_ini, min_ini,hora_fin,min_fin = input().split()

hora_ini = int(hora_ini)
min_ini = int(min_ini)
hora_fin = int(hora_fin)
min_fin = int(min_fin)

hora = hora_fin - hora_ini
min = min_fin - min_ini

if min < 0:
    min = min + 60
    hora = hora - 1

if hora < 0:
    hora = hora + 24

if hora_fin == hora_ini and min_ini == min_fin:
    hora = 24

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hora,min))
