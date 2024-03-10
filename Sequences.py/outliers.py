data = [6,9,20,78,99,265,109,198,144,120,168,153,486,279,690]
data.sort()
min_valid = 100
max_valid = 200

stop = 0
for index , value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) -1,-1,-1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)