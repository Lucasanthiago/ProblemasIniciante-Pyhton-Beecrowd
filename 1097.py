x = 7
for i in range(1,10,2):
    if i > 1:
        x = x + 2
    for j in range(x,x-3,-1):
        print("I={} J={}".format(i,j))