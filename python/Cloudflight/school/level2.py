def count(file):
    file=open(file,"r")
    lines=int(file.readline())
    count_dict = {}
    for i in file:
        i=i.strip()
        #print("Normal:"+i)
        i_rotaded = [0] * 4
        i_array = i.split(",")
        count=0
        for j in range(4):
            for k in range(4):
                #print("j:" + str(j) +" k:" + str(k) +" len:" + str(len((i_array))))
                if j+k<len(i_array):
                    i_rotaded[k]=(i_array[k+j])
                else:
                    i_rotaded[k]=(i_array[k+j-4])
            #print("Rotated:"+str(i_rotaded))
            rot=i_rotaded[0]+","+i_rotaded[1]+","+i_rotaded[2]+","+i_rotaded[3]
            #print(rot)
            if rot in count_dict:
                count_dict[rot] += 1
                break
            else:
                count+=1
            if count==4:
                count_dict[i] = 1
    return count_dict

def outlevel1(dic,outfile):
    file=open(outfile,"w")
    for i in dic.items():
        if i != None:
            file.write(str(i[1])+" "+i[0]+"\n")

outlevel1(count(".\\level2\\level2_example.in"),".\\level2\\level2_example_my.out")
outlevel1(count(".\\level2\\level2_1.in"),".\\level2\\level2_1.out")
outlevel1(count(".\\level2\\level2_2.in"),".\\level2\\level2_2.out")
outlevel1(count(".\\level2\\level2_3.in"),".\\level2\\level2_3.out")
outlevel1(count(".\\level2\\level2_4.in"),".\\level2\\level2_4.out")
outlevel1(count(".\\level2\\level2_5.in"),".\\level2\\level2_5.out")
