num = int(input())
results = []

for x in range(num):
    val = int(input())
    if val % 2 == 0:
        if val > 0:
            results.append("EVEN POSITIVE")
        elif val == 0:
            results.append("NULL")
        else:
            results.append("EVEN NEGATIVE")
    else:
        if val > 0:
            results.append("ODD POSITIVE")
        elif val == 0:
            results.append("NULL")
        else:
            results.append("ODD NEGATIVE")

for x in range(len(results)):
    print(results[x])
