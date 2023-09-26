
salary = float(input())
imposto = 0


if salary > 2000.00:
    temp_salary3 = salary - 2000.00
    if temp_salary3 > 1000.00:
        temp_salary3 = 1000.00
    temp3 = 0.08 * temp_salary3
    imposto = imposto + temp3

    if salary > 3000.00:
        temp_salary2 = salary - 3000.00
        if temp_salary2 > 1500.00:
            temp_salary2 = 1500.00
        temp2 = 0.18 * temp_salary2
        imposto = imposto + temp2

        if salary > 4500.00:
            temp_salary = salary - 4500.00
            temp = 0.28 * temp_salary
            imposto = imposto + temp
            
    
if imposto == 0:
    print("Isento")
else:
    print("R$ %.2f" %imposto)
