def waterland(file,outfile):
    file = open(file,"r")
    length=int(file.readline())
    map = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        row = file.readline()
        for ii in range(len(row)-1):
            map[i][ii]=row[ii]

    """
    for i in map:
        for ii in i:
            print(ii,end="")
        print("")
    """

    n_guess = int(file.readline())
    outfile = open(outfile,"w")
    for i in range(n_guess):
        cords=file.readline().strip().split(" ")
        firstcord=cords[0].split(",")
        secondcord = cords[1].split(",")
        if sameland(map,int(firstcord[0]),int(firstcord[1]),int(secondcord[0]),int(secondcord[1])):
            outfile.write("SAME\n")
        else:
            outfile.write("DIFFERENT\n")

def sameland(map, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = set()
    stack = [(x1, y1)]

    while stack:
        x, y = stack.pop()
        visited.add((x, y))

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map) and map[new_y][new_x] == 'L' and (new_x, new_y) not in visited:
                stack.append((new_x, new_y))
                visited.add((new_x, new_y))

                if new_x == x2 and new_y == y2:
                    return True

    return False


waterland(".\\level2\\level2_example.in",".\\level2\\level2_example_my.out")
waterland((".\\level2\\level2_1.in"),".\\level2\\level2_1.out")
print("LEVEL1")
waterland((".\\level2\\level2_2.in"),".\\level2\\level2_2.out")
print("LEVEL2")
waterland((".\\level2\\level2_3.in"),".\\level2\\level2_3.out")
print("LEVEL3")
waterland((".\\level2\\level2_4.in"),".\\level2\\level2_4.out")
print("LEVEL4")
waterland((".\\level2\\level2_5.in"),".\\level2\\level2_5.out")
print("LEVEL5")
print("DONE")