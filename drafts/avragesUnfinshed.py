#our files
from matplotlib import pyplot as plt

from ..createGraph import createGraph
from read_unfinished_path import read_unfinished_path, getCentralityIndices



def avarageOf8OfOutDegree():
    """The function checks the average of centrality indices in tracks of the same length"""
    g = createGraph()
    allGames=read_unfinished_path(g)
    size=8

    sumGames=[0 for i in range(size)]
    counter=0
    for index, game in enumerate(allGames):
        if len(game) == size and '<' not in game:
            betw_game, in_deg_game, out_deg_game, pge_rnk_game, clos_game = funcListOfCentralityForGame(game)

            out_deg_game_avg=list(map(lambda x: x/sum(out_deg_game),out_deg_game)) #to get the proportional value
            temp=[x + y for x, y in zip(sumGames, out_deg_game_avg)]
            sumGames=temp
            counter+=1

    res=list(map(lambda x: x/counter, sumGames))
    game_clicks = list(range(0, size))

    plt.plot(game_clicks, res)
    plt.title('GAME STATISTICS : ')
    plt.xlabel('Game steps')
    plt.ylabel('out degree average')
    # plt.legend()
    # plt.show()

    # path = 'resultsAvg/'
    # file_name = path + str(index) + '.png'
    file_name='avgOutDegreeUnfinshed.png'
    plt.savefig(file_name)
    plt.cla()


if __name__ == '__main__':
    g = createGraph()
    lenNodes = len(g.nodes())
    lenEdges = len(g.edges())
    print(g)

    allGames = read_unfinished_path(g)
    funcListOfCentralityForGame = getCentralityIndices()
    avarageOf8OfOutDegree()

