from matplotlib import pyplot as plt
from urllib.parse import unquote
import networkx as nx

#our files
from createGraph import createGraph



g=createGraph()
print(g)

# ------------------------------------------------------------
def game_statistics(game, betw, in_deg, out_deg, pge_rnk, clos, index):

    # betw_game = [betw[x] for x in game]
    # in_deg_game = [in_deg[x] for x in game]
    out_deg_game = [out_deg[x] for x in game]
    # pge_rnk_game = [pge_rnk[x] for x in game]
    # clos_game = [clos[x] for x in game]

    game_clicks = list(range(0, len(game)))

    # plt.plot(game, betw_game, label='Betweeness')
    # plt.plot(game, in_deg_game, label='In degree')
    plt.plot(game_clicks, out_deg_game, label='Out degree')
    # plt.plot(game, pge_rnk_game, label='Page rank')
    # plt.plot(game, clos_game, label='Closeness')

    plt.title('GAME STATISTICS : ')
    plt.xlabel('Game steps')
    plt.ylabel('Game indices')
    plt.legend()
    # plt.show()

    file_name = str(index)+'.png'
    plt.savefig(file_name)
    plt.cla()

def read_finished_path(g, Lines):

    betweenness = nx.betweenness_centrality(g, k=100, normalized=True, weight=None, endpoints=False, seed=None)
    # deg_centrality = nx.degree_centrality(g)
    in_degree = nx.in_degree_centrality(g)
    out_deg = nx.out_degree_centrality(g)
    page_rank = nx.pagerank(g, alpha=0.8)
    closeness= nx.closeness_centrality(g)

    index = 0

    for line in Lines[16:]:
        new_line = line.replace('\n', ' ')
        new_line = new_line.replace('\t', ' ')
        new_line = new_line.split(' ')
        new_line = new_line[3]
        new_line = unquote(new_line)
        game = new_line.split(';')

        if len(game) >= 8 and '<' not in game:
            index += 1
            game_statistics(game, betweenness, in_degree, out_deg, page_rank, closeness, index)

        # TODO: fix path with '<' and with '<<'
        # path = new_line.copy()
        # for article in new_line:
        #     if article == '<':
        #         del_index1 = new_line.index(article)
        #         del_index2 = del_index1-1
        #         # path.remove(article)
        #         while (del_index2 == '<') :
        #             del_index2 -= 1
        #         del path[del_index2:del_index1+1]
        #         print('----------------', path)


finishedPathFile = open('data/paths_finished.tsv', 'r')
finishedPathLines = finishedPathFile.readlines()
finishedPathFile.close()

read_finished_path(g, finishedPathLines)

