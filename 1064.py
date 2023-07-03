val_post = 0
media = 0

for i in range(6):
    val = float(input())
    if val > 0:
        val_post = val_post + 1
        media = media + val

media = media/val_post

print(val_post,"valores positivos")
print("%.1f" %(media))
