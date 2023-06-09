value = int(input())

year = value/365
value = value % 365

month = value/30
days = value % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(int(year),int(month),int(days)))