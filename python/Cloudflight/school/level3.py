def to_array(file,outfile):
    file=open(file,"r")
    lines=int(file.readline())
    puzzle = [[0 for _ in range(lines)] for _ in range(lines)]
    c1=0
    for i in file:
        j=i.split(" ")
        c2=0
        for ii in j:
            puzzle[c1][c2]=ii.strip()
            c2=c2+1
        c1=c1+1

    print(puzzle)
    ##EDGE
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if i==0:
                puzzle[i][j] = puzzle[i][j][:0] + 'E' + puzzle[i][j][0 + 1:]
            if j==0:
                puzzle[i][j] = puzzle[i][j][:6] + 'E' + puzzle[i][j][6 + 1:]
            if i==len(puzzle)-1:
                puzzle[i][j] = puzzle[i][j][:4] + 'E' + puzzle[i][j][4 + 1:]
            if j==len(puzzle)-1:
                puzzle[i][j] = puzzle[i][j][:2] + 'E' + puzzle[i][j][2 + 1:]
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            for n in range(4):
                if n==0 and i!=0:
                    if puzzle[i][j][0] == puzzle[i-1][j][4]:
                        if puzzle[i-1][j][4] == 'H':
                            puzzle[i][j] = puzzle[i][j][:0] + 'K' + puzzle[i][j][0 + 1:]
                        else:
                            puzzle[i][j] = puzzle[i][j][:0] + 'H' + puzzle[i][j][0 + 1:]

                if n==1 and j!=len(puzzle)-1:
                    if puzzle[i][j][2] == puzzle[i][j+1][6]:
                        print(puzzle[i][j][2] + "|" + puzzle[i][j+1][6])
                        if puzzle[i-1][j][6] == 'H':
                            puzzle[i][j] = puzzle[i][j][:2] + 'K' + puzzle[i][j][2 + 1:]
                        else:
                            puzzle[i][j] = puzzle[i][j][:2] + 'H' + puzzle[i][j][2 + 1:]

                if n == 2 and i != len(puzzle) - 1:
                    if puzzle[i][j][4] == puzzle[i + 1][j][0]:
                        if puzzle[i +1][j][0] == 'H':
                            puzzle[i][j] = puzzle[i][j][:4] + 'K' + puzzle[i][j][4 + 1:]
                        else:
                            puzzle[i][j] = puzzle[i][j][:4] + 'H' + puzzle[i][j][4 + 1:]

                if n == 3 and j != 0:
                    if puzzle[i][j][6] == puzzle[i][j-1][2]:
                        if puzzle[i][j-1][2] == 'H':
                            puzzle[i][j] = puzzle[i][j][:6] + 'K' + puzzle[i][j][6 + 1:]
                        else:
                            puzzle[i][j] = puzzle[i][j][:6] + 'H' + puzzle[i][j][6 + 1:]
    print(puzzle)
    file=open(outfile,"w")
    for i in puzzle:
        for ii in i:
            file.write(ii+" ")
        file.write("\n")


to_array(".\\level3\\level3_example.in",".\\level3\\level2_example_my.out")
to_array(".\\level3\\level3_1.in",".\\level3\\level3_1.out")
to_array(".\\level3\\level3_2.in",".\\level3\\level3_2.out")
to_array(".\\level3\\level3_3.in",".\\level3\\level3_3.out")
to_array(".\\level3\\level3_4.in",".\\level3\\level3_4.out")
to_array(".\\level3\\level3_5.in",".\\level3\\level3_5.out")
