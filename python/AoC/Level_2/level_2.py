import re

def part_1(input):
    max_red = 12
    max_green = 13
    max_blue = 14
    sum = 0
    for zeile in input:
        valid = True
        id = int(re.findall('Game ([0-9]+):', zeile)[0])
        zeile = zeile.split(':')[1]
        games = zeile.split(';')
        for game in games:
            if game.find(',') != -1:
                marbels = game.split(',')
                for marbel in marbels:
                    marbel=marbel.strip()
                    num = int(marbel.split(' ')[0])
                    color = marbel.split(' ')[1]
                    if color == 'green':
                        if num > max_green:
                            valid = False
                            break
                    elif color == 'red':
                        if num > max_red:
                            valid = False
                            break
                    elif color == 'blue':
                        if num > max_blue:
                            valid = False
                            break
        if (valid):
            sum += id
    return sum


def part_2(input):
    sum = 0
    for zeile in input:
        print(zeile)
        zeile = zeile.split(':')[1]
        games = zeile.split(';')
        max_red = 1
        max_green = 1
        max_blue = 1
        for game in games:
            if game.find(',') != -1:
                marbels = game.split(',')
                for marbel in marbels:
                    marbel=marbel.strip()
                    num = int(marbel.split(' ')[0])
                    color = marbel.split(' ')[1]
                    if color == 'green':
                        if num > max_green:
                            max_green=num
                    elif color == 'red':
                        if num > max_red:
                            max_red=num
                    elif color == 'blue':
                        if num > max_blue:
                            max_blue=num
        print("Red:"+str(max_red))
        print("Green:" + str(max_green))
        print("Blue:" + str(max_blue))
        sum += max_red*max_green*max_blue
    return sum

def read_file(file):
    return open(file, 'r')


print(part_1(read_file(".\level_2")))
print(part_2(read_file(".\level_2")))
