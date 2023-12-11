def to_array(file,outfile=""):
    file=open(file,"r")
    n_pieces=int(file.readline())
    pieces=[0 for _ in range(n_pieces)]
    for i in range(n_pieces):
        pieces[i]=file.readline().strip()
    print(pieces)
    n_puzzel=int(file.readline())
    for i in range(n_pieces):
        pieces[i]=file.readline().strip()

to_array(".\\level4\\level4_example.in")