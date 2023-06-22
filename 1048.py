salary = float(input())

if 0 < salary <= 400:
    percent = 15
    temp = salary
    salary = salary * (100+percent)/100
    ajuste = salary - temp

elif 400.01 < salary <= 800.00:
    percent = 12
    temp = salary
    salary = salary * (100+percent)/100
    ajuste = salary - temp

elif 800.01 <= salary <= 1200.00:
    percent = 10
    temp = salary
    salary = salary * (100 + percent) / 100
    ajuste = salary - temp

elif 1200.01 <= salary <= 2000.00:
    percent = 7
    temp = salary
    salary = salary * (100 + percent) / 100
    ajuste = salary - temp

elif salary >= 2000.00:
    percent = 4
    temp = salary
    salary = salary * (100 + percent) / 100
    ajuste = salary - temp

print('Novo salario: {:.2f}'.format(salary))
print('Reajuste ganho: {:.2f}'.format(ajuste))
print('Em percentual: {} %'.format(percent))
