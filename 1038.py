cod_qntd = input().split()
code, qntd = cod_qntd

code = int(code)
qntd = int(qntd)
value = 0

if code == 1:
    value = 4.00
if code == 2:
    value = 4.50
if code == 3:
    value = 5.00
if code == 4:
    value = 2.00
if code == 5:
    value = 1.50

total = value * qntd

print("Total: R$ %0.2f" %total)
