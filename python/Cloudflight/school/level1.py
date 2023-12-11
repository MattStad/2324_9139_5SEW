def count(file):
    file=open(file,"r")
    lines=int(file.readline())
    count_dict = {}
    for i in file:
        i=i.strip()
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def outlevel1(dic,outfile):
    file=open(outfile,"w")
    for i in dic.items():
        if i != None:
            file.write(str(i[1])+" "+i[0]+"\n")


outlevel1(count(".\\level1\\level1_1.in"),".\\level1\\level1_1.out")
outlevel1(count(".\\level1\\level1_2.in"),".\\level1\\level1_2.out")
outlevel1(count(".\\level1\\level1_3.in"),".\\level1\\level1_3.out")
outlevel1(count(".\\level1\\level1_4.in"),".\\level1\\level1_4.out")
outlevel1(count(".\\level1\\level1_5.in"),".\\level1\\level1_5.out")
