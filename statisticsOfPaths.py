import statistics

import networkx as nx
from matplotlib import pyplot as plt

from createGraph import createGraph ,getCentralityIndices
from readFinshedPaths import read_finished_path



def dataOnPaths(allGames,gamesWOBack):
    print(f"number of finished paths {len(allGames)}")
    print(f"number of finished paths without '<' {len(gamesWOBack)}")

def lengthOfGames(gamesWOBack):
    """ this function creates histogram of the length of the games"""
    lengthGames=list(map(len, gamesWOBack))
    print(lengthGames)

    plt.title('Length of finished games')
    plt.xlabel('length of game')
    plt.ylabel('frequency')

    plt.hist(lengthGames,bins=max(lengthGames),align='left',edgecolor='black',linewidth=0.5)
    plt.show()
    plt.cla()

def averageOutDegree(g,allGames, getOutDegreePerGame,size):
    """The function checks the average of centrality indices in tracks of the same length"""

    gamesOnlySize=list(filter(lambda x : len(x)==size, allGames))

    clicksOutDegree=[[] for i in range(size)]
    for game in list(gamesOnlySize):
        out_degree_game=getOutDegreePerGame(game)
        for i, out_degree in enumerate(out_degree_game):
            clicksOutDegree[i].append(out_degree)


    resAvg=list(map(lambda click: statistics.mean(click), clicksOutDegree))
    resMedian=list(map(lambda click: statistics.median(click), clicksOutDegree))
    resVariance=list(map(lambda click: statistics.variance(click), clicksOutDegree))
    resStdev=list(map(lambda click: statistics.stdev(click), clicksOutDegree))

    xAxis = list(range(0, size))

    # plt.plot(xAxis, resAvg)
    # plt.boxplot(clicksOutDegree, meanline=True, whis=[0, 100], showfliers=False, showmeans=True,positions=xAxis)
    plt.errorbar(xAxis, resAvg ,resStdev, linestyle='None', marker='^' ,label='stdev')
    plt.plot(xAxis, resAvg , label='Average')
    plt.plot(xAxis, resMedian , label='Median')
    # plt.errorbar(xAxis, resAvg ,resVariance, linestyle='None', marker='^' ,label='Variance')

    plt.legend()

    plt.title(f'GAME STATISTICS \nNumber of clicks= {size}, Amount of games= {len(gamesOnlySize)}')
    plt.xlabel('Game steps')
    plt.ylabel('Out degree')
    # plt.xticks(xAxis,xAxis)
    # plt.show()

    path = 'resultsOfAvgClicks/'
    file_name = path + 'avgOutDegree' +str(size) +'.png'
    plt.savefig(file_name)
    plt.cla()

def wrapOutDegree():
    out_deg = nx.out_degree_centrality(g)
    def getOutDegreePerGame(game):
        return [out_deg[x] for x in game]

    return getOutDegreePerGame



if __name__=='__main__':
    allGames = read_finished_path()
    gamesWOBack = list(filter(lambda game: True if '<' not in game else False, allGames))
    # dataOnPaths()
    # lengthOfGames(gamesWOBack)
    g=createGraph()
    # funcListOfCentralityForGame=getCentralityIndices(g)
    getOutDegreePerGame=wrapOutDegree()
    for i in range(2,15):
        averageOutDegree(g, gamesWOBack, getOutDegreePerGame, size=i)
