from matplotlib import pyplot as plt
from urllib.parse import unquote
import networkx as nx

#our files
from createGraph import createGraph





# ------------------------------------------------------------
def game_statistics(game, index ):
    betw_game, in_deg_game, out_deg_game, pge_rnk_game, clos_game=funcListOfCentralityForGame(game)
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

    path='results/'
    file_name = path+str(index)+'.png'
    plt.savefig(file_name)
    plt.cla()

def getCentralityIndices():
    k=len(g.nodes()) #paramter to put inside the betweens but it takes time so meanwhile without it
    betweenness = nx.betweenness_centrality(g, k=100)
    # deg_centrality = nx.degree_centrality(g)
    in_degree = nx.in_degree_centrality(g)
    out_deg = nx.out_degree_centrality(g)
    page_rank = nx.pagerank(g)
    closeness= nx.closeness_centrality(g)

    def funcListOfCentralityForGame(game):
        betw_game = [betweenness[x] for x in game]
        in_deg_game = [in_degree[x] for x in game]
        out_deg_game = [out_deg[x] for x in game]
        pge_rnk_game = [page_rank[x] for x in game]
        clos_game = [closeness[x] for x in game]
        return betw_game,in_deg_game,out_deg_game,pge_rnk_game,clos_game

    return funcListOfCentralityForGame


def read_finished_path(g):
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

def loopGames(allGames):
    for index, game in enumerate(allGames):
        if len(game) >= 8 and '<' not in game:
            game_statistics(game,index)






g = createGraph()

if __name__=='__main__':
    lenNodes = len(g.nodes())
    lenEdges = len(g.edges())
    print(g)

    allGames= read_finished_path(g)
    funcListOfCentralityForGame = getCentralityIndices()
    loopGames(allGames)

