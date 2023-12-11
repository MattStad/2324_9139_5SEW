import re

def part_1(file):
    total_sum = 0
    with open(file, 'r') as file:
        for line in file:
            first_digit = re.search(r"\d", line).group()
            last_digit = re.findall(r'\d+', line)[-1]
            total_sum += int(first_digit) * 10 + int(last_digit)
    return total_sum

def extract_num(file):
    sum=0
    datei = open(file, 'r')
    for zeile in datei:
        last=False
        first=False
        zws=0
        for i in range(len(zeile)):
            if zeile[len(zeile)-1-i].isdigit() and not last:
                zws += int(zeile[len(zeile)-1-i])
                last=True
            elif zeile[i].isdigit() and not first:
                zws+=int(zeile[i])*10
                first=True
            if first and last:
                continue
        sum+=zws
    return sum

def extract_num_part2(file):
    sum=0
    datei = open(file, 'r')
    for zeile in datei:
        num=list()
        for i in range(len(zeile)):
            if zeile[i].isdigit():
                num.append(int(zeile[i]))
            else:
                if zeile.find('one')!=-1:
                    num.append(1)
                elif zeile.find('two')!=-1:
                    num.append(2)
                elif zeile.find('three')!=-1:
                    num.append(3)
                elif zeile.find('four')!=-1:
                    num.append(4)
                elif zeile.find('five')!=-1:
                    num.append(5)
                elif zeile.find('six')!=-1:
                    num.append(6)
                elif zeile.find('seven')!=-1:
                    num.append(7)
                elif zeile.find('eight')!=-1:
                    num.append(8)
                elif zeile.find('nine')!=-1:
                    num.append(9)
        zws=0
        for i in num:
            zws*10
            zws+=i
        sum+=zws
    return sum;

print(extract_num('.\level_1'))
print(part_1('.\level_1'))
print( extract_num_part2('.\level_1'))
