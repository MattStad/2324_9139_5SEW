import argparse
import copy
import cProfile
import pstats
import time

def read_labyrinth(file_path):
    labyrinth = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            labyrinth.append(row)
    return labyrinth


def print_labyrinth(labyrinth):
    for row in labyrinth:
        print("".join(row))


def suchen(spalte, zeile, labyrinth):
    if labyrinth[spalte][zeile] == 'A':
        print_labyrinth(labyrinth)
        return True
    labyrinth[spalte][zeile] = 'X'
    if labyrinth[spalte - 1][zeile] != 'X' and labyrinth[spalte - 1][zeile] != '#':
        if suchen(spalte - 1, zeile, labyrinth):
            return True
    if labyrinth[spalte][zeile - 1] != 'X' and labyrinth[spalte][zeile - 1] != '#':
        if suchen(spalte, zeile - 1, labyrinth):
            return True
    if labyrinth[spalte + 1][zeile] != 'X' and labyrinth[spalte + 1][zeile] != '#':
        if suchen(spalte + 1, zeile, labyrinth):
            return True
    if labyrinth[spalte][zeile + 1] != 'X' and labyrinth[spalte][zeile + 1] != '#':
        if suchen(spalte, zeile + 1, labyrinth):
            return True
    labyrinth[spalte][zeile] = ' '
    return False

def count_paths(spalte, zeile, labyrinth,print=False,delay=0):
    if labyrinth[spalte][zeile] == 'A':
        if print:
            print_labyrinth(labyrinth)
            time.sleep(delay)
        return 1
    elif labyrinth[spalte][zeile] == ' ':
        labyrinth[spalte][zeile] = 'X'
        return count_paths(spalte-1, zeile, copy.deepcopy(labyrinth)) + count_paths(spalte, zeile-1, copy.deepcopy(labyrinth)) + count_paths(spalte+1, zeile, copy.deepcopy(labyrinth)) + count_paths(spalte, zeile+1, copy.deepcopy(labyrinth))
    return 0


parser = argparse.ArgumentParser(description='Calculate the number of ways through a labyrinth.')
parser.add_argument('filename', help='File containing the labyrinth to solve')
parser.add_argument('-x', '--xstart', type=int, help='x-coordinate to start')
parser.add_argument('-y', '--ystart', type=int, help='y-coordinate to start')
parser.add_argument('-p', '--print', action='store_true', help='Print output of every solution')
parser.add_argument('-t', '--time', action='store_true', help='Print total calculation time (in milliseconds)')
parser.add_argument('-d', '--delay', type=int, default=0, help='Delay after printing a solution (in milliseconds)')
args = parser.parse_args()

with cProfile.Profile() as profile:
    try:
        labyrinth=read_labyrinth(args.filename)

        start_time = time.time()
        total_paths = count_paths(args.xstart, args.ystart, labyrinth,args.print,args.delay)
        end_time = time.time()

        print("Anzahl an Pfaden:"+str(total_paths))

        if args.time:
            print("Die Gesamtzeit ist:"+str(round((end_time-start_time)*1000,2))+"millisekunden")

    except Exception as e:
        print(f"An error occurred: {e}")

results=pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
#results.print_stats()
results.dump_stats("results.prof")