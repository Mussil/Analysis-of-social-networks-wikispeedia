import statistics
from colour import Color

import matplotlib
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from createGraph import createGraph ,getCentralityIndices
from readPaths import read_finished_path , read_unfinished_path



def dataOnPaths(allGames,gamesWOBack):
    print(f"number of finished paths {len(allGames)}")
    print(f"number of finished paths without '<' {len(gamesWOBack)}")

def lengthOfGames(gamesWOBack):
    """ this function creates histogram of the length of the games"""
    lengthGames=list(map(len, gamesWOBack))

    plt.title('Length of finished games')
    # plt.yscale('log')
    plt.xlabel('length of game')
    plt.ylabel('frequency')

    plt.hist(lengthGames,bins=max(lengthGames),align='left',edgecolor='black',linewidth=0.5)
    plt.show()
    plt.cla()

def listOfClicksByOutDegree(allGames, getOutDegreePerGame,size):
    gamesOnlySize=list(filter(lambda x : len(x)==size, allGames))

    clicksOutDegree=[[] for i in range(size)]
    for game in list(gamesOnlySize):
        out_degree_game=getOutDegreePerGame(game)
        for i, out_degree in enumerate(out_degree_game):
            clicksOutDegree[i].append(out_degree)

    return len(gamesOnlySize),clicksOutDegree

def statsOutDegree(allGames, getOutDegreePerGame,size):
    """The function checks the average of centrality indices in tracks of the same length"""

    # gamesOnlySize=list(filter(lambda x : len(x)==size, allGames))
    #
    # clicksOutDegree=[[] for i in range(size)]
    # for game in list(gamesOnlySize):
    #     out_degree_game=getOutDegreePerGame(game)
    #     for i, out_degree in enumerate(out_degree_game):
    #         clicksOutDegree[i].append(out_degree)

    amount,clicksOutDegree=listOfClicksByOutDegree( allGames, getOutDegreePerGame, size)

    resAvg=list(map(lambda click: statistics.mean(click), clicksOutDegree))
    resMedian=list(map(lambda click: statistics.median(click), clicksOutDegree))
    resVariance=list(map(lambda click: statistics.variance(click), clicksOutDegree))
    resStdev=list(map(lambda click: statistics.stdev(click), clicksOutDegree))

    xAxis = list(range(0, size))
    slope, intercept = np.polyfit(xAxis[1:], resAvg[1:], 1)
    y=[x*slope+intercept for x in xAxis]
    # plt.plot(xAxis,y,label=f'slope of Avg {slope}')
    # plt.plot(xAxis, resAvg)
    # plt.boxplot(clicksOutDegree, meanline=True, whis=[0, 100], showfliers=False, showmeans=True,positions=xAxis)
    plt.errorbar(xAxis, resAvg ,resStdev, linestyle='None', marker='^' ,label='stdev')
    plt.plot(xAxis, resAvg , label='Average')
    plt.plot(xAxis, resMedian , label='Median')
    # plt.errorbar(xAxis, resAvg ,resVariance, linestyle='None', marker='^' ,label='Variance')

    plt.legend()

    plt.title(f'GAME STATISTICS \nNumber of clicks= {size}, Amount of games= {amount}')
    plt.xlabel('Game steps')
    plt.ylabel('Out degree')
    plt.xticks(xAxis,xAxis)
    # plt.show()

    path = 'resultsOfAvgClicks/'
    file_name = path + 'avgOutDegree' +str(size) +'.png'
    plt.savefig(file_name)
    plt.cla()

def compare(finished,unFinished,size):
    amountFinished,clicksOutDegreeFinished=listOfClicksByOutDegree( finished, getOutDegreePerGame, size)
    amountUnFinished,clicksOutDegreeUnFinished=listOfClicksByOutDegree( unFinished, getOutDegreePerGame, size)
    finishedAvg=list(map(lambda click: statistics.mean(click), clicksOutDegreeFinished))
    unFinishedAvg=list(map(lambda click: statistics.mean(click), clicksOutDegreeUnFinished))
    xAxis = list(range(0, size))
    slopeF, interceptF = np.polyfit(xAxis[1:-1], finishedAvg[1:-1], 1)
    yF=[x*slopeF+interceptF for x in xAxis]
    slopeUF, interceptUF = np.polyfit(xAxis[1:-1], unFinishedAvg[1:-1], 1)
    yUF=[x*slopeUF+interceptUF for x in xAxis]
    plt.plot(xAxis, finishedAvg ,label=f'Finished, amount of paths: {amountFinished}')
    plt.plot(xAxis, unFinishedAvg , label=f'Unfinished, amount of paths: {amountUnFinished}')
    plt.plot(xAxis, yF ,label=f'Slope finished', linestyle='dashed')
    plt.plot(xAxis, yUF ,label=f'Slope unfinished', linestyle='dashed')


    plt.legend()
    plt.xlabel('Game steps')
    plt.ylabel('Out degree average')
    plt.xticks(xAxis,xAxis)
    path = 'resultsOfAvgClicksCompare/'
    file_name = path + 'avgOutDegree' +str(size) +'.png'
    plt.savefig(file_name)
    plt.cla()


def compareSlopes(gamesF,gamesUF):
    sizeRange=range(3,15)

    slopesF=[]
    for size in sizeRange :
        xAxis = list(range(0, size))

        amountFinished, clicksOutDegreeFinished = listOfClicksByOutDegree(gamesF, getOutDegreePerGame, size)
        finishedAvg = list(map(lambda click: statistics.mean(click), clicksOutDegreeFinished))

        slopeF, interceptF = np.polyfit(xAxis[1:-1], finishedAvg[1:-1], 1)
        slopesF.append(slopeF)

    slopesUF=[]
    for size in sizeRange :
        xAxis = list(range(0, size))

        amountUFinished, clicksOutDegreeUFinished = listOfClicksByOutDegree(gamesUF, getOutDegreePerGame, size)
        unfinishedAvg = list(map(lambda click: statistics.mean(click), clicksOutDegreeUFinished))

        slopeUF, interceptUF = np.polyfit(xAxis[1:-1], unfinishedAvg[1:-1], 1)
        slopesUF.append(slopeUF)

    plt.xlabel('Game steps')
    plt.ylabel('Slopes')
    plt.xticks(xAxis,xAxis)

    plt.plot(sizeRange,slopesF, label='slope of finished path')
    plt.plot(sizeRange,slopesUF, label='slope of unfinished path')
    plt.legend()
    plt.show()


def avgAllClicks(allGames, getOutDegreePerGame):
    red = Color("lightgrey")
    rangeNumbers=range(3,11)
    colors = list(red.range_to(Color("black"), len(rangeNumbers)))
    listOfAmount=[]
    for size in rangeNumbers:
        xAxis = list(range(0, size))
        amount,clicksOutDegree=listOfClicksByOutDegree(allGames, getOutDegreePerGame, size)
        listOfAmount.append(amount)

    listOfAmount.sort()
    colorAmount=dict(zip(listOfAmount,colors))

    for size in rangeNumbers:
        xAxis = list(range(0, size))
        amount,clicksOutDegree=listOfClicksByOutDegree(allGames, getOutDegreePerGame, size)
        resAvg=list(map(lambda click: statistics.mean(click), clicksOutDegree))

        plt.plot(xAxis, resAvg,label=str(size) + ' amount:' +str(amount),color=colorAmount[amount].rgb )

    plt.legend()
    plt.xlabel('Game steps')
    plt.ylabel('Out degree average')
    plt.xticks(xAxis,xAxis)

    plt.show()

def wrapOutDegree():
    out_deg = g.out_degree()
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
        statsOutDegree( gamesWOBack, getOutDegreePerGame,size=i)

    avgAllClicks(gamesWOBack, getOutDegreePerGame)

    #---unFinished
    unFinishedGames=read_unfinished_path()
    unFinishedGamesWOBack = list(filter(lambda game: True if '<' not in game else False, unFinishedGames))
    # dataOnPaths(unFinishedGames, unFinishedGamesWOBack)
    # lengthOfGames(unFinishedGamesWOBack)
    # for i in range(2,15):
    #     statsOutDegree(g, unFinishedGamesWOBack, getOutDegreePerGame, size=i)
    for i in range(3,15):
        compare(gamesWOBack,unFinishedGamesWOBack,i)

    compareSlopes(gamesWOBack, unFinishedGamesWOBack)
