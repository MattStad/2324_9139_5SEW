def waterland(file,outfile):
    file = open(file,"r")
    length=int(file.readline())
    map = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        row = file.readline()
        for ii in range(len(row)-1):
            map[i][ii]=row[ii]

    for i in map:
        for ii in i:
            print(ii,end="")
        print("")

    guess = int(file.readline())
    outfile = open(outfile,"w")
    for i in range(guess):
        coord=file.readline()
        x,y=coord.strip().split(",")
        outfile.write(map[int(y)][int(x)]+"\n")

waterland(".\\level1\\level1_example.in",".\\level1\\level1_example_my.out")
waterland((".\\level1\\level1_1.in"),".\\level1\\level1_1.out")
waterland((".\\level1\\level1_2.in"),".\\level1\\level1_2.out")
waterland((".\\level1\\level1_3.in"),".\\level1\\level1_3.out")
waterland((".\\level1\\level1_4.in"),".\\level1\\level1_4.out")
waterland((".\\level1\\level1_5.in"),".\\level1\\level1_5.out")