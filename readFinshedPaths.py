from urllib.parse import unquote

def read_finished_path():
    finishedPathFile = open('data/paths_finished.tsv', 'r')
    finishedPathLines = finishedPathFile.readlines()
    finishedPathFile.close()

    allGames=[]

    for line in finishedPathLines[16:]:
        new_line = line.replace('\n', ' ')
        new_line = new_line.replace('\t', ' ')
        new_line = new_line.split(' ')
        new_line = new_line[3]
        new_line = unquote(new_line)
        game = new_line.split(';')
        allGames.append(game)

    return allGames