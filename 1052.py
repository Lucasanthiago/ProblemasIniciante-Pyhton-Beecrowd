month = int(input())
month = month - 1
month_ext = ["January","February","March","April","May","June",
             "July","August","September","October","November","December"]

for i in range (len(month_ext)):
    if i == month:
        print(month_ext[i])

