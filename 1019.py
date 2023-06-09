time = int(input())

seconds = time % 60
time = time/60

minutes = time % 60
time = time/60

seconds = int(seconds)
minutes = int(minutes)
time = int(time)

print('{}:{}:{}'.format(time,minutes,seconds))
