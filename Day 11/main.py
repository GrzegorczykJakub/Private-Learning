file = open('input.txt', 'r')
array = file.readlines()
for i in range(len(array)):
    array[i] = list(array[i].strip())
    for x in range(len(array[i])):
        array[i][x] = int(array[i][x])
light = 0


def check(i, x):
    global already_flashed
    returned = False
    for a in already_flashed:
        if i == a[0] and x == a[1]:
            returned = True
    return returned


for y in range(100):
    for i in range(len(array)):
        for x in range(len(array[i])):
            array[i][x] += 1
    flash = True
    already_flashed = []
    while flash:
        flash = False
        for i in range(len(array)):
            for x in range(len(array[i])):
                if array[i][x] > 9 and not check(i, x):
                    already_flashed.append([i, x])
                    flash = True
                    if i == 0:
                        for a in range(0, 2):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
                    elif i == len(array) - 1:
                        for a in range(-1, 1):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
                    else:
                        for a in range(-1, 2):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
    for i in range(len(array)):
        for x in range(len(array[i])):
            if array[i][x] > 9:
                array[i][x] = 0
                light += 1


print(light)
run = True
y = 100
while run:
    y = y + 1
    for i in range(len(array)):
        for x in range(len(array[i])):
            array[i][x] += 1
    flash = True
    already_flashed = []
    while flash:
        flash = False
        for i in range(len(array)):
            for x in range(len(array[i])):
                if array[i][x] > 9 and not check(i, x):
                    already_flashed.append([i, x])
                    flash = True
                    if i == 0:
                        for a in range(0, 2):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
                    elif i == len(array) - 1:
                        for a in range(-1, 1):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
                    else:
                        for a in range(-1, 2):
                            if x == 0:
                                for b in range(0, 2):
                                    array[i + a][x + b] += 1
                            elif x == len(array) - 1:
                                for b in range(-1, 1):
                                    array[i + a][x + b] += 1
                            else:
                                for b in range(-1, 2):
                                    array[i + a][x + b] += 1
    for i in range(len(array)):
        for x in range(len(array[i])):
            if array[i][x] > 9:
                array[i][x] = 0
                light += 1
    if len(already_flashed) == 100:
        print(y)
        run = False